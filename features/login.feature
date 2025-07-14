Feature: User Login Functionality
  As a registered user
  I want to login to the application
  So that I can access my account and use the features

  # Background: Steps that run before each scenario
  Background:
    Given I am on the login page
    And the login page is loaded successfully

  Scenario: Successfull login with valid credentials
    When I enter username "standard_user"
    And I enter password "secret_sauce"
    And I click the login button
    Then I should be redirected to the Home page
    And I should see Home page logo

  Scenario: Login failure with invalid credentials
    When I enter username "wrong@example.com"
    And I enter password "wrongpassword"
    And I click the login button
    Then I should see error message "Epic sadface: Username and password do not match any user in this service"
    And I should remain on the login page
    And the login form should still be visible

  Scenario Outline: Login with different invalid credentials
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then I should see error message "<error_message>"
    And I should remain on the login page

    # Examples: Data table for Scenario Outline
    Examples:
      | username           | password    | error_message                                                             |
      | ""                 | secret_sauce| Epic sadface: Username is required                                        |
      | standard_user      | ""          | Epic sadface: Password is required                                        |
      | invalid-user       | secret_sauce| Epic sadface: Username and password do not match any user in this service |
      | ""                 | ""          | Epic sadface: Username is required                                        |  