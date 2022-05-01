# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import csv
from typing import Any, Text, Dict, List
from webbrowser import get

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
                print(e)
                continue

        if not check:
            # If there is no entry in csv file
            res = f"Data retrieval error, could not find key:{key}. Please contact a developer at fakesupport@failtebot.com"

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
            },{
                "title": getText('accommodation', user_lang),
                "payload": '/conversation_accommodation'                
            },{
                "title": getText('education', user_lang),
                "payload": '/conversation_education'                
            },{
                "title": getText('healthcare', user_lang),
                "payload": '/conversation_healthcare'                   
            }, {
                "title": getText('bug', user_lang),
                "payload": '/conversation_bug'
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
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_housing_checklist_1', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_2', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_3', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_4', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_5', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_6', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_7', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_8', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_9', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_10', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_11', user_lang))
        dispatcher.utter_message(text=getText('utter_housing_checklist_12', user_lang))

        return []

# ACTIONS FOR EDUCATION STORIES
## Menu for Education Stories
class ActionUtterInIrelandBy(Action):
    def name(self) -> Text:
        return "action_utter_in_ireland_by"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_in_ireland_by', user_lang), buttons=[{
            "title": getText('early_childhood', user_lang),
            "payload": "/early_childhood"
        },{
            "title": getText('primary_education', user_lang),
            "payload": "/primary_education"
        },{
            "title": getText('second_level', user_lang),
            "payload": "/second_level"
        },{
            "title": getText('third_level', user_lang),
            "payload": "/third_level"
        },{
            "title": getText('further_education', user_lang),
            "payload": "/further_education"
        },{
            "title": getText('main_menu', user_lang),
            "payload": "/main_menu"
        }])
        return []

## Early Education
class ActionUtterEarlyChildhoodEducation(Action):
    def name(self) -> Text:
        return "action_utter_early_childhood_education"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_early_childhood_education', user_lang))
        dispatcher.utter_message(text=getText('utter_the_ecce_programme', user_lang))
        return []

## Primary Education
class ActionUtterChildrenAttendPrimary(Action):
    def name(self) -> Text:
        return "action_utter_children_attend_primary"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_children_attend_primary', user_lang))
        list_string =   getText('denominational_schools', user_lang) + '\n' + getText('multidenominational_schools', user_lang) + '\n' +\
                        getText('nondeonminational_schools', user_lang) + '\n' + getText('irish_speaking_schools', user_lang) + '\n' +\
                        getText('schools_for_children', user_lang) + '\n' + getText('private_primary_schools', user_lang)
        dispatcher.utter_message(text=getText(list_string, user_lang))
        dispatcher.utter_message(text=getText('utter_education_in_state', user_lang))
        dispatcher.utter_message(text=getText('utter_primary_schools_are', user_lang))
        dispatcher.utter_message(text=getText('utter_education_in_state', user_lang))
        dispatcher.utter_message(text=getText('utter_primary_schools', user_lang))
        return []  

## Secondary Education
class ActionUtterChildrenBeginTheir(Action):
    def name(self) -> Text:
        return "action_utter_children_begin_their"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_children_begin_their', user_lang))
        dispatcher.utter_message(text=getText('utter_the_second_level', user_lang))
        dispatcher.utter_message(text=getText('utter_the_earliest_a', user_lang), buttons=[{
            "title": getText('is_there_english', user_lang),
            "payload": "/english_language"
        }])
        return []

class ActionUtterYoungChildrenLearn(Action):
    def name(self) -> Text:
        return "action_utter_young_children_learn"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_young_children_learn', user_lang), buttons=[{
            "title": getText('are_there_special', user_lang),
            "payload": "/special_education"
        }])
        return []  

class ActionUtterYoungChildrenLearn(Action):
    def name(self) -> Text:
        return "action_utter_children_with_special"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_children_with_special', user_lang))
        return []  

## Third Level
class ActionUtterThirdLevelEducation(Action):
    def name(self) -> Text:
        return "action_utter_third_level_education"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_third_level_education', user_lang))
        dispatcher.utter_message(text=getText('utter_access_to_higher', user_lang))
        dispatcher.utter_message(text=getText('utter_the_central_applications', user_lang), buttons=[{
            "title": getText('is_there_financial', user_lang),
            "payload": "/financial_support"
        }])

class ActionUtterFinancialHelpFor(Action):
    def name(self) -> Text:
        return "action_utter_financial_help_for"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_financial_help_for', user_lang))
        dispatcher.utter_message(text=getText('utter_some_students_may', user_lang))
        dispatcher.utter_message(text=getText('utter_this_help_is', user_lang), buttons=[{
            "title": getText('is_there_any', user_lang),
            "payload": "/help_for"
        }])

class ActionUtterYesThereIs(Action):
    def name(self) -> Text:
        return "action_utter_yes_there_is"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_yes_there_is_1', user_lang))
        dispatcher.utter_message(text=getText('utter_yes_there_is_2', user_lang))
        dispatcher.utter_message(text=getText('utter_yes_there_is_3', user_lang))
        dispatcher.utter_message(text=getText('utter_yes_there_is_4', user_lang))
        dispatcher.utter_message(text=getText('utter_yes_there_is_5', user_lang))
        dispatcher.utter_message(text=getText('utter_yes_there_is_6', user_lang))
        dispatcher.utter_message(text=getText('utter_yes_there_is_7', user_lang), buttons=[{
            "title": getText('are_my_education', user_lang),
            "payload": "/are_my"
        }])
        return []  

