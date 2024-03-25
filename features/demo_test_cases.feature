Feature: Facebook login functionality

  @logincase
  @sanity
  Scenario: Test Login with correct login credentials
     Given credentials are given
      When we input correct credentials
      Then login will be successful
      And correct profile opened

  @smoke
  Scenario: Test Login with incorrect login credentials
     Given credentials are given
      When we input correct credentials
      Then login will be successful
      And correct profile opened
