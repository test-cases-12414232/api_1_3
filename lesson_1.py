import requests

cities = ["Лондон", "Шереметьево", "Череповец"]
options = {"mnTq":"","lang":"ru"}

for town in cities:
    response = requests.get(url=f"https://wttr.in/{town}", params=options)
    response.raise_for_status()
    print(response.text)
