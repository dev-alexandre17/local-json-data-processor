import json

def read_json_file():
    with open('data/pokemonDB_dataset.json') as f:
        return json.load(f)

print(read_json_file())