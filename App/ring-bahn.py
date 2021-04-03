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

*s41_stations: 
 -is an Array of 27 Objects each object contaiens 3 items:
  ('name':str(station-name),'duration':int(minutes till nex station),'is_down':bool(station status))
 -s41_stations is called in  s41() as parameter: stations_list.
 -in  duration() this list is sliced and appended to s41_in_between_stations list.
 *s41_temp_list:
 -is an Array with 2 objects tooken from s41_stations.
 -each object contaiens 4 items:
 ('name':str(station-name),'duration':int(minutes till nex station),'is_down':bool(station status),'index':int(position))
 -in  s41() these 2 objects are given by user start/end input and they get an 'index' key and int(value)
 -in  duration() s41_stations is sliced based on s41_temp_list objects index values(end station is excluded), 
  and appended to s41_in_between_stations list.
  *s41_in_between_stations:
  -is an Array with objects sliced from s41_stations based on user start/end input.
  -s41_in_between_stations is called in  duration() as parameter: traveled_stations.
  *minutes_list:
  -is an Array of integers, that are tooken from 'duration' values of objects in s41_in_between_stations array of objects.
  -minutes_list is called in  duration() as parameter: traveled_minutes
"""

s41_stations = [
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
    {'name': "Südkreuz", 'duration': 2, 'is_down': False}
]

# print("S41:", *s41_stations)
# print()
s42_ringbahn_stations = list(reversed(s41_stations))
# print("S42:", *s42_ringbahn_stations)

s41_temp_list = []
s42_temp_list = []
s41_in_between_stations = []
s42_in_between_stations = []
user_input = ""

"""
-function s41 takes a list of stations(the list is an Array and stations are Objects).
-first loop is counting the elements, starts from 1, index is always 1,
 in every iteration index is added to index_counter depending on list length.
-second loop is iterating over every object in the array.
-checking if user inputs matches any object value in key 'name'.
-appending new 'index' keys to the matched objects with the value (index_counter-1) to get the real object position in the list.
- appending updated objects to a temporary list outside the function
"""

start_input = input(">> Departure station: ")
end_input = input(">> Destination station: ")


def s41(stations_list):
    index_counter = 0
    for index in range(1, len(stations_list)):
        for station in stations_list:
            if index_counter < len(stations_list):
                #print(index_counter, station['name'], station['duration'])
                index_counter += index
                if (start_input == station['name']) or (end_input == station['name']):
                    # adding index as key:value to start_input/end_input station object
                    station['index'] = index_counter-1
                    # appending updated start_input/end_input object to a temporary list
                    s41_temp_list.append(station)
                    # print("<< ", index_counter-1,
                    #       station['name'], station['duration'])


minutes_list = []

"""
-function duration takes two lists as parameters.
-assigning the 'index' key values of s41_temp_list objects in two diffrent variables.
-the difference between the variables is how many stations are in between.
-slicing s41_stations based on the two variables values as slicing indexes and appending them to s41_in_between_stations.
-taking 'duration' key value from s41_in_between_stations objects and appending them in minutes_list.
-adding minutes_list elements together and returning the value
"""


def duration(traveled_stations, traveled_minutes):
    s41_start = s41_temp_list[0]['index']
    s41_end = s41_temp_list[1]['index']
    s41_difference = s41_end - s41_start
    print("<< Stations till destination:", s41_difference)
    # slicing ringbahn stations list depending on the index values of the objects in s41_temp_list
    traveled_stations.append(s41_stations[s41_start:s41_end])
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


s41(s41_stations)
print("<< Travel time:", duration(
    s41_in_between_stations, minutes_list), "minutes")

# print(s41_stations[24]['name'], s41_stations[24]['duration'],
#     s41_stations[20]['name'], s41_stations[20]['duration'])
