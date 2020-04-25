from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from bs4 import BeautifulSoup
import requests

dir = {
    ###################
    #     Miền bắc
    ###################
    "hà nội": "ha-noi",
    "bắc ninh": "bac-ninh",
    "bắc giang": "bac-giang",
    "điện biên": "dien-bien",
    "hải dương": "hai-duong",
    "hòa bình": "hoa-binh",
    "lai châu": "lai-chau",
    "quảng ninh": "quang-ninh",
    "nam định": "nam-dinh",
    "phú thọ": "phu-tho",
    "thái bình": "thai-binh",
    "thanh hóa": "thanh-hoa",
    "vĩnh phúc": "vinh-phuc",
    "hải phòng": "hai-phong",
    "bắc Kạn": "bac-kan",
    "cao bằng": "cao-bang",
    "hà giang": "ha-giang",
    "hà nam": "ha-nam",
    "hưng yên": "hung-yen",
    "lạng sơn": "lang-son",
    "lào cai": "lao-cai",
    "ninh bình": "ninh-binh",
    "sơn la": "son-la",
    "thái nguyên": "thai-nguyen",
    "tuyên quang": "tuyen-quang",
    "yên bái": "yen-bai",

    ######################
    #      Miền trung
    ######################
    "đà nẵng": "da-nang",
    "nghệ an": "nghe-an",
    "phú yên": "phu-yen",
    "bình định": "binh-dinh",
    "dắk nông": "dak-nong",
    "kon tum": "kon-tum",
    "ninh thuận": "ninh-thuan",
    "quảng ngãi": "quang-ngai",
    "thừa thiên huế": "thua-thien-hue",
    "khánh hòa": "khanh-hoa",
    "hà tĩnh": "ha-tinh",
    "quảng bình": "quang-binh",
    "đắk lắk": "dak-lak",
    "gia lai": "gia-lai",
    "lâm đồng": "lam-dong",
    "quảng nam": "quang-nam",
    "quảng trị": "quang-tri",
    "bình thuận": "binh-thuan",

    ######################
    #       Miền nam
    ######################
    "hồ chí minh": "ho-chi-minh",
    "sóc trăng": "soc-trang",
    "bạc liêu": "bac-lieu",
    "bến tre": "ben-tre",
    "bình phước": "binh-phuoc",
    "đồng nai": "dong-nai",
    "hậu giang": "hau-giang",
    "long an": "long-an",
    "tiền giang": "tien-giang",
    "vĩnh long": "vinh-long",
    "cần thơ": "can-tho",
    "an giang": "an-giang",
    "bà rịa vũng tàu": "ba-ria-vung-tau",
    "bình dương": "binh-duong",
    "cà mau": "ca-mau",
    "đồng tháp": "dong-thap",
    "kiên giang": "kien-giang",
    "tây ninh": "tay-ninh",
    "trà vinh": "tra-vinh"
}

#####################################################

class action_ask_weather(Action):

    def name(self) -> Text:
        return "action_ask_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        local = tracker.get_slot("local")

        def City_zone(city):
            for key, item in dir.items():
                if key == city:
                    return item

        ################################
        city = local.lower()
        temp = City_zone(city)
        link = "https://thoitietvietnam.locvy.com/thoi-tiet-{}-viet-nam".format(temp)
        URL = requests.get(link)
        soup = BeautifulSoup(URL.content, "html.parser")

        #################################
        data_1 = soup.find(class_="navbar navbar-fixed-top navbar-inverse")
        data_2 = data_1.find(class_="container")
        data_3 = data_2.find_next(class_="container")
        row = data_3.find_next(class_="row")
        #################################

        name_city = data_3.find_next(class_="text-center").text
        temperature = row.find_next(class_="hientai").text

        dispatcher.utter_message("{} {}".format(name_city, temperature))
        return []







