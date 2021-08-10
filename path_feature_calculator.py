def distance_calculation(data, routing, solution):


    distance=[]
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0

        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)

        distance.append(route_distance/250)
    #distance.append(sum(distance))
    return distance

