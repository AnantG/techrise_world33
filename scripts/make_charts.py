"""
Regenerates the charts in results/charts/ from results/data/world33_flight_data.csv.

Usage (from the repository root):
    pip install pandas matplotlib
    python scripts/make_charts.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "results" / "data" / "world33_flight_data.csv"
OUT = ROOT / "results" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

BLUE = "C0"          # matplotlib's default first color
BAND = "0.9"         # light gray for the float band

LAUNCH_SITE_ALT_M = 1400   # anything above this is "off the ground"
FLOAT_ALT_M = 23000        # float altitude threshold used for shading

matplotlib.rcdefaults()
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["savefig.dpi"] = 160

d = pd.read_csv(DATA)
# One telemetry packet came through as all zeros (altitude/lat/lon = 0); drop it for plotting.
d = d[d.altitude_m > 0].copy()
d["hours"] = d.time_balloon_s / 3600
d["altitude_km"] = d.altitude_m / 1000

aloft = d[d.altitude_m > LAUNCH_SITE_ALT_M]
floating = d[d.altitude_m > FLOAT_ALT_M]
float_start, float_end = floating.hours.min(), floating.hours.max()


def shade_float(ax):
    ax.axvspan(float_start, float_end, color=BAND, zorder=0, lw=0)


# 1. Flight profile ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4))
shade_float(ax)
ax.plot(d.hours, d.altitude_km, color=BLUE, lw=2)
peak = d.loc[d.altitude_m.idxmax()]
ax.annotate(f"Peak {peak.altitude_km:.1f} km",
            xy=(peak.hours, peak.altitude_km), xytext=(peak.hours + 0.4, peak.altitude_km - 4),
            arrowprops=dict(arrowstyle="-", lw=0.8))
ax.text((float_start + float_end) / 2, 2.5, "float (> 23 km)", ha="center")
ax.set_title("WORLD-33 flight profile")
ax.set_xlabel("Time since balloon telemetry start (hours)")
ax.set_ylabel("Altitude (km)")
ax.set_ylim(0, 27)
fig.tight_layout()
fig.savefig(OUT / "flight_profile.png")
plt.close(fig)

# 2. Every sensor over the flight (small multiples, shared time axis) -------
panels = [
    ("temperature_c", "Temperature (°C)"),
    ("humidity_pct", "Relative humidity (%)"),
    ("uvs_raw", "UV index sensor (raw counts)"),
    ("ozone_raw", "Ozone sensor (raw; see notes on units)"),
    ("co2_ppm", "CO2 (ppm)"),
    ("no2_ppm", "NO2 (ppm)"),
]
fig, axes = plt.subplots(3, 2, figsize=(10, 8.5), sharex=True)
for ax, (col, title) in zip(axes.flat, panels):
    shade_float(ax)
    ax.scatter(d.hours, d[col], s=2, color=BLUE, lw=0)
    ax.set_title(title)
for ax in axes[-1]:
    ax.set_xlabel("Hours since telemetry start")
fig.suptitle("Sensor readings across the flight (gray band = float above 23 km)",
             fontsize=12)
fig.tight_layout()
fig.savefig(OUT / "sensors_over_time.png")
plt.close(fig)

# 3. UV vs each gas, aloft only ----------------------------------------------
gases = [
    ("ozone_raw", "Ozone sensor (raw)", aloft),
    ("co2_ppm", "CO2 (ppm), zero readings removed", aloft[aloft.co2_ppm > 0]),
    ("no2_ppm", "NO2 (ppm)", aloft),
]
fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), sharey=True)
for ax, (col, label, sub) in zip(axes, gases):
    ax.scatter(sub[col], sub.uvs_raw, s=8, color=BLUE, alpha=0.35, lw=0)
    ax.set_xlabel(label)
    ax.set_title(f"UV vs {label.split(' ')[0]}")
axes[0].set_ylabel("UV index sensor (raw)")
fig.tight_layout()
fig.savefig(OUT / "uv_vs_gases.png")
plt.close(fig)

print("Charts written to", OUT)
