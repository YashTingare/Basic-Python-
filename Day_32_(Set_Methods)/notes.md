# Joining Sets

Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

## I. union() and update():

The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

```py
s1 = {2, 3, 8, 3 ,29}
s2 = {5, 4, 3, 4, 0, 23}
s1.update(s2)
print(s1.union(s2))
print(s1, s2)
```

## II. Intersection and Intersection_update():

The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

```py
cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
cities3 = cities1.union(cities2)
print(cities3)
cities4 = cities1.intersection(cities2)
print(cities4)
```

```py
cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
cities1.intersection_update(cities2)
print(cities1)
```

## III. Symmetric_difference and Symmetric_difference_update():

The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

```py
cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
cities3 = cities1.difference(cities2)
print(cities3)
```

```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
```

## IV. difference() and difference_update():

The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

```py
cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
cities3 = cities1.difference(cities2)
print(cities3)
```

# Set Methods

There are several in-built methods used for the manipulation of set.They are explained below

## isdisjoin():
 
 The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

```py
cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
cities2 = {"Pune", "Kolhapur", "Mumbai", "Bhiwandi"}
print(cities1.isdisjoint(cities2))
```

## issuperset():

The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

```py
cities1 = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
cities2 = {"Pune", "Mumbai"}
cities3 = {"Mumbai", "Nagpur", "Sangli"}
print(cities1.issuperset(cities2))
print(cities2.issuperset(cities3))
```

## issubset():

The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
```

## add():

If you want to add a single item to the set use the add() method

```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
```

## update():

If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
```

## remove():

We can use remove() and discard() methods to remove items form list.

```py
cities = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
cities.remove("Pune")
print(cities)
```

## pop()

This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

```py
cities = {"Pune", "Pimpri", "Mumbai", "Nagpur", "Sangli"}
item = cities.pop()
print(item)
```

## del():

del is not a method, rather it is a keyword which deletes the set entirely.

```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
```

## clear():

This method clears all items in the set and prints an empty set.

```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
```

## Check if item exists

You can also check if an item exists in the set or not.

```py
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
```