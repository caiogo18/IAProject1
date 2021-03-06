#https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce
#https://fr.wikipedia.org/wiki/2-opt
#https://fr.wikipedia.org/wiki/Recherche_locale_(optimisation)
from RandomCityMap import RandomCityMap

def getTotalCost(path, costs):
    cost = 0
    for i in range(0, len(path)):
        if i+1 == len(path):
            j = 0
        else:
            j = i+1
        cost += getCost(path[i], path[j], costs)
    return cost

def getCost(pointA, pointB, costs):
    if pointA < pointB:
        return costs[(pointA, pointB)]
    else:
        return costs[(pointB, pointA)]    

def localSearch(cities, costs):
    path = list(cities)
    improvement = True
    while improvement:
        improvement = False
        for i in range(0, len(path)):
            if i+1 == len(path):
                break
            
            for j in range(0, len(path)):
                if j == i or j == i-1 or j == i+1:
                    continue
                if j+1 == len(path):
                    break
                actualPathCost = getCost(path[i], path[i+1], costs) + getCost(path[j], path[j+1], costs)
                newPathCost = getCost(path[i], path[j], costs) + getCost(path[i+1], path[j+1], costs)
                #actualPathCost = getCost(path[i], path[i+1], costs)
                #newPathCost = getCost(path[i], path[j], costs)
                if actualPathCost > newPathCost:
                    temp = path[i+1]
                    path[i+1] = path[j]
                    path[j] = temp
                    improvement = True
    return (path, getTotalCost(path, costs))

cities1 = ('A','B','C','D','E')
costs1 = {
            ('A', 'B') : 3,
            ('A', 'C') : 100,
            ('A', 'D') : 8,
            ('A', 'E') : 1,
            ('B', 'C') : 6,
            ('B', 'D') : 1,
            ('B', 'E') : 1,
            ('C', 'D') : 6,
            ('C', 'E') : 7,
            ('D', 'E') : 5        
        }  
cityMap1 = RandomCityMap(10)
print(cityMap1.getCityList())
print(cityMap1.getCosts())
print(cityMap1.getCostBetweenCities(1,5))
print(cityMap1.getTotalCost(cityMap1.getCityList()))
print(localSearch(cities1, costs1))

