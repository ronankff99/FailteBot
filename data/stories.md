<!-- ONBOARDING STORIES -->
## Onboarding
* choose_lang
  - action_language_select
* lang_choice{"user_lang":"{user_lang}"}
  - slot{"user_lang":"{user_lang}"}
  - action_utter_main_menu
<!-- Show main menu -->

* greet
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
## Accommodation Menu
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

<!-- EDUCATION STORIES -->
## Education Menu
* conversation_education
  - action_utter_in_ireland_by
> education_choice_1

## Education: Early childhood Education
> education_choice_1
* early_childhood
  - action_utter_early_childhood_education
  - action_utter_in_ireland_by
<!-- Show education menu -->

## Education: Primary Education
> education_choice_1
* primary_education
  - action_utter_children_attend_primary
  - action_utter_in_ireland_by
<!-- Show education menu -->

## Education: Second-level Education
> education_choice_1
* second_level
  - action_utter_children_begin_their
* english_language
  - action_utter_young_children_learn
* special_educational
  - action_utter_children_with_special_educational
  - action_utter_in_ireland_by
<!-- Show education menu -->

## Education: Third-level Education
> education_choice_1
* third_level
  - action_utter_third_level_education
* financial_support
  - action_utter_financial_help_for
* help_for
  - action_utter_yes_there_is
* are_my
  - action_utter_it_depends_quality
  - action_utter_in_ireland_by
<!-- Show education menu -->

## Education: Further Education and Adult Education
> education_choice_1
* further_education
  - action_utter_further_education_is
  - action_utter_in_ireland_by
<!-- Show education menu -->

## Education: Main Menu
> education_choice_1
* main_menu
  - action_utter_main_menu
<!-- Show main menu -->

<!-- HEALTHCARE STORIES -->
## Healthcare Menu
* conversation_healthcare
  - action_utter_in_ireland_the
> healthcare_choice_1

## Healthcare: HSE Local Health Offices
> healthcare_choice_1
* hse_local
  - action_utter_your_local_health
  - action_utter_in_ireland_the
<!-- Show healthcare menu -->

## Healthcare: GPs
> healthcare_choice_1
* register_gp
  - action_utter_to_access_health
* do_i_pay
  - action_utter_in_ireland_if
* do_i_have
  - action_utter_for_acute_public
  - action_utter_in_ireland_the
<!-- Show healthcare menu -->

## Healthcare: Public Health Nurse
> healthcare_choice_1
* public_health
  - action_utter_public_health_nurses
  - action_utter_in_ireland_the
<!-- Show healthcare menu -->

## Healthcare: Medical Emergencies
> healthcare_choice_1
* medical_emergency
  - action_utter_in_a_medical
  - action_utter_in_ireland_the
<!-- Show healthcare menu -->

## Healthcare: Other Services
> healthcare_choice_1
* other_services
  - action_utter_additional_information_on
  - action_utter_in_ireland_the
<!-- Show healthcare menu -->

## Healthcare: Main Menu
> healthcare_choice_1
* main_menu
  - action_utter_main_menu
<!-- Show main menu -->