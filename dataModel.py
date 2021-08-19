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
        data['demands'] = [4, 6, 9, 4, 5, 2, 1, 6, 7, 5, 6, 7, 9, 1, 5, 6,
                           7, 8, 4, 7, 1, 1, 5, 8, 5, 5, 5, 4, 4, 1, 7, 2,
                           6, 3, 2, 6, 7, 7, 5, 6, 7, 7, 4, 9, 3, 8, 6, 4,
                           4, 2, 7, 7, 7, 5, 1, 5, 1, 5, 3, 3, 4, 8, 9, 6,
                           2, 1, 1, 2, 3, 7, 7, 6, 8, 4, 6, 4, 2, 6, 3, 1,
                           9, 7, 2, 2, 9, 4, 1, 3, 2, 9, 3, 1, 3, 9, 3, 4,
                           4, 1, 6, 8, 8]
        data['vehicle_capacities'] = [1000,1000,1000]
        data['drive_time']=[4,6,8]
        data['num_vehicles'] = 3
        data['distance_from_depot']= [distance.euclidean(data['loc'][data['depot']], i) for i in data['loc']]
        return data

# data=create_data_model('utils/distance_matrix.csv','utils/XYLondon.csv')
# routeNodes=data['loc']
# print(data['demands'])

