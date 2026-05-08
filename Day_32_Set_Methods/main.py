# s1 = {2, 3, 8, 3 ,29}
# s2 = {5, 4, 3, 4, 0, 23}
# s1.update(s2)
# print(s1.union(s2))
# print(s1, s2)



# cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
# cities3 = cities1.union(cities2)
# print(cities3)
# cities4 = cities1.intersection(cities2)
# print(cities4)



# cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
# cities1.intersection_update(cities2)
# print(cities1)



# cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)



# cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
# cities3 = cities1.difference(cities2)
# print(cities3)



# cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
# print(cities1.isdisjoint(cities2))



# cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities2 = {"Pune", "Mumbai"}
# cities3 = {"Mumbai", "Nagpur", "Sangli"}
# print(cities1.issuperset(cities2))
# print(cities2.issuperset(cities3))



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))


# cities = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities.add("Jaypur")
# print(cities)



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2)
# print(cities)



# cities = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# cities.remove("Pune")
# print(cities)



# cities = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
# item = cities.pop()
# print(item)



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)



# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")