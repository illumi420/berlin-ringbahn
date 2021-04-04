
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.WARNING}RRRRRR  IIIII NN   NN   GGGG         BBBBB     AAA   HH   HH NN   NN {bcolors.ENDC}")
print(f"{bcolors.WARNING}RR   RR  III  NNN  NN  GG  GG        BB   B   AAAAA  HH   HH NNN  NN{bcolors.ENDC}")
print(f"{bcolors.WARNING}RRRRRR   III  NN N NN GG{bcolors.ENDC}      {bcolors.FAIL}_____{bcolors.ENDC}  {bcolors.WARNING}BBBBBB  AA   AA HHHHHHH NN N NN{bcolors.ENDC}")
print(f"{bcolors.FAIL}RR  RR   III  NN  NNN GG   GG        BB   BB AAAAAAA HH   HH NN  NNN {bcolors.ENDC}")
print(f"{bcolors.FAIL}RR   RR IIIII NN   NN  GGGGGG        BBBBBB  AA   AA HH   HH NN   NN {bcolors.ENDC}")
print("                                                                  <--")
print(
    f"                                                             \x1B[3m{bcolors.OKGREEN}S{bcolors.ENDC}41\x1B[23m/\x1B[3m{bcolors.OKGREEN}S{bcolors.ENDC}42\x1B[23m")
print("                                                            -->")


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
    {'name': "Schönhauser Allee", 'duration': 2, 'is_down': False},
    {'name': "Prenzlauer Allee", 'duration': 2, 'is_down': False},
    {'name': "Greifswalder Straße", 'duration': 2, 'is_down': False},
    {'name': "Landsberger Allee", 'duration': 2, 'is_down': False},
    {'name': "Storkower Straße", 'duration': 2, 'is_down': False},
    {'name': "Frankfurter Allee", 'duration': 2, 'is_down': False},
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


# func
stations_class_list = []
temp_list = []
index_counter = 0
for index in range(1, len(ringbahn_stations)):
    for station in ringbahn_stations:
        if index_counter < len(ringbahn_stations):
            stations_class_list.append(Stations(index_counter,
                                                station['name'], station['duration'], station['is_down']))
            index_counter += index
# print("list of Stationsinstances: ", stations_class_list)

# func
stations = {}
print("<< Ring-Bahn Stations:")
for obj in stations_class_list:
    # Menu
    print(f"{bcolors.OKGREEN}{obj.index+1}.{bcolors.ENDC}{obj.name}",
          end=' + '*obj.duration)

    stations['index'] = obj.index
    stations['name'] = obj.name
    stations['duration'] = obj.duration
    temp_list.append(
        {'index': stations['index'], 'name': stations['name'], 'duration': stations['duration']})
# add last station object to the array
temp_list.append(
    {'index': 27, 'name': temp_list[0]['name'], 'duration': temp_list[0]['duration']})
print(
    f"{bcolors.OKGREEN}{last_station['index']+1}.{bcolors.ENDC}{last_station['name']}")
#print("stations ", stations)

print()
print()

"""
debug section
"""
any_station = temp_list[14]
last_station = temp_list[-1]


def debuggingFunc(station_list, a_station, end_station):
    print("*"*((32*6)-3))
    print("for debugging")
    print("*"*((32*6)-3))
    print(f"{bcolors.OKGREEN}temp_list:{bcolors.ENDC}", station_list)
    print("*"*((32*6)-3))
    print(f"{bcolors.OKGREEN}a station:{bcolors.ENDC}", a_station)
    print("*"*((32*6)-3))
    print(f"{bcolors.OKGREEN}last station:{bcolors.ENDC}", end_station)
    print("*"*((32*6)-3))
    print(f"{bcolors.OKGREEN}Stations in total:{bcolors.ENDC}", len(station_list))
    print("*"*((32*6)-3))


#debuggingFunc(temp_list, any_station, last_station)
