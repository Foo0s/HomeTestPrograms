"""Получение json-объекта и взаимодействие с ним."""
import requests
from flask import Flask
import random
import json

# response = requests.get("http://127.0.0.1:3000/api/courses/" + str(random.randint(0, 4))) # Запрос на получение данных.
# response = requests.delete("http://127.0.0.1:3000/api/courses/" + str(random.randint(0, 4))) # Удаление значений - запрос на удаление
res = requests.post("http://127.0.0.1:3000/api/courses/5", {"name": "Golang", "price": 1239})     # Запрос - на созд файла, данных.
print(res.json())
