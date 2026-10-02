Feature: Login validation

  As a user
  I want invalid login attempts to be rejected
  So that unauthorized access is prevented

  @negative
  Scenario: Reject login with invalid credentials
    When the user enters invalid login credentials
    Then an authentication error message should be displayed