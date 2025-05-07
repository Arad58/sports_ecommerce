Feature: Place Orders
  As a Customer
  I want to add items to my cart and complete an order
  So that I can purchase products

  Scenario: Customer adds items to cart
    Given the customer is logged in
    When the customer selects a product
    And adds the product to the cart
    Then the product should appear in the customer's cart

  Scenario: Customer proceeds to checkout
    Given the customer has items in the cart
    When the customer clicks "Proceed to Checkout"
    Then the system should navigate to the checkout page

  Scenario: Customer enters user details
    Given the customer is on the checkout page
    When the customer enters their user details
    Then the system should store the customer details

  Scenario: Customer confirms order
    Given the customer has entered their details
    When the customer clicks "Confirm Order"
    Then the order should be placed now

  Scenario: Customer receives order confirmation
    Given the order has been placed
    When the system processes the order
    Then the customer should receive an confirmation message