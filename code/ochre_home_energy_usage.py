#OCHRE install
%pip install ochre-nrel

from ochre.utils import default_input_path  # for using sample files

import os
import datetime as dt
import pandas as pd

import sys
sys.path.append(r'C:\Users\mblonsky\Github\OCHRE\ochre')
from ochre import Dwelling
from ochre.utils import default_input_path  # for using sample files

simulation_name = 'Sample House'

dwelling_args = {
    # Timing parameters
    'start_time': dt.datetime(2018, 1, 1, 0, 0),  # year, month, day, hour, minute
    'time_res': dt.timedelta(minutes=10),         # time resolution of the simulation
    'duration': dt.timedelta(days=365),             # duration of the simulation

    # Input files
#    'hpxml_file': os.path.join(default_input_path, 'Input Files', 'sample_resstock_properties.xml'),
    'hpxml_file': os.path.join("/hex", "sample_resstock_properties_gas_furnace.xml"),
#    'hpxml_file': os.path.join("/hex", "sample_resstock_properties_heat_pump.xml"),    
    'schedule_input_file': os.path.join(default_input_path, 'Input Files', 'sample_resstock_schedule.csv'),
    'weather_file': os.path.join("/hex", "USA_NJ_Teterboro.AP.725025_TMY3.epw"),

    # Output parameters
    'verbosity': 4,                         # verbosity of time series files (0-9)
    'output_path': os.getcwd(),             # defaults to properties_file path

    # Equipment parameters (see bin/run_dwelling.py for more options)
    # 'Equipment': {
    #     'PV': {
    #         'capacity': 5,   # in kW
    #         'tilt': 20,      # in degrees
    #         'azimuth': 180,  # in degrees
    #     }
    # },
}

# Create Dwelling model
dwelling = Dwelling(name=simulation_name, **dwelling_args)

# Run OCHRE simulation (returns DataFrames of timeseries results and a dictionary of metrics)
df_baseline, metrics, hourly = dwelling.simulate()

# Load results from previous run
# output_path = dwelling_args.get('output_path', os.path.dirname(dwelling_args['properties_file']))
# df, metrics, hourly = Analysis.load_ochre(output_path, simulation_name)

df_baseline.head()

metrics

%matplotlib

from ochre import CreateFigures

# Plot results
CreateFigures.plot_power_stack(df_baseline)
CreateFigures.plot_daily_profile(df_baseline, 'Total Electric Power (kW)', plot_max=False, plot_min=False)
