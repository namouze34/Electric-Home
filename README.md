# Electric-Home
Terra.Do Climate Stack course project

2/20/2024: the project was continued beyond the Terra.Do class to integrate NREL OCHRE Home energy model

SUMMARY: Building on the home energy model from assignment 2.2b. The goal of this project is to build the equivalent of Google Sunroof Project (which provides quick estimates on size and ROI for a rootop solar system) but for home electrification.

Scope of work:
The existing home energy model from assignment 2.2b is based on the assumption that the home is using an efficient electric heat pump for heating and cooling.
One of the first thing to do will be to adapt the model to consider that the heating is done by a natural gas furnace (we will only consider this heating mode because it represents 88% of homes in the pilot city of Fair Lawn and we want to motivate people to switch from a gas furnace to an electric heat pump). A conventional furnace has an efficiency of 0.8 and modern high efficiency furnace has an efficiency of 0.95. We can start by modeling only one type of furnace (conventional or high efficiency). Typical furnaces range between 80000 BTU and 100000 BTU (input of energy).
From there we could sum the energy use of the gas furnace from October to April, convert the kwh to therms (1 US therm = 29.3 kwh), calculate the heating bills total (with local utility -PSEG- rate 1 therm = 1.0092 USD), and CO2eq emissions (1 therm = 0.0053 metric ton CO2eq).
Second step would be to consider the current home energy model from assignment 2.2b with a typical heat pump 3.5 tons or 42000 BTU and run the model to calculate the energy use. We would then again sum the energy use from October to April, calculate the total heating cost (with local utility PSEG 1 kwh = 0.1921 USD) and CO2eq emissions (1 kwh = .000305 metric ton CO2eq according to EGrid).
Last step would be to graph the emissions and heating costs with a furnace and heat pump using a bar graph and display the “savings”.
Additional features (nice to have):
We can even try to calculate a typical Return On Investment: a cold climate 3.5 tons heat pump is probably between 15K and 20K installation included. The IRA provide a 30% tax credit, and credits will be made available in 2024 if the household income does not exceed 150% of the local median income (see rewiring america website)
It’s probably better to consider a Typical Meteorological Year for accuracy.
If somebody is familiar with web development we could develop a basic user interface to enter parameters like furnace size (in BTU, by default would be 100K because contractors tend to oversize), ACH value (if the own had somebody do a blower door test, otherwise we would consider ACH=15 because most houses in Fair Lawn were built in the 40s or 50s and so are pretty drafty. For reference I did some weatherization on my home, before improvement the ACH was 16 and after it was 10.3), square footage, size of windows on the south facing side (we can put a defaut value of 3.5 m^2 or 110 sq.ft).

For context, as part of the implementation of New Jersey Energy Master Plan at municipality level (through a Community Energy Plan) the Climate Action Committee of Fair Lawn that I am chairing is considering doing a residential and commercial outreach campaign to motivate residents to implement energy efficiency initiatives in their homes. The electric home project tool could be a useful tool to assess the benefits of electrifying the heating mode (which is responsible for 20% of the community CO2 emissions).


