import json

# JSON data as a string
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Parse JSON string to a Python dictionary
data = json.loads(json_data)

# Accessing elements in the dictionary
print(data['name'])  # Output: John Doe
print(data['age'])
