"""Capacited Vehicles Routing Problem (CVRP)."""
from path_feature_calculator import distance_calculation
from print_result import print_solution
from dataModel import create_data_model
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from visualise_result import visualise_solution


def Routing(data):

    manager = pywrapcp.RoutingIndexManager(len(data['DM']),
                                           data['num_vehicles'], data['depot'])
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['DM'][from_node][to_node]
    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(1)
    routing.AddDimensionWithVehicleCapacity(demand_callback_index,0, data['vehicle_capacities'],True,'Capacity')
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)
        visualise_solution(data, manager, routing, solution)
    return solution,routing



def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model('utils/distance_matrix.csv','utils/XYLondon.csv')

    solution,routing = Routing(data)

    route_distances= distance_calculation(data, routing, solution)
    # for dist in route_distances:
    #     data['num_vehicles']
    #     if dist >2300 :
    #         i=route_distances.index(dist)
    #         good=True
    #     else:
    #         good=False
    #     while good:
    #         data['vehicle_capacities'][i]=data['vehicle_capacities'][i]*0.8
    #         solution,routing = Routing(data)
    #         route_distances = distance_calculation(data, routing, solution)
    #         dist=route_distances
    #
    #         if dist < 2300:
    #             good = False
    # longest_route= max(route_distances)
    #
    # while longest_route>8:
    #
    #     index_ofmax=data['vehicle_capacities'].index(max(data['vehicle_capacities']))
    #     data['vehicle_capacities'][index_ofmax]  =data['vehicle_capacities'][index_ofmax]*0.8
    #     solution,routing = Routing(data)
    #     route_distances = distance_calculation(data, routing, solution)
    #     longest_route= max(route_distances)


if __name__ == '__main__':
    main()