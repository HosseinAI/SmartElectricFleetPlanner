"""Capacited Vehicles Routing Problem (CVRP)."""


from path_feature_calculator import distance_calculation
import local_Search
from print_result import print_solution
from dataModel import create_data_model


def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model('utils/distance_matrix.csv','utils/XYLondon.csv')

    dist_from_depot= data['distance_from_depot'].sort(reverse=True)


    solution, routing = local_Search.Routing(data)
    route_distances,route_time= distance_calculation(data, routing, solution)


    i=0
    for time in route_time:

        if time >data['drive_time'][i] :
            run_out=True
        else:
            run_out=False
        while run_out:
            data['vehicle_capacities'][i]=data['vehicle_capacities'][i]*0.8
            solution,routing = local_Search.Routing(data)
            route_distances,route_time= distance_calculation(data, routing, solution)
            time=route_time[i]





            if  max(route_time)> max(data['drive_time']):
                i=route_time.index(max(route_time))
                data['vehicle_capacities'][i] = data['vehicle_capacities'][i] * 0.8

            if time <= data['drive_time'][i] and max(route_time)<= max(data['drive_time']):
                run_out = False
        i=i+1

    # longest_route= max(route_distances)
    # longest_route_time = max(route_time)
    #
    # while longest_route_time>4:
    #
    #     index_ofmax=data['vehicle_capacities'].index(max(data['vehicle_capacities']))
    #     data['vehicle_capacities'][index_ofmax]  =data['vehicle_capacities'][index_ofmax]*0.8
    #     solution,routing = local_Search.Routing(data)
    #     route_distances,route_time= distance_calculation(data, routing, solution)
    #     longest_route_time= max(route_time)


if __name__ == '__main__':
    main()