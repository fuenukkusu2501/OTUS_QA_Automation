import json

import requests

headers = {"Aut": "Sds"}
query = {'status = availeble'}
response = requests.get(url="https://garwin.ru/")
                        # headers=headers,
                        # params=query)
                        # # json={})

print(response.ok)
print(response.text)
print(response.headers)


def create_pet(id_):
    url = f"/orders/{id_}"
    requests.post("")



# Вывод конкретного значения
# a = json.loads(response.text)
# print(a[0]['id'])

# Просто вывод JSON
# a = response.json()
# print(a)
# к json мы обращаемся всегда подоюным образом
# print(a[0]["id"]) - первый безымяггый обьект(словарь) в списке, а в нем выбираем значение по ключу id