m_long = 37, 0
#read about django modules
# break station_duration to array of objects
station_duration = {
    "Südkreuz": 2,
    "Schöneberg": 1,
    "Innsbrucker Platz": 2,
    "Bundesplatz": 2,
    "Heidelberger Platz": 2,
    "Halensee": 2,
    "Westkreuz": 1,
    "Messe Nord/ICC": 2,
    "Westend": 1,
    "Jungfernheide": 2,
    "Beusselstraße": 3,
    "Westhafen": 3,
    "Wedding": 2,
    "Gesundbrunnen": 3,
    "Schönhauser Alle": 2,
    "Prenzlauer Alle": 3,
    "Greifswalder Straße": 2,
    "Landsberger Alle": 2,
    "Storkower Straße": 2,
    "Frankfurter Alle": 6,
    "Ostkreuz": 2,
    "Treptower Park": 3,
    "Sonnenallee": 2,
    "Neukölln": 1,
    "Hermannsstraße": 4,
    "Tempelhof": 2,
    "Südkreuz": 0
}
index = 0
temp_list = []
counter = 1

user_input = ""


def fromTo(start, end, a_dictionary):
    start = input("Enter start station: ")
    end = input("Enter end station: ")
    for j in range(len(a_dictionary)):
        for key, value in a_dictionary.items():
            # if any(start and end in value for value in a_dictionary.items()):
            if key == start:
                print(key, value)
                print(j)

            elif key == end:
                print(key, value)
                print(j)


fromTo(user_input, user_input, station_duration)

# for i in stations:
#     print(i)
#     station_duration[i] = 0
#     for j in minuets_till_next_station:
#         station_duration[i] = j

# for j in minuets_till_next_station:
#     print(j)

# print(station_duration)
# print(sum(minuets_till_next_station))

# r_41 = print("r41:", stations)
# print()
# stations.reverse()
# r_42 = print("r42:", stations)
