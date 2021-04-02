print("RRRRRR  IIIII NN   NN   GGGG         BBBBB     AAA   HH   HH NN   NN ")
print("RR   RR  III  NNN  NN  GG  GG        BB   B   AAAAA  HH   HH NNN  NN")
print("RRRRRR   III  NN N NN GG      _____  BBBBBB  AA   AA HHHHHHH NN N NN")
print("RR  RR   III  NN  NNN GG   GG        BB   BB AAAAAAA HH   HH NN  NNN ")
print("RR   RR IIIII NN   NN  GGGGGG        BBBBBB  AA   AA HH   HH NN   NN ")
print(
    "                                                             \x1B[3mS41\x1B[23m/\x1B[3mS42\x1B[23m")
print("")


km_long = 37, 0

"""
Lists Descreption:

*ringbahn_stations: 
 -is an Array of 26 Objects each object contaiens 3 items:
  ('name':str(station-name),'duration':int(minutes till nex station),'is_down':bool(station status))
 -ringbahn_stations is called in  fromTo() as parameter: stations_list.
 -in  duration() this list is sliced and appended to in_between_stations list.
 *temp_list:
 -is an Array with 2 objects tooken from ringbahn_stations.
 -each object contaiens 4 items:
 ('name':str(station-name),'duration':int(minutes till nex station),'is_down':bool(station status),'index':int(position))
 -in  fromTo() these 2 objects are given by user start/end input and they get an 'index' key and int(value)
 -in  duration() ringbahn_stations is sliced based on temp_list objects index values(end station is excluded), 
  and appended to in_between_stations list.
  *in_between_stations:
  -is an Array with objects sliced from ringbahn_stations based on user start/end input.
  -in_between_stations is called in  duration() as parameter: traveled_stations.
  *minutes_list:
  -is an Array of integers, that are tooken from 'duration' values of objects in in_between_stations array of objects.
  -minutes_list is called in  duration() as parameter: traveled_minutes
"""

ringbahn_stations = [
    {'name': "Südkreuz", 'duration': 2, 'is_down': False},
    {'name': "Schöneberg", 'duration': 1, 'is_down': False},
    {'name': "Innsbrucker Platz", 'duration': 2, 'is_down': False},
    {'name': "Bundesplatz", 'duration': 2, 'is_down': False},
    {'name': "Heidelberger Platz", 'duration': 2, 'is_down': False},
    {'name': "Halensee", 'duration': 2, 'is_down': False},
    {'name': "Westkreuz", 'duration': 1, 'is_down': False},
    {'name': "Messe Nord/ICC", 'duration': 2, 'is_down': False},
    {'name': "Westend", 'duration': 1, 'is_down': False},
    {'name': "Jungfernheide", 'duration': 2, 'is_down': False},
    {'name': "Beusselstraße", 'duration': 3, 'is_down': False},
    {'name': "Westhafen", 'duration': 3, 'is_down': False},
    {'name': "Wedding", 'duration': 2, 'is_down': False},
    {'name': "Gesundbrunnen", 'duration': 3, 'is_down': False},
    {'name': "Schönhauser Alle", 'duration': 2, 'is_down': False},
    {'name': "Prenzlauer Alle", 'duration': 3, 'is_down': False},
    {'name': "Greifswalder Straße", 'duration': 2, 'is_down': False},
    {'name': "Landsberger Alle", 'duration': 2, 'is_down': False},
    {'name': "Storkower Straße", 'duration': 2, 'is_down': False},
    {'name': "Frankfurter Alle", 'duration': 6, 'is_down': False},
    {'name': "Ostkreuz", 'duration': 2, 'is_down': False},
    {'name': "Treptower Park", 'duration': 3, 'is_down': False},
    {'name': "Sonnenallee", 'duration': 2, 'is_down': False},
    {'name': "Neukölln", 'duration': 1, 'is_down': False},
    {'name': "Hermannsstraße", 'duration': 4, 'is_down': False},
    {'name': "Tempelhof", 'duration': 2, 'is_down': False}
]

temp_list = []
in_between_stations = []
user_input = ""

"""
-function fromTo takes user input for start/end station and a list of stations(the list is an Array and stations are Objects).
-first loop is counting the elements, starts from 1, index is always 1,
 in every iteration index is added to index_counter depending on list length.
-second loop is iterating over every object in the array.
-checking if user inputs matches any object value in key 'name'.
-appending new 'index' keys to the matched objects with the value (index_counter-1) to get the real object position in the list.
- appending updated objects to a temporary list outside the function
"""


def fromTo(start_input, end_input, stations_list):
    index_counter = 0
    start_input = input(">> Departure station: ")
    end_input = input(">> Destination station: ")
    for index in range(1, len(stations_list)):
        for station in stations_list:
            if index_counter < len(stations_list):
                #print(index_counter, station['name'], station['duration'])
                index_counter += index
                if (start_input == station['name']) or (end_input == station['name']):
                    # adding index as key:value to start_input/end_input station object
                    station['index'] = index_counter-1
                    # appending updated start_input/end_input object to a temporary list
                    temp_list.append(station)
                    # print("<< ", index_counter-1,
                    #       station['name'], station['duration'])


minutes_list = []

"""
-function duration takes two lists as parameters.
-assigning the 'index' key values of temp_list objects in two diffrent variables.
-the difference between the variables is how many stations are in between.
-slicing ringbahn_stations based on the two variables and appending them to in_between_stations.
-taking 'duration' key value from in_between_stations objects and appending them in minutes_list.
-adding minutes_list elements together and returning the value
"""


def duration(traveled_stations, traveled_minutes):
    start = temp_list[0]['index']
    end = temp_list[1]['index']
    print("<< Stations till destination:", end - start)
    # slicing ringbahn stations list depending on the index values of the objects in temp_list
    traveled_stations.append(ringbahn_stations[start:end])
    # print(*traveled_stations[0])
    counter = 0
    duration_time = 0
    for i in range(0, len(traveled_stations[0])):
        for stations in traveled_stations:
            if counter < len(traveled_stations[0]):
                counter += 1
                duration_time = stations[i]['duration']
                traveled_minutes.append(duration_time)

    # print(traveled_minutes)
    minutes = 0
    for elements in traveled_minutes:
        minutes += elements
    return minutes


fromTo(user_input, user_input, ringbahn_stations)
print("<< Travel time:", duration(in_between_stations, minutes_list), "minutes")

# print(ringbahn_stations[24]['name'], ringbahn_stations[24]['duration'],
#     ringbahn_stations[20]['name'], ringbahn_stations[20]['duration'])
