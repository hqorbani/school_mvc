import json

def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json_file(file_name, data):
    # Serializing json
    json_object = json.dumps(data, indent=4)
    # Writing to sample.json
    with open(file_name, "w") as outfile:
        outfile.write(json_object)
