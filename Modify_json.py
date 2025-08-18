import json

# JSON data as a string
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Parse JSON string to a Python dictionary
data = json.loads(json_data)

# Modify data
data['age'] = 31
data['city'] = 'San Francisco'

# Convert back to JSON
updated_json_data = json.dumps(data)

print(updated_json_data)
