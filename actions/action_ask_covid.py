from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from bs4 import BeautifulSoup
import requests

class action_ask_covid(Action):

    def name(self) -> Text:
        return "action_ask_covid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.get_slot("area").lower()
        temp = []

        def check(text):
            if text == "vn" or text == "việt nam":
                return "https://www.worldometers.info/coronavirus/country/viet-nam/"
            elif text == "tg" or text == "thế giới" or text == "toàn cầu":
                return "https://www.worldometers.info/coronavirus/"
            else:
                pass

        URL = check(text)
        link = requests.get(URL)
        soup = BeautifulSoup(link.content, "html.parser")

        data_1 = soup.find(class_="col-md-8")
        data_2 = data_1.find_all(id="maincounter-wrap")

        for i in data_2:
            a = i.find(class_="maincounter-number").text.strip()
            temp.append(a)

        nhiem = temp[0]
        hoi_phuc = temp[2]
        tu_vong = temp[1]

        dispatcher.utter_message("Số ca nhiễm: {}\nSố ca hồi phục: {}\nSố ca tử vong: {}".format(nhiem, hoi_phuc, tu_vong))

        return []
