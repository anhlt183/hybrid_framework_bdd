Feature: User sort product list on Home page Functionality
  As a logged in user
  I want to sort the product list on Home page
  So that my product list can be sorted in a certain order

  # Background: Steps that run before each scenario
  Background:
    Given I already logged in with username is "standard_user" and password is "secret_sauce"
    And I should be redirected to the Home page
    And the product sort container should be visible

  Scenario: Successfull sorting the product list with Name (Z to A)
    When I click on the "Name (Z to A)" option
    Then the product list should be sorted with Name (Z to A) successfully

  Scenario: Successfull sorting the product list with Name (A to Z)
    When I click on the "Name (A to Z)" option
    Then the product list should be sorted with Name (A to Z) successfully 

  Scenario: Successfull sorting the product list with Price (low to high)
    When I click on the "Price (low to high)" option
    Then the product list should be sorted with Price (low to high) successfully 

  Scenario: Successfull sorting the product list with Price (high to low)
    When I click on the "Price (high to low)" option
    Then the product list should be sorted with Price (high to low) successfully