class ActionUtterItDependsQuality(Action):
    def name(self) -> Text:
        return "action_utter_it_depends_quality"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_it_depends_quality', user_lang))
        return []

## Further and Adult Education
class ActionUtterFurtherEducationIs(Action):
    def name(self) -> Text:
        return "action_utter_further_education_is"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_further_education_is_1', user_lang))
        dispatcher.utter_message(text=getText('utter_further_education_is_2', user_lang))
        dispatcher.utter_message(text=getText('utter_further_education_is_3', user_lang))
        dispatcher.utter_message(text=getText('utter_further_education_is_4', user_lang))
        dispatcher.utter_message(text=getText('utter_further_education_is_5', user_lang))
        dispatcher.utter_message(text=getText('utter_further_education_is_6', user_lang))
        dispatcher.utter_message(text=getText('utter_you_can_get', user_lang))
        dispatcher.utter_message(text=getText('utter_further_information_about', user_lang))
        return []

# ACTIONS FOR EDUCATION STORIES
## Menu for Education Stories
class ActionUtterInIrelandThe(Action):
    def name(self) -> Text:
        return "action_utter_in_ireland_the"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_in_ireland_by', user_lang), buttons=[{
            "title": getText('hse_local', user_lang),
            "payload": "/hse_local"
        },{
            "title": getText('register_gp', user_lang),
            "payload": "/register_gp"
        },{
            "title": getText('public_health', user_lang),
            "payload": "/public_health"
        },{
            "title": getText('medical_emergency', user_lang),
            "payload": "/medical_emergency"
        },{
            "title": getText('other_services', user_lang),
            "payload": "/other_services"
        },{
            "title": getText('main_menu', user_lang),
            "payload": "/main_menu"
        }])
        return []

## HSE Local Health Office
class ActionUtterYourLocalHealth(Action):
    def name(self) -> Text:
        return "action_utter_your_local_health"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('action_utter_your_local_health', user_lang))
        list_string =   getText('gp_services', user_lang) + '\n' + \
                        getText('public_health_nursing', user_lang) + '\n' + \
                        getText('child_health', user_lang) + '\n' + \
                        getText('community_welfare', user_lang) + '\n' + \
                        getText('chiropody', user_lang) + '\n' + \
                        getText('ophthalmic', user_lang) + '\n' + \
                        getText('speech_therapy', user_lang) + '\n' + \
                        getText('social_work', user_lang) + '\n' + \
                        getText('addiction_counselling', user_lang) + '\n' + \
                        getText('physiotherapy', user_lang) + '\n' + \
                        getText('occupational_therapy', user_lang) + '\n' + \
                        getText('psychiatric_services', user_lang)
        dispatcher.utter_message(text=list_string)
        return []

## Register with a GP
class ActionUtterToAccessHealth(Action):
    def name(self) -> Text:
        return "action_utter_to_access_health"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_to_access_health', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_change', user_lang))
        dispatcher.utter_message(text=getText('utter_some_gps_only', user_lang), buttons=[{
            "title": getText('do_i_pay', user_lang),
            "payload": "/do_i_pay"
        }])
        return []

class ActionUtterInIrelandIf(Action):
    def name(self) -> Text:
        return "action_utter_in_ireland_if"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_in_ireland_if', user_lang))
        dispatcher.utter_message(text=getText('utter_if_your_family', user_lang))
        dispatcher.utter_message(text=getText('utter_children_under_the', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_do', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_are', user_lang), buttons=[{
            "title": getText('do_i_have', user_lang),
            "payload": "/do_i_have"
        }])
        return []

class ActionUtterForAcutePublic(Action):
    def name(self) -> Text:
        return "action_utter_for_acute_public"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_for_acute_public', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_do', user_lang))
        dispatcher.utter_message(text=getText('utter_hospital_services', user_lang))
        dispatcher.utter_message(text=getText('utter_you_can_get', user_lang))
        return []

## Public Health Nurses
class ActionUtterPublicHealthNurses(Action):
    def name(self) -> Text:
        return "action_utter_public_health_nurses"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_public_health_nurses', user_lang))
        dispatcher.utter_message(text=getText('utter_if_you_have', user_lang))
        dispatcher.utter_message(text=getText('utter_for_more', user_lang))
        return []

## Medical Emergencies
class ActionUtterInAMedical(Action):
    def name(self) -> Text:
        return "action_utter_in_a_medical"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_in_a_medical', user_lang))
        return []

## Medical Emergencies
class ActionUtterAdditionalInformationOn(Action):
    def name(self) -> Text:
        return "action_utter_additional_information_on"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_additional_information_on', user_lang))
        return []

## Medical Emergencies
class ActionUtterToReportA(Action):
    def name(self) -> Text:
        return "action_utter_to_report_a"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_to_report_a', user_lang), buttons=[{
            "title": getText('main_menu', user_lang),
            "payload": "/main_menu"
        }])
        return []

## CHATBOT INFO ACTIONS
class ActionUtterAChatbotOr(Action):
    def name(self) -> Text:
        return "action_utter_a_chatbot_or"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_lang = tracker.get_slot("user_lang")
        dispatcher.utter_message(text=getText('utter_a_chatbot_or', user_lang))
        dispatcher.utter_message(text=getText('utter_design_to_convincingly', user_lang), buttons=[{
            "title": getText('utter_interesting', user_lang),
            "payload": "/interesting"
        }])
        return []