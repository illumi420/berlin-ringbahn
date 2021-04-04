
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
print(
    f"                                                             \x1B[3m{bcolors.OKGREEN}S{bcolors.ENDC}41\x1B[23m/\x1B[3m{bcolors.OKGREEN}S{bcolors.ENDC}42\x1B[23m")


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

station = {}
print("<< Ring-Bahn Stations:")
for obj in stations_class_list:
    # Menu
    print(f"{bcolors.OKGREEN}{obj.index+1}.{bcolors.ENDC}{obj.name}",
          end='~+~'*obj.duration),

    station['index'] = obj.index
    station['name'] = obj.name
    station['duration'] = obj.duration
    temp_list.append(
        {'index': station['index'], 'name': station['name'], 'duration': station['duration']})

print()
print()
print("temp_list: ", temp_list)
print("*********************************")
print("station: ", station)
print(temp_list[0])
print(len(temp_list))
