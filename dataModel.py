import numpy as np
import pandas as pd
import random

def create_data_model(DM_directory, XY_directory):
        """Stores the data for the problem."""
        data = {}
        data['DM'] = np.array(pd.read_csv(DM_directory, skiprows=[0], header=None).iloc[:, 1:])
        data['loc'] = np.array(pd.read_csv(XY_directory, header=None))

        data['depot'] = 0
        data['demands'] = [random.randrange(1, 10, 1) for i in range(len(data['loc']))]
        data['vehicle_capacities'] = [200, 200, 200, 200]
        data['num_vehicles'] = 4
        return data

# data=create_data_model('utils/distance_matrix.csv','utils/XYLondon.csv')
# routeNodes=data['loc']
# print(data['demands'])

