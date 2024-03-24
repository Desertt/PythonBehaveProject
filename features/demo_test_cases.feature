Feature: Facebook login functionality

  Scenario: Test Login with correct login credentials
     Given credentials are given
      When we input correct credentials
      Then login will be successful
      And correct profile opened

  Scenario: Test Login with incorrect login credentials
     Given credentials are given
      When we input correct credentials
      Then login will be successful
      And correct profile opened

  Scenario: Test Login with will be delete login credentials
     Given credentials are given
      When we input correct credentials
      Then login will be successful
      And correct profile opened