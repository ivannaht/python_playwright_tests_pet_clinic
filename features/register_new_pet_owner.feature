Feature: Register New Pet Owner
  Scenario: Verify that new owner with valid data is added
    Given I am on the pet clinic home page
    When I am creating the owner with valid data
    Then I see the owner is registered successfully
    