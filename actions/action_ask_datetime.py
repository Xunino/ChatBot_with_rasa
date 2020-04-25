from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime

class Action_Hoi_Gio(Action):

    def name(self) -> Text:
        return "action_hoi_gio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        currentDT = datetime.datetime.now()
        dispatcher.utter_message(text = "Bây giờ là " + currentDT.strftime("%I:%M:%S %p"))

        return []

class Action_Hoi_Ngay(Action):

    def name(self) -> Text:
        return "action_hoi_ngay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        currentDT = datetime.datetime.now()
        dispatcher.utter_message(text = "Hôm nay là " + currentDT.strftime("%a, %b %d, %Y"))

        return []