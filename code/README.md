# Code

All code targets the **Adafruit Metro M4 Express** connected to the TechRise **Payload Interface Board (PIB)**, which forwards World View balloon telemetry over UART (9600 baud, one 38-byte packet per second).

| Folder | File | What it is | Author |
|---|---|---|---|
| `flight/` | `WORLD33_code.py` | Our CircuitPython flight loop: reads balloon telemetry, detects flight-phase changes, and appends each packet to `/sd/WORLD.txt` on the microSD card. | Team WORLD-33 |
| `flight/` | `worldview_lib.py` | Telemetry parser for the World View data stream. | Future Engineers starter library, **modified by Team WORLD-33** (see below) |
| `arduino-demo/` | `worldview.ino` | Arduino version of the telemetry demo, used while we were comparing Arduino with CircuitPython. | Future Engineers demo, **modified by Team WORLD-33** (GO LED blink logic) |
| `component-tests/` | `SDIO_code.py` | Test that writes "Hello World!" to the microSD breakout every 2 s, used to verify SD wiring before integrating it. | Adafruit example (MIT) |

## What we changed in the Future Engineers library

`worldview_lib.py` started as the Future Engineers TechRise starter library (written by Mark DeLoura and Arnie Martin). We added:

- **Status-color NeoPixel:** the on-board LED changes color with flight phase (initializing, launching, floating, terminating).
- **GO-LED blink codes,** so the payload's state can be read from outside the flight box:
  - PBF inserted, no data: slow blink (5 s)
  - PBF inserted, data streaming: medium blink (3 s)
  - PBF removed, no data: fast blink (1 s)
  - PBF removed, data streaming: solid on
- A public `prev_status` attribute so the main loop can log phase transitions.

These files are included for reference with attribution to Future Engineers. They are **not** covered by this repository's MIT license.

## Running it

1. Flash the Metro M4 Express with **CircuitPython 8.2.x**. We used 8.2.10, available from [circuitpython.org](https://circuitpython.org/board/metro_m4_express/).
2. Copy the required libraries (`neopixel.mpy`) from the CircuitPython library bundle into `CIRCUITPY/lib/`.
3. Copy `worldview_lib.py` to the board, and copy `WORLD33_code.py` to the board as `code.py`.
4. Connect the PIB, then stream data from the TechRise web simulator. A real flight provides the same stream.
5. Wiring: see [`../hardware/`](../hardware/). The SD card uses SPI with chip-select on **D10**.

Each logged line is CSV:

```
time, latitude, longitude, altitude_m, speed_mps, heading_deg, velocity_down_mps, pressure_pa, temperature_c
```

Flight-phase changes are written to the log as plain-text lines between data rows.
