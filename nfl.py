import csv, json, yaml #pip install pyyaml
#### CSV

# #as lines
# with open('nfl_teams.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(row)

# #as dictionary
# with open('nfl_teams.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         print(row)

# with open('nfl_teams.csv', mode='w') as nfl_file:
#     nfl_writer = csv.writer(nfl_file)
#     nfl_writer.writerow([4,'Giants',6,4])
#     nfl_writer.writerow([5,'Lions',8,2])

# with open('nfl_teams.csv', mode='a') as csv_file:
#     fieldnames = ['id', 'team', 'wins', 'losses']
#     nfl_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     nfl_writer.writerow({'id': 4,'team': 'Giants', 'wins': 6, 'losses': 4})
#     nfl_writer.writerow({'id': 5,'team':'Lions','wins': 8,'losses': 2})

#### json

# writing in json and yaml is different.
# you don't append to them directly
# you convert them to and from dicts
# data = {}
# with open('nfl_teams.json') as json_file:
#     data = json.load(json_file)
# data.append({'id': 4,'team': 'Giants', 'wins': 6, 'losses': 4})
# data.append({'id': 5,'team':'Lions','wins': 8,'losses': 2})
# data = json.dumps(data, indent=4)
# with open('nfl_teams.json', "w") as json_file:
#     json_file.write(data)

#### yaml
# data = {}
# with open('nfl_teams.yaml') as yaml_file:
#     data = yaml.load(yaml_file, Loader=yaml.FullLoader)
#     data.append({'id': 4,'team': 'Giants', 'wins': 6, 'losses': 4})
#     data.append({'id': 5,'team':'Lions','wins': 8,'losses': 2})
# with open('nfl_teams.yaml', "w") as yaml_file:
#     yaml.dump(data, yaml_file)
