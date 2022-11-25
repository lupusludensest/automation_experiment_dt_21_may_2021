# Created by rapid at 04/08/2022
Feature: # Go to main page send search ford to field and verify respond is expected

  Scenario: # ebay_shoes_001
    Given Loginpage
    Then In search field type "Shoes"
    And Click on the Search button
    Then Verify that the text "Clothing, Shoes & Accessories" is here
    And Find iFrames here and their quantity


