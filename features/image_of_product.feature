Feature: Product image validation on inventory page
  As a logged in user
  I want to validate for product image on inventory page

  # Background: Steps that run before each scenario
  Background:
    Given I already logged in with username is "standard_user" and password is "secret_sauce"

  Scenario: Verify all product images are displayed
    When I open inventory page
    Then all product images should be visible

  Scenario: Verify image src and alt attributes are not empty
    When I open inventory page
    Then all product images should have valid src and alt attributes

  Scenario: Verify product image navigation
      When I open inventory page
      And I click on the image of "Sauce Labs Backpack"
      Then I should be redirected to the product detail page for "Sauce Labs Backpack"  