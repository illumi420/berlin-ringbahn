km_long = 37, 0


station_duration = [
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
index = 0
temp_list = []
another_list = []
user_input = ""


def fromTo(start, end, stations_list):
    counter = 0
    start = input("Departure station: ")
    end = input("Destination station: ")
    for i in range(1, len(stations_list)):
        for j in stations_list:
            if counter < len(stations_list):
                #print(counter, j['name'], j['duration'])
                counter += i
                if (start == j['name']) or (end == j['name']):
                    j['index'] = counter-1
                    temp_list.append(j)
                    print(counter-1, j['name'], j['duration'])


fromTo(user_input, user_input, station_duration)

first = temp_list[0]['index']
second = temp_list[1]['index']
another_list.append(station_duration[first:second+1])
new_list = []
# print(another_list[:]['duration'])
# for q in another_list:
#     new_list.append(q['duration'])
# print(new_list)

# print(station_duration[24]['name'], station_duration[24]['duration'],
#     station_duration[20]['name'], station_duration[20]['duration'])
