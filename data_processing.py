import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))
        
for city in cities:
    city["temperature"] = float(city["temperature"])

# # Print first 5 cities only
# for city in cities[:5]:
#     print(city)

# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = []
# for city in cities:
#     temps.append(float(city['temperature']))
# print(sum(temps)/len(temps))
# print()

# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = [float(city['temperature']) for city in cities]
# print(sum(temps)/len(temps))
# print()

# # Print all cities in Germany

# print("all cities in Germany:")
# for city in cities:
#     if city["country"] == "Germany":
#         print(city["city"])
# print()

# # Print all cities in Spain with a temperature above 12°C

# print("all cities in Spain with a temperature above 12°C:")
# for city in cities:
#     if city["country"] == "Spain" and float(city["temperature"]) > 12:
#         print(city["city"])

# # Count the number of unique countries

# print("Count the number of unique countries: ")
# countries = []
# count = 0
# for city in cities:
#     if city["country"] not in countries:
#         countries.append(city["country"])
#         count += 1
        
# print(count)
    


# # Print the average temperature for all the cities in Germany

# total = 0
# count = 0
# for city in cities:
#     if city["country"] == "Germany":
#         total += float(city["temperature"])
#         count += 1
# print(f"the average temperature for all the cities in Germany is {total / count:.2f}")


# # Print the max temperature for all the cities in Italy

# temp = []
# for city in cities:
#     if city["country"] == "Italy":
#         temp.append(city["temperature"])
# print(f"max temperature for all the cities in Italy is {max(temp)}")

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    temp = []
    for item in dict_list:
        if condition(item):
            temp.append(item)
    return temp

def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    temp = []
    for k in dict_list:
        temp.append(k[aggregation_key])
    return aggregation_function(temp)

students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 85}
]
        
print(aggregate("temperature", sum, cities) / len(cities))

print(filter_items(lambda n: n["country"] == "Germany", cities))
print(filter_items(lambda n: n["country"] == "Spain" and n["temperature"] > 12, cities))

print(len(aggregate("country", set, cities)))

print(aggregate("temperature", sum, filter_items(lambda n: n["country"] == "Germany", cities)) / len(filter_items(lambda n: n["country"] == "Germany", cities)))
print(aggregate("temperature", max, cities))

print(filter_items(lambda n: n["country"] != "Sweden" and n["temperature"] < 10, cities))