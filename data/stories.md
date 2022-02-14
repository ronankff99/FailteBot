<!-- ## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - action_hello_world
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot -->

## Onboarding
* greet
  - action_language_select
* lang_choice{"user_lang":"{user_lang}"}
  - slot{"user_lang":"{user_lang}"}
  - action_utter_main_menu
<!-- Show main menu -->

## Show main menu
* conversation_where_to_get
  - action_utter_your_local_citizens
> where_to_get_choice_1

## Where to get: see nearest centre -> no
> where_to_get_choice_1
* deny
  - action_utter_okay
  - action_utter_main_menu
<!-- Show main menu -->

## Where to get: see nearest centre -> yes
> where_to_get_choice_1
* affirm
  - action_utter_show_local_centre
  - action_utter_main_menu
<!-- Show main menu -->