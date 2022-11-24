import json as js

with open('file.json') as f:
    data = js.load(f)

print('{ "zscaler.net": {')  # starting curly braces open  #1 open

count_continent = 0
for continentx in data['zscaler.net']:
    if count_continent > 0:
        print(',')

    print('"' + continentx + '": ' + '{')  # 2 open
    count_continent += 1

    count_city = 0
    for cityx in data['zscaler.net'][continentx]:

        if count_city > 0:
            print(',')

        print('"' + cityx + '": [')  # 3 open # ignore this for empty objects
        count_city += 1

        count = 0
        for obj_in_City in data['zscaler.net'][continentx][cityx]:

            if obj_in_City.get('vpn') != '' and obj_in_City.get('gre') != '':
                if count > 0:
                    print(',')

                print(obj_in_City)  # , end = ''
                count += 1

        print(' ]', end='')  # 3 closed

    print('}')  # 2 closed

print('}}')  # 1 closed anf # starting curly braces closed
