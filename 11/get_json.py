# показать как работать с json
# скачать json стандартным модулем

# https://academy.yandex.ru/handbook/python/article/potokovyj-vvodvyvod-rabota-s-tekstovymi-fajlami-json

# Import JSON module
import json
 
# Define JSON string
json_string = '{ "id": 121, "name": "Maxim", "course": ["Math", "C"]}'
 
# Convert JSON String to Python
student = json.loads(json_string)
 
# Print Dictionary
print(student)
 
# Print values using keys
print(student['name'])
print(student['course'])


# скачать json с помощью requests
