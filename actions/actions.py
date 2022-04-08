# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import csv
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# FUNCTIONALITY ACTIONS
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

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('default_fallback', user_lang))
        return []

# ACTIONS FOR ONBOARDING STORY
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

# ACTIONS FOR MAIN MENU STORY
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

# ACTIONS FOR WHERE TO GET HELP STORIES
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
        dispatcher.utter_message(text=getText('utter_show_local_centre', tracker.get_slot("user_lang")))
        return []

# ACTIONS FOR ACCOMMODATION STORIES
## Menu for Accommodation navigation
class ActionUtterTheFirstChallenge(Action):
    def name(self) -> Text:
        return "action_utter_the_first_challenge"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_the_first_challenge', user_lang), buttons=[{
            "title": getText('social_housing', user_lang),
            "payload": "/social_housing"
        },{
            "title": getText('private_housing', user_lang),
            "payload": "/private_housing"
        },{
            "title": getText('homelessness', user_lang),
            "payload": "/homelessness"
        },{
            "title": getText('help_with_paying', user_lang),
            "payload": "/help_with_paying"
        },{
            "title": getText('housing_checklist', user_lang),
            "payload": "/housing_checklist"
        },{
            "title": getText('main_menu', user_lang),
            "payload": "/main_menu"
        }])
        return []

## Public housing
class ActionUtterInIrelandCity(Action):
    def name(self) -> Text:
        return "action_utter_in_ireland_city"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_in_ireland_city', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_associations_and', user_lang))
        return []

class ActionUtterNotEveryoneHas(Action):
    def name(self) -> Text:
        return "action_utter_not_everyone_has"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_not_everyone_has', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_associations_and_2', user_lang), buttons=[{
            "title": getText('what_points_do', user_lang),
            "payload": "/what_points_do"
        }])
        return []

class ActionUtterGeneralPoints(Action):
    def name(self) -> Text:
        return "action_utter_general_points"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_general_points_1', user_lang))
        dispatcher.utter_message(text=getText('utter_general_points_2', user_lang))
        dispatcher.utter_message(text=getText('utter_general_points_3', user_lang))
        dispatcher.utter_message(text=getText('utter_general_points_4', user_lang))
        dispatcher.utter_message(text=getText('utter_general_points_5', user_lang))
        dispatcher.utter_message(text=getText('utter_general_points_6', user_lang))
        dispatcher.utter_message(text=getText('utter_general_points_7', user_lang))
        dispatcher.utter_message(text=getText('utter_general_points_8', user_lang))

        return []

## Private housing
class ActionUtterIfYouDo(Action):
    def name(self) -> Text:
        return "action_utter_if_you_do"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_if_you_do', user_lang))
        dispatcher.utter_message(text=getText('utter_the_private_residential', user_lang))
        dispatcher.utter_message(text=getText('utter_you_can_also', user_lang))
        return []

class ActionUtterTheCostOf(Action):
    def name(self) -> Text:
        return "action_utter_the_cost_of"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_the_cost_of', user_lang))
        dispatcher.utter_message(text=getText('utter_you_will_usually', user_lang))
        dispatcher.utter_message(text=getText('utter_both_threshold_and', user_lang), buttons=[{
            "title": getText('what_documents_might', user_lang),
            "payload": "/what_documents_might"
        }])
        return []

class ActionUtterTheLandlordMay(Action):
    def name(self) -> Text:
        return "action_utter_the_landlord_may"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_the_landlord_may_1', user_lang))
        dispatcher.utter_message(text=getText('utter_the_landlord_may_2', user_lang))
        dispatcher.utter_message(text=getText('utter_the_landlord_may_3', user_lang))
        dispatcher.utter_message(text=getText('utter_the_landlord_may_4', user_lang))
        return []

## Homelessness
class ActionUtterIfYouOr(Action):
    def name(self) -> Text:
        return "action_utter_if_you_or"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_if_you_or_1', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_or_2', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_or_3', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_or_4', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_or_5', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_or_6', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_or_7', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_or_8', user_lang))

        return []

class ActionUtterThereAreTwo(Action):
    def name(self) -> Text:
        return "action_utter_there_are_two"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_there_are_two_1', user_lang))
        dispatcher.utter_message(text=getText('utter_there_are_two_2', user_lang))
        dispatcher.utter_message(text=getText('utter_there_are_two_3', user_lang), buttons=[{
            "title": getText('housing_assistance_payment', user_lang),
            "payload": "/housing_assistance_payment"
        },{
            "title": getText('rent_supplement', user_lang),
            "payload": "/rent_supplement"
        }])
        return []

class ActionUtterHapIsA(Action):
    def name(self) -> Text:
        return "action_utter_hap_is_a"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_hap_is_a', user_lang))
        dispatcher.utter_message(text=getText('utter_hap_will_mean', user_lang))
        dispatcher.utter_message(text=getText('utter_under_hap_you', user_lang))
        dispatcher.utter_message(text=getText('utter_you_must_pay', user_lang))
        return []

class ActionUtterIfYouLive(Action):
    def name(self) -> Text:
        return "action_utter_if_you_live"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_if_you_live', user_lang))
        dispatcher.utter_message(text=getText('utter_rent_supplement_is_1', user_lang))
        dispatcher.utter_message(text=getText('utter_rent_supplement_is_2', user_lang))
        dispatcher.utter_message(text=getText('utter_rent_supplement_is_3', user_lang))
        dispatcher.utter_message(text=getText('utter_rent_supplement_is_4', user_lang))
        dispatcher.utter_message(text=getText('utter_you_can_find', user_lang))
        return []

class ActionUtterHousingChecklist(Action):
    def name(self) -> Text:
        return "action_utter_housing_checklist"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=getText('', 'en'))
        return []