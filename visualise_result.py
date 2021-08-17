import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

def visualise_solution(data, manager, routing, solution):
    """Prints solution on console."""

    # plotting results
    plt.figure(figsize=(10, 7))
    color = ['blue', 'green', 'cyan', 'black', 'red', 'black', 'yellow', 'brown']


    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route = []
        route_distance=0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)

            route.append(data['loc'][node_index])
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)

        route.append(data['loc'][manager.IndexToNode(index)])


        lat= [la[0] for la in route]
        long=[lo[1] for lo in route]

        if len(lat)>2:
            plt.text(lat[3], long[3], 'vehicle {0} with size of {1} & time of {2}'.format(vehicle_id,len(lat),round(route_distance/40000,1)))
            plt.scatter(lat, long, c=color[vehicle_id])
            plt.plot(lat, long, linestyle='-', marker='x')
    plt.xlabel("Longitude", fontdict=font2)
    plt.ylabel("Latitude", fontdict=font2)
    plt.show()


