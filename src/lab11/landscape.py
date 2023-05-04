import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np

landType ={
    "Sea": [0,35],
    "Marsh": [50,36],
    "Plain": [51,99],
    "Hill": [100,186],
    "Mount": [187,250],
}

def game_fitness(cities, idx, elevation, size):
    fitness = 0.0001  # Do not return a fitness of 0, it will mess up the algorithm.
    """
    Create your fitness function here to fulfill the following criteria:
    1. The cities should not be under water
    2. The cities should have a realistic distribution across the landscape
    3. The cities may also not be on top of mountains or on top of each other
    DO NOt return fitness of 0 or less
    """

    for city in cities:
        #1. Make sure city location elevation is below a number
        if elevation[city[0]][city[1]][0] > landType["Marsh"][1]:
            fitness += 5
        elif elevation[city[0]][city[1]][0] > landType["Sea"][1]:
            fitness += 1

        #2. Check if cities are farthere away
        for otherCity in slice(cities.index(city)):
            dis = math.dist(city,otherCity)
            if dis > 10:
                fitness += 5
            if dis > 3:
                fitness += 1

        #3. Make sure city location elevation is above a number
        if elevation[city[0]][city[1]][0] < landType["Mount"][1]:
            fitness += 1
        elif elevation[city[0]][city[1]][0] < landType["Hill"][1]:
            fitness += 5

        if fitness > idx:
            fitness = idx
    return fitness

#Calculates cost
def get_route_cost(current_city, final_city, elivation):
    costs =[]
    while current_city != final_city:
        #determine if x needs to move right of left
        x = current_city[0]
        if x < final_city[0]:
            x +=  + 1
        elif x > final_city[0]:
            x -= 1
     
        #determine if y needs to move up of down
        y = current_city[1]
        if y < final_city[1]:
            y += 1
        elif y > final_city[1]:
                y -= 1
        
        current_city = (x,y)
        current_elivation = elivation[x][y][0]

        #check if in sea
        if current_elivation <= landType["Sea"][1]:
            cost = 0.6
        #check if in Marsh
        elif current_elivation <= landType["Marsh"][1] and current_elivation >= landType["Marsh"][0]:
            cost = 0.3
        #check if in plain
        elif current_elivation <= landType["Plain"][1] and current_elivation >= landType["Plain"][0]:
            cost = 0.1
        #check if in Hill
        elif current_elivation <= landType["Hill"][1] and current_elivation >= landType["Hill"][0]:
            cost = 0.2
        #check if in Mountin
        elif current_elivation <= landType["Mount"][1] and current_elivation >= landType["Mount"][0]:
            cost = 0.4
        #In peaks
        else:
            cost = 0.5

        costs.append(cost)

    return round(sum(costs),2)

def get_elevation(size, octaves=3):
    xpix, ypix = size
    noise = PerlinNoise(octaves=octaves, seed=2)
    # elevation = np.random.random(size)
    elevation = np.array(
        [[noise([i / xpix, j / ypix]) for j in range(ypix)] for i in range(xpix)]
    )
    return elevation


def elevation_to_rgba(elevation, cmap="gist_earth"):
    xpix, ypix = np.array(elevation).shape
    colormap = plt.cm.get_cmap(cmap)
    elevation = (elevation - elevation.min()) / (elevation.max() - elevation.min())
    landscape = (
        np.array(
            [colormap(elevation[i, j])[0:3] for i in range(xpix) for j in range(ypix)]
        ).reshape(xpix, ypix, 3)
        * 255
    )
    landscape = landscape.astype("uint8")
    return landscape


get_landscape = lambda pixel_map: elevation_to_rgba(get_elevation(pixel_map))
get_combat_bg = lambda pixel_map: elevation_to_rgba(
    get_elevation(pixel_map, 10), "RdPu"
)




if __name__ == "__main__":
    size = 640, 480
    el = get_elevation(size)
    pic = elevation_to_rgba(el)
    print(pic[0][0][0])
    plt.imshow(pic, cmap="gist_earth")
    plt.show()
