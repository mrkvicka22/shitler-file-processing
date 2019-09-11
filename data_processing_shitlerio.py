import json
import re
with open('big_data.json', 'r', encoding='utf-8') as f:
    content = f.read()
    content = re.sub(r'\u0000*?gameSummaries.*?[^{]+',r'@@@',content)
    all_files = re.split(r'@@@', content[3:-3])
    for i, json_part in enumerate(all_files):
        with open(f'C:\\Users\\Matej\\PycharmProjects\\discordBot\\hope\\game_file{i}.json', 'w') as json_file:
            json.dump(json.loads(json_part), json_file)
