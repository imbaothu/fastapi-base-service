import json
import orjson
import time

# Create a large list of dictionaries
data = [{"key": "value"} for _ in range(10000)]

# use json
start_time = time.time()
json_data = json.dumps(data)
data = json.loads(json_data)
end_time = time.time()
print(f"json.dumps: {end_time - start_time} seconds")

# use orjson
start_time = time.time()
orjson_data = orjson.dumps(data)
data = json.loads(orjson_data)
end_time = time.time()
print(f"orjson.dumps: {end_time - start_time} seconds")


# results 
# json.dumps: 0.010320186614990234 seconds
# orjson.dumps: 0.003702878952026367 seconds