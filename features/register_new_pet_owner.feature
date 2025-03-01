Feature: Register New Pet Owner

  Scenario: Verify that new owner with valid data is added
    Given I am on the pet clinic home page
    When I navigate to the Find Owners page
    And I navigate to the Add Owner page
    And I enter owner valid data
    Then I see the owner is registered successfully
