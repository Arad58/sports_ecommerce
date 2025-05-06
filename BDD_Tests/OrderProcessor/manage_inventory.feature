Feature: Manage Inventory
  As an Inventory Manager
  I want to create, read, update, and delete inventory records
  So that I can maintain stock levels for the system

  Scenario: Inventory Manager creates a new inventory record
    Given the inventory manager is logged in
    When the inventory manager navigates to the "Create Inventory" page
    And enters valid inventory details
    And submits the form
    Then the new inventory record should be created
    And the inventory should appear in the system

  Scenario: Inventory Manager reads inventory details
    Given the inventory manager is logged in
    When the inventory manager searches for an inventory record
    Then the system should display the inventory details

  Scenario: Inventory Manager updates an existing inventory record
    Given the inventory manager is logged in
    And an inventory record exists in the system
    When the inventory manager navigates to the "Update Inventory" page
    And modifies inventory information
    And submits the changes
    Then the system should update the inventory record

  Scenario: Inventory Manager deletes an inventory record
    Given the inventory manager is logged in
    And an inventory record exists in the system
    When the inventory manager navigates to the "Delete Inventory" option
    And confirms the deletion
    Then the system should remove the inventory record from the database