import  requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json
import subprocess
#subprocess.call('cmd /c "rasa run --enable-api -m models\nlu-20211201-003949-grating-muffler.tar.gz"')
user_input = input (" Ask Santa >>")

url = "http://localhost:5005/model/parse"
data = {"text": user_input}
data = json.dumps(data, ensure_ascii=False)
data = data.encode(encoding="utf-8")  # If text with Chinese needs to be transcoded
r = requests.post(url=url, data=data)
print(json.loads(r.text))

# current = requests.post('http://localhost:5000/parse?q=hello').json()
# print(current)
# country = current['sys']['country']

# import requests as req
# def rasa_output(text):
#     message = str(text).strip()
#     result =rasa.nlu.model.parse(message)
#     return result
#
# def main():
#     user_input = input (" Ask Santa >>")
#     while not (user_input.lower() in ("exit","quit","q")):
#         out= rasa_output(user_input)
#         print(out)
#
#         user_input=input(">> ")
# main()


