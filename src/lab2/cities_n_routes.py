''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of and all possible routes between them.
'''
import random
import itertools

def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of to be generated 
    and returns a list of with their x and y coordinates. The are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of to generate
    :return: A list of with random x and y coordinates, as a tuble of 2 ints.
    """
    # Consider the condition where x size and y size are different
    city_list = []

    i = 0
    while i < n_cities:
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        cord = (x,y)
        city_list.append(cord)
        i += 1
        

    return city_list
    

def get_routes(city_names):
    """
    It takes a list of and returns a list of all possible routes between those. 
    Equivalently, all possible routes is just all the possible pairs of the. 
    
    :param: a list of city names
    :return: A list of tuples representing all possible links between/ pairs of, 
            each item in the list (a link) represents a route between two.
            a,b,c
            [(a, b), (b,c), (b,c)]
            intertools.combinatioms(list, size 2) gives all combinations
    """
    route_Combinations = list(itertools.combinations(city_names, 2))
    return route_Combinations



# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the and routes'''
    city_coordinate = get_randomly_spread_cities((100, 200), len(city_names))
    routes = get_routes(city_names)
    print('City Coordinates:')
    for i, city in enumerate(city_coordinate):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(routes):
        print(f'{i}: {route[0]} to {route[1]}')
