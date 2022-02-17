# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import csv
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def getText(key, lang):
    # Define the flag to indicate if the text was found in the csv
    check = False

    # Default is English
    if not lang:
        print("USER LANGUAGE LOST, SETTING TO DEFAULT")
        lang = "en"

    with open(f'actions/dialogue_{lang}.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, escapechar='\\')
        for row in csv_reader:
            try:
                if row[0] == key:
                    res = row[1].replace('\\n', '\n')
                    check = True
                    break
            except IndexError as e:
                # print(e)
                continue

        if not check:
            # If there is no entry in csv file
            res = f"Data retrieval error, could not find {key} please contact a developer"

    return res

# Actions for fallback option
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('default_fallback', user_lang))
        return []

# Actions for onboarding conversation
class ActionLanguageSelect(Action):
    def name(self) -> Text:
        return "action_language_select"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text=getText('utter_which_language_would', 'en'), 
            buttons=[
                {
                    "title": getText('utter_lets_use', 'en'),
                    "payload": '/lang_choice{"user_lang":"en"}'
                }, 
                {
                    "title": getText('utter_lets_use', 'fr'),
                    "payload": '/lang_choice{"user_lang":"fr"}'
                }, 
                {
                    "title": getText('utter_lets_use', 'ar'),
                    "payload": '/lang_choice{"user_lang":"ar"}'
                }
            ]
        )
        return []

# Actions for main menu
class ActionUtterMainMenu(Action):
    def name(self) -> Text:
        return "action_utter_main_menu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_main_menu', user_lang), buttons=[
            {
                "title": getText('utter_where_to_get', user_lang),
                "payload": '/conversation_where_to_get'            
            }])
        return []

# Actions for Where to get help
class ActionUtterYourLocalCitizens(Action):
    def name(self) -> Text:
        return "action_utter_your_local_citizens"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_lang = tracker.get_slot("user_lang")

        dispatcher.utter_message(text=getText('utter_your_local_citizens_1', user_lang))
        dispatcher.utter_message(text=getText('utter_your_local_citizens_2', user_lang))
        dispatcher.utter_message(text=getText('utter_your_local_citizens_3', user_lang))
        dispatcher.utter_message(text=getText('utter_your_local_citizens_4', user_lang))
        dispatcher.utter_message(text=getText('utter_your_local_citizens_5', user_lang), buttons=[{
            "title": getText('utter_affirm', user_lang),
            "payload": "/affirm"
        },{
            "title": getText('utter_deny', user_lang),
            "payload": "/deny"
        }])

        return []

class ActionUtterOkay(Action):
    def name(self) -> Text:
        return "action_utter_okay"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=getText('utter_okay', tracker.get_slot("user_lang")))
        return []

class ActionUtterShowLocalCentre(Action):
    def name(self) -> Text:
        return "action_utter_show_local_centre"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=getText('utter_show_local_centre', 'en'))
        return []

