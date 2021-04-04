print("RRRRRR  IIIII NN   NN   GGGG         BBBBB     AAA   HH   HH NN   NN ")
print("RR   RR  III  NNN  NN  GG  GG        BB   B   AAAAA  HH   HH NNN  NN")
print("RRRRRR   III  NN N NN GG      _____  BBBBBB  AA   AA HHHHHHH NN N NN")
print("RR  RR   III  NN  NNN GG   GG        BB   BB AAAAAAA HH   HH NN  NNN ")
print("RR   RR IIIII NN   NN  GGGGGG        BBBBBB  AA   AA HH   HH NN   NN ")
print(
    "                                                             \x1B[3mS41\x1B[23m/\x1B[3mS42\x1B[23m")
print("")


km_long = 37, 0


ringbahn_stations = [
    {'name': "Südkreuz", 'duration': 2, 'is_down': False},
    {'name': "Schöneberg", 'duration': 1, 'is_down': False},
    {'name': "Innsbrucker Platz", 'duration': 2, 'is_down': False},
    {'name': "Bundesplatz", 'duration': 2, 'is_down': False},
    {'name': "Heidelberger Platz", 'duration': 2, 'is_down': False},
    {'name': "Hohenzollerndamm", 'duration': 2, 'is_down': False},
    {'name': "Halensee", 'duration': 1, 'is_down': False},
    {'name': "Westkreuz", 'duration': 2, 'is_down': False},
    {'name': "Messe Nord/ICC", 'duration': 2, 'is_down': False},
    {'name': "Westend", 'duration': 3, 'is_down': False},
    {'name': "Jungfernheide", 'duration': 3, 'is_down': False},
    {'name': "Beusselstraße", 'duration': 1, 'is_down': False},
    {'name': "Westhafen", 'duration': 3, 'is_down': False},
    {'name': "Wedding", 'duration': 2, 'is_down': False},
    {'name': "Gesundbrunnen", 'duration': 3, 'is_down': False},
    {'name': "Schönhauser Alle", 'duration': 2, 'is_down': False},
    {'name': "Prenzlauer Alle", 'duration': 2, 'is_down': False},
    {'name': "Greifswalder Straße", 'duration': 2, 'is_down': False},
    {'name': "Landsberger Alle", 'duration': 2, 'is_down': False},
    {'name': "Storkower Straße", 'duration': 2, 'is_down': False},
    {'name': "Frankfurter Alle", 'duration': 2, 'is_down': False},
    {'name': "Ostkreuz", 'duration': 6, 'is_down': False},
    {'name': "Treptower Park", 'duration': 3, 'is_down': False},
    {'name': "Sonnenallee", 'duration': 2, 'is_down': False},
    {'name': "Neukölln", 'duration': 1, 'is_down': False},
    {'name': "Hermannsstraße", 'duration': 4, 'is_down': False},
    {'name': "Tempelhof", 'duration': 2, 'is_down': False},
]


class Stations:
    def __init__(self, index, name, duration, is_down):
        self.index = index
        self.name = name
        self.duration = duration
        self.is_down = is_down


stations_class_list = []
temp_list = []
index_counter = 0
for index in range(1, len(ringbahn_stations)):
    for station in ringbahn_stations:
        if index_counter < len(ringbahn_stations):
            stations_class_list.append(Stations(index_counter,
                                                station['name'], station['duration'], station['is_down']))
            index_counter += index


counter = 0

# for i in range(1, len(stations_class_list)):
#     for obj in stations_class_list:
#         if counter < len(stations_class_list):
#             station['index'] = obj.index
#             station['name'] = obj.name
#             counter += i
#             temp_list.append(i)

# departure_station = input("Departure Station: ")
# destination_station = input("Destination Station: ")

station = {}
for obj in stations_class_list:
    station['index'] = obj.index
    station['name'] = obj.name
    station['duration'] = obj.duration
    temp_list.append(
        {'index': station['index'], 'name': station['name'], 'duration': station['duration']})

#     print(obj.index, obj.name, obj.duration, sep=' ')

print("temp_list: ", temp_list)
print("*********************************")
print("station: ", station)
