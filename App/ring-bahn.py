import random as r


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


def menu():
    # Logo
    print(f"{' '*58}{bcolors.WARNING}RRRRRR  IIIII NN   NN   GGGG         BBBBB     AAA   HH   HH NN   NN {bcolors.ENDC}")
    print(f"{' '*57}{bcolors.WARNING}RR   RR  III  NNN  NN  GG  GG        BB   B   AAAAA  HH   HH NNN  NN{bcolors.ENDC}")
    print(f"{' '*56}{bcolors.WARNING}RRRRRR   III  NN N NN GG{bcolors.ENDC}      {bcolors.FAIL}_____{bcolors.ENDC}  {bcolors.WARNING}BBBBBB  AA   AA HHHHHHH NN N NN{bcolors.ENDC}")
    print(f"{' '*55}{bcolors.FAIL}RR  RR   III  NN  NNN GG   GG        BB   BB AAAAAAA HH   HH NN  NNN {bcolors.ENDC}")
    print(f"{' '*54}{bcolors.FAIL}RR   RR IIIII NN   NN  GGGGGG        BBBBBB  AA   AA HH   HH NN   NN {bcolors.ENDC}")
    print(f"{' '*54}                                                                  <--")
    print(
        f"{' '*54}                                                             \x1B[3m{bcolors.OKGREEN}S{bcolors.ENDC}41\x1B[23m/\x1B[3m{bcolors.OKGREEN}S{bcolors.ENDC}42\x1B[23m")
    print(f"{' '*54}                                                            -->")
    print()

    # Menu
    print("<< Ring-Bahn Stations:")
    print()
    for obj in stations_class_list:
        print(f"{bcolors.OKGREEN}{obj.index+1}{bcolors.ENDC}.{obj.name}",
              end=' + '*obj.duration)
    print(
        f"Südkreuz")
    print(
        f"\n {bcolors.OKGREEN}b{bcolors.ENDC}.back  {bcolors.OKGREEN}q{bcolors.ENDC}.quit")
    print()


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

for obj in stations_class_list:
    stations['index'] = obj.index
    stations['name'] = obj.name
    stations['duration'] = obj.duration
    # stations['is_down'] = obj.is_down
    # must append to temp_list when station's statue has to be checked
    temp_list.append(
        {'index': stations['index'], 'name': stations['name'], 'duration': stations['duration']})
    # print(stations['name'], stations)


# add last station object to the array
# temp_list.append(
#    {'index': 27, 'name': temp_list[0]['name'], 'duration': temp_list[0]['duration']})
# last_station = temp_list[-1]


selected_stations = []


def input_station():
    start_station = ""
    end_station = ""
    print()
    while start_station != 'q' and end_station != 'q':
        for i in range(2):
            try:
                start_station = input(
                    f">> Enter Departure-station {bcolors.OKGREEN}number{bcolors.ENDC}: ").lower()

                if start_station == 'q':
                    break

                end_station = input(
                    f">> Enter Destination-station {bcolors.OKGREEN}number{bcolors.ENDC}: ").lower()

                if end_station == 'q':
                    break
                    if end_station == 'b':
                        return

                if station_validation(temp_list, start_station, end_station):
                    print(another_list)
                    another_list.pop()
                    # a_list.pop()

                    input("Press Enter to start again")
                    menu()

            except:
                print("invalid input")


another_list = []
minutes_list = []
a_list = []


def station_validation(temp_station_list, start, end):
    start = int(start) - 1
    end = int(end) - 1
    # if start < end:
    #     another_list.append(temp_station_list[int(start):int(end)])
    #     counter = 0
    #     for i in range(len(another_list)):
    #         for j in another_list[0]:
    #             minutes_list.append(another_list[0][counter]['duration'])
    #             counter += 1
    #             minutes = 0
    #             for k in minutes_list:
    #                 minutes += k
    #             train = "S41"
    #         # printing ride-infos
    #         infos(start, end, train, minutes)
    #     del minutes_list[:]
    #     return "S41"

    if end - start >= 10:
        another_list.append(list(reversed(temp_station_list[0:int(start)])))
        counter = 0
        while len(minutes_list) <= len(another_list)+1:
            for i in range(len(another_list)):
                minutes_list.append(another_list[0][counter]['duration'])
                counter += 1
        # another_list[0].insert(0, temp_station_list[int(start)])
        for obj in temp_station_list[-1*(len(temp_station_list)-(end)):]:
            stations['index'] = obj['index']
            stations['name'] = obj['name']
            stations['duration'] = obj['duration']
            # stations['is_down'] = obj['is_down']
            # must append to another_list when station's statue has to be checked
            another_list[0].insert(
                start, {'index': stations['index'], 'name': stations['name'], 'duration': stations['duration']})
            minutes_list.append(stations['duration'])
            minutes = 0
            #     for k in minutes_list:
            #         minutes += k
        # train = "S42"
        # infos(start, end, train, minutes)
        print(minutes_list)
        del minutes_list[:]
        return "S42"


def infos(start, end, train, minutes):
    print()
    print("<< From", temp_list[start]['name'],
          "To", temp_list[end]['name'])
    print("<< Ride the", train, "for", (end-start)//2, "stations")
    print("<< Duration:", minutes, "minutes")
    greetings = ["<< Be aware of unfriendly Ticket-controllers!!!",
                 "<< Enjoy Berlin", "<< Have a nice Day"]
    print(r.choice(greetings))
    print()


# Menu
menu()

input_station()


####debug section#####

# any_station = temp_list[14]


# def debuggingFunc(station_list, a_station, end_station):
#     print()
#     print()
#     print("*"*((32*6)-3))
#     print("for debugging")
#     print("*"*((32*6)-3))
#     print(f"{bcolors.OKGREEN}temp_list:{bcolors.ENDC}", station_list)
#     print("*"*((32*6)-3))
#     print(f"{bcolors.OKGREEN}a station:{bcolors.ENDC}", a_station)
#     print("*"*((32*6)-3))
#     print(f"{bcolors.OKGREEN}last station:{bcolors.ENDC}", end_station)
#     print("*"*((32*6)-3))
#     print(f"{bcolors.OKGREEN}Stations in total:{bcolors.ENDC}", len(station_list))
#     print("*"*((32*6)-3))


# debuggingFunc(temp_list, any_station, last_station)
