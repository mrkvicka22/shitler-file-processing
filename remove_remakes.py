# import json
# import os
#
# dir = 'C:\\Users\\PC\\PycharmProjects\\shitler\\hope\\7'
# for fstring in os.listdir(dir):
#     with open(f'{dir}\\{fstring}') as f:
#         json_file = json.load(f)

# TODO A custom gam. S custom settings napr. Gun game
# TODO Roztried to podla hracov, tie ktore maju odideneho cloveka
myList = ['120$My life cycle 3$121$My daily routine 2']
myList = myList[0].split('$')
results = []
for i in range(0,len(myList),2):
    results.append(int(myList[i]))
print(results)