from services.data_analysis.tools.core import *

# Calcula dados e os agrega
def analyse_data_from_data(data:list, name:str):
    mean = get_mean_by_list(data, int)
    mode = get_mode_by_list(data, int)
    median = get_median_by_list(data, int)
    max_value = get_max_by_list(data, int)
    min_value = get_min_by_list(data, int)

    return {name: {**mean, **median, **mode, **max_value, **min_value}}



