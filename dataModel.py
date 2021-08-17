from scipy.spatial import distance
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
        data['vehicle_capacities'] = [300, 500,300]
        data['drive_time']=[4,3,2]
        data['num_vehicles'] = 3
        data['distance_from_depot']= [distance.euclidean(data['loc'][data['depot']], i) for i in data['loc']]
        return data

# data=create_data_model('utils/distance_matrix.csv','utils/XYLondon.csv')
# routeNodes=data['loc']
# print(data['distance_from_depot'])

