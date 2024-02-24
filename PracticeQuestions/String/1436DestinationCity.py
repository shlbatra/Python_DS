#You are given the array paths, where 
# paths[i] = [cityAi, cityBi] means there exists a 
# direct path going from cityAi to cityBi. Return
#  the destination city, that is, the city without any 
# path outgoing to another city.

# Alternate solution
# A, B = map(set, zip(*paths))
# return (B - A).pop()

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict_outgoing = {}
        for path in paths:
            city_a, city_b = path
            dict_outgoing[city_a] = dict_outgoing.get(city_a,0) + 1
            dict_outgoing[city_b] = dict_outgoing.get(city_b,0)
        
        for city in dict_outgoing:
            if dict_outgoing[city] == 0:
                return city
            
