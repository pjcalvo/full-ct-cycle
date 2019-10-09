Feature: This feature file will test all related to the money API of the application

  Background:
    Given As a user of the application

  Scenario: Request with valid integer value
    Given a "2200" as a test value
    When  I execute the request to format the money
    Then  the api will response "201" code
    Then  the expected value should be "2 200.00" 

    