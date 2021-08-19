def distance_calculation(data, routing, solution):


    distance=[]
    time=[]
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        number_of_parcels = 0
        while not routing.IsEnd(index):

            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
            number_of_parcels+=1
        distance.append(route_distance/1000)
        time.append(round((route_distance/40000)+(2*number_of_parcels/60),1))
    #distance.append(sum(distance))
    return distance,time

