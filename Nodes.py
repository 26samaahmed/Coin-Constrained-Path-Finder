
class City:
    def __init__(self, cityName, heuristic):
        self.cityName = cityName
        self.heuristic = heuristic
        self.roads = {} # dictionary for the city to be able to connect to multiple cities with a cost 

    def connect(self, neighbor_city, cost):
        # rice an err if the node connection already exist 
        if neighbor_city in self.roads:
            raise ValueError(f"{self.cityName} already connected to {neighbor_city.cityName}.")
        if self in neighbor_city.roads:
            raise ValueError(f"{neighbor_city.cityName} already connected to {self.cityName}.")
        
        # create the connection going both ways 
        self.roads[neighbor_city] = cost
        neighbor_city.roads[self] = cost 

    def get_heuristic(self):
        return self.heuristic
    
    def get_cost_to(self, neighbor_city):
        #Return the cost if the connection exist, if not it retunr -1
        return self.roads.get(neighbor_city, -1)


