"""Capacited Vehicles Routing Problem (CVRP)."""


from path_feature_calculator import distance_calculation
import local_Search
from print_result import print_solution
from dataModel import create_data_model


def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model('utils/distance_matrix.csv','utils/XYLondon.csv')



    solution, routing = local_Search.Routing(data)
    route_distances,route_time= distance_calculation(data, routing, solution)



    # for dist in route_distances:
    #     data['num_vehicles']
    #     if dist >230000 :
    #         i=route_distances.index(dist)
    #         good=True
    #     else:
    #         good=False
    #     while good:
    #         data['vehicle_capacities'][i]=data['vehicle_capacities'][i]*0.8
    #         solution,routing = local_Search.Routing(data)
    #         route_distances = distance_calculation(data, routing, solution)
    #         dist=route_distances
    #
    #         if dist < 2300:
    #             good = False
    longest_route= max(route_distances)
    longest_route_time = max(route_time)

    while longest_route_time>3:

        index_ofmax=data['vehicle_capacities'].index(max(data['vehicle_capacities']))
        data['vehicle_capacities'][index_ofmax]  =data['vehicle_capacities'][index_ofmax]*0.8
        solution,routing = local_Search.Routing(data)
        route_distances,route_time= distance_calculation(data, routing, solution)
        longest_route_time= max(route_time)


if __name__ == '__main__':
    main()