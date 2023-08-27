import json


with open("data.json", "r") as json_file:
    parsed_json = json.load(json_file)
    print(parsed_json)


person = {
    "name": "mike",
    "age": 29,
    "gender": "male",
    "hobbies": ["a", "b", None, True, False],
}


with open("new-data.json", "w") as json_file:
    serialized_json_string = json.dumps(person)
    json_file.write(serialized_json_string)
