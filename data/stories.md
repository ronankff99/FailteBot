<!-- ONBOARDING STORIES -->
## Onboarding
* greet
* choose_lang
  - action_language_select
* lang_choice{"user_lang":"{user_lang}"}
  - slot{"user_lang":"{user_lang}"}
  - action_utter_main_menu
<!-- Show main menu -->

## Where to get help
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

<!-- ACCOMMODATION STORIES -->
## Accommodation
* conversation_accommodation
  - action_utter_the_first_challenge
> accommodation_choice_1

## Accommodation: Social Housing
> accommodation_choice_1
* social_housing
  - action_utter_in_ireland_city
* do_i_have
  - action_utter_not_everyone_has
* what_points_do
  - action_utter_general_points
  - action_utter_the_first_challenge
<!-- Show accommodation menu -->

## Accommodation: Private Housing
> accommodation_choice_1
* private_housing
  - action_utter_if_you_do
* how_much_will
  - action_utter_the_cost_of
* what_documents_might
  - action_utter_the_landlord_may
  - action_utter_the_first_challenge
<!-- Show accommodation menu -->

## Accommodation: Homelessness
> accommodation_choice_1
* homelessness
  - action_utter_if_you_or
  - action_utter_the_first_challenge
<!-- Show accommodation menu -->

## Accommodation: Help with paying your rent
> accommodation_choice_1
* help_with_paying
  - action_utter_there_are_two
> accommodation_choice_2

## Accommodation: Help with paying your rent -> HAP
> accommodation_choice_2
* housing_assistance_payment
  - action_utter_hap_is_a
  - action_utter_the_first_challenge
<!-- Show accommodation menu -->

## Accommodation: Help with paying your rent -> Rent supplement
> accommodation_choice_2
* rent_supplement
  - action_utter_if_you_live
  - action_utter_the_first_challenge
<!-- Show accommodation menu -->

## Accomodation: Housing checklist
> accommodation_choice_1
* housing_checklist
  - action_utter_housing_checklist
  - action_utter_the_first_challenge
<!-- Show accommodation menu -->

## Accommodation: Main Menu
> accommodation_choice_1
* main_menu
  - action_utter_main_menu
<!-- Show main menu -->