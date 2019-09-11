import json
import os
import shutil

dir = 'C:\\Users\\Matej\\PycharmProjects\\discordBot\\hope'
for fstring in os.listdir(dir):
    if fstring.startswith('g'):
        with open(f'{dir}\\{fstring}') as f:
            json_file = json.load(f)
            try:
                os.mkdir(f'{dir}\\{len(json_file["players"])}')
            except FileExistsError:
                pass
        shutil.move(f'{dir}\\{fstring}', f'{dir}\\{len(json_file["players"])}\\{fstring}')
        print('managed to move that shit')
