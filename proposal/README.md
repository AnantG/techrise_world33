# Proposal

[`world33_proposal_original.pdf`](world33_proposal_original.pdf) is the proposal **exactly as our team submitted it** to the NASA TechRise Student Challenge (December 2023). The text below is a word-for-word transcription so it's readable on GitHub. We left it unedited on purpose; what we would change now is in the reflection section of the [results](../results/).

---

## NASA TechRise Proposal

**Vehicle:** Weather Balloon  **Budget:** $1500

### Experiment Objective

We propose an experiment to address the following question: What combination of Carbon Dioxide, Nitrogen Dioxide, and Ozone most effectively absorbs UV radiation? We have gathered relevant information from credible sources regarding the elements involved in this experiment, which is outlined below.

- Ozone absorbs the majority of the radiation in our stratosphere and is formed when an oxygen atom is split into 2 oxygen atoms through UV radiation and then bonds to other oxygen atoms to naturally create ozone.
- With approximately a 3280-foot increase in altitude, UV levels will increase by approximately 10 percent.
- The ozone layer, Earth's sunscreen, absorbs about 98 percent of this devastating UV light.
- Ozone is good at trapping ultraviolet radiation, or UV light, which can penetrate organisms' protective layers, like skin.

We hypothesize that by sending the balloon seventy thousand feet above ground level, we predict to see:

1. Higher densities of air in the atmosphere usually correlate to higher levels of UV absorption.

### Experimental Design

Our goals for this experiment design is to collect and store data from our 6 sensors in a reliable and safe way. Another goal for this experiment design is to make sure that our sensors work in temperatures from -20～50℃. Our last goal is to make sure our systems have consistency and do not fail at high altitude from problems such as short circuit.

We will use a PCB layout that not only maximizes space efficiency but also ensures good operation of our sensors and data storage systems throughout the entire mission.

For the temperature constraint we will use insulation to maintain the sensors within the working temperature range of -20°C to 50°C, to make sure there are no effects on data collection due to varying temperatures at high altitudes.

In terms of software, our system will focus on collecting sensor data and continuously monitoring for massive inconsistencies in the data. By monitoring the data we can find irregularities and incorporate a system that alerts us of the massive irregularities at the end of the run. We will incorporate corrective measures in software to detect the issue and try to fix it self.

Overall our design pushes to collect reliable and consistent data for more accurate statistical analysis. By using different systems to keep everything safe and in working order, we are able to decrease the percentage of likely failures and high altitude.

### Required Materials

| Material | Manufacturer | Amount |
|---|---|---|
| Nitrogen Dioxide (NO₂) Sensor | DFRobot | 1 |
| Ultraviolet (UV) Radiation Sensor | Adafruit | 1 |
| Carbon Dioxide (CO₂) | Adafruit | 1 |
| Ozone (O₃) Sensor | Arduino | 1 |
| Micro SD Card Reader/Writer | Adafruit | 1 |
| Micro SD Card | Adafruit | 1 |

### Execution of the Experiment

Our plan involves launching a balloon and collecting gas concentration measurements at various altitudes. We aim to collect data on three main gasses which are: nitrogen dioxide, ozone, and carbon dioxide. Our project will utilize various sensors to collect data on the different gasses, along with collecting data on UV radiation every 1,000 feet 300 times, so we will collect data approximately 21,000 times. Data will be collected at altitudes between 15 and 30 km from ground level which is where the ozone layer can be found. We plan to identify the physical properties of the gasses beforehand since the sensors in our budget cannot differentiate between the gasses. These properties will be used to differentiate between the 3 gasses we want to collect data on.

The properties that distinguish all three gasses are their densities. Ozone at a density of 2.144g/L, Nitrogen with a density of 1.25 g/L, and Co2 with a density of 1.98 g/L. The sensors differentiate between the gasses using their densities.

The next step is organizing our data and using our data effectively. A classic choice would be to graph our data and find a relationship between the UV radiation and the composition of the gasses. The different altitudes will allow us to collect data from varying gas compositions, and they will also help us monitor the level of UV radiation at those levels. Through this process, the data will allow us to find a relationship between the two categories.

This relationship will then be modeled by a best fit. Using the best fit, we can derive an equation to represent it. Since we are looking at the 3 main gasses in the atmosphere, we can make several 2-dimensional graphs and 3-dimensional graphs.

### Relevance of the Experiment

It is important to understand how the composition of our atmosphere affects things like radiation to understand our atmosphere better and to emphasize this to future generations. We can also utilize our data to predict the effect of UV radiation in certain areas of the atmosphere. Moreover, we can understand the gasses that protect our lives from UV rays and also understand how to prepare other planets to be able to sustain life. Our everyday lives depend on these gasses and learning more about their operations in the atmosphere can dictate the creation of new ideas and innovation.

In addition to studying the effects of these gasses on radiation, it is also important to know their importance to life on Earth considering these gasses deal with more than just radiation. One of the main reasons carbon dioxide is important to the well-being of the Earth is that it is crucial to maintaining the perfect temperature. Carbon dioxide is a greenhouse gas that prevents too much heat from escaping the atmosphere. Without carbon dioxide, the Earth would be a cold and desolate planet. Similarly, nitrogen is equally important to life on Earth but for a different reason. Without nitrogen, there would be little to no life on Earth since it is an essential component of building blocks, like proteins. Unlike carbon dioxide and nitrogen, the main purpose of ozone is to prevent harmful ultraviolet radiation from reaching Earth. If there was no ozone to protect us, most plant and animal life would be endangered by the harmful diseases and illnesses the radiation would cause. Although these gasses deal with ultraviolet radiation, they all have their own jobs that support life on Earth. By sending up our payload we can better study our atmosphere and come up with methods to preserve life for future generations.
