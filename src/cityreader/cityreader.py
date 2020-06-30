import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"<City: {{ name: {self.name}, lat: {self.lat}, lon: {self.lon} }}>"


cities = []


def cityreader(cities=[]):
    with open("cities.csv", newline='') as cities_file:
        reader = list(csv.reader(cities_file))
        for city in reader[1:]:
            cities.append(City(city[0], float(city[3]), float(city[4])))

    return cities


cityreader(cities)

for c in cities:
    print(c)


def normalize_floats(val1, val2):
    val1, val2 = [float(val1), float(val2)]
    return [val for val in ([val1, val2] if val1 < val2 else [val2, val1])]


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    low_lat, high_lat = normalize_floats(lat1, lat2)
    low_lon, high_lon = normalize_floats(lon1, lon2)
    within = [city for city in cities if (city.lat >= low_lat and city.lat <= high_lat) and (
        city.lon >= low_lon and city.lon <= high_lon)]
    return within


lat1, lon1 = input(
    'Enter a latitude value and a longitude value, separated by a comma: ').split(',')
lat2, lon2 = input(
    'Now enter two more values, just like above: ').split(',')
bound_cities = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
for city in bound_cities:
    print(city)
