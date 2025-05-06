Feature: Manage Orders
  As an Order Processor
  I want to create, read, update, and delete orders
  So that I can manage the customer orders

  Scenario: Order Processor creates a new order
    Given the order processor is logged in
    When the order processor navigates to the "Create Order" page
    And enters valid order details
    And submits the form
    Then the new order should be created
    And the order should appear in the system

  Scenario: Order Processor reads order details
    Given the order processor is logged in
    When the order processor searches for an order
    Then the system should display the order's details

  Scenario: Order Processor updates an existing order
    Given the order processor is logged in
    And an order exists in the system
    When the order processor navigates to the "Update Order" page
    And modifies order information
    And submits the changes
    Then the system should update the order

  Scenario: Order Processor deletes an order
    Given the order processor is logged in
    And an order exists in the system
    When the order processor navigates to the "Delete Order" option
    And confirms the deletion
    Then the system should remove the order from the database