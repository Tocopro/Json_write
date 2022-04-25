
import json
sample_jason = {"id": 1, "name": "value2", "age": 28}

print("Started writing JSON data into a file")
with open("sampleJ_son.json", "w") as write_file:
    json.dump(sample_jason, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")
