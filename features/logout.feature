Feature: User Logout Functionality
  As a logged in user
  I want to logout from the application
  So that my session is securely closed

  # Background: Steps that run before each scenario
  Background:
    Given I already logged in with username is "standard_user" and password is "secret_sauce"
    And I should be redirected to the Home page

  Scenario: Successfull logout from the application
    When I click the logout button
    Then I should be redirected to the Login page
    And Verify that user should be in the Login page
    And the login form should still be visible