Feature: Manage Products
  As a Product Manager
  I want to create, read, update, and delete products
  So that I can maintain the product catalog

  Scenario: Product Manager creates a new product
    Given the product manager is logged in
    When the product manager navigates to the "Create Product" page
    And enters valid product details
    And submits the form
    Then the new product should be created
    And the product should appear in the product catalog

  Scenario: Product Manager reads product details
    Given the product manager is logged in
    When the product manager searches for a product
    Then the system should display the product's details

  Scenario: Product Manager updates an existing product
    Given the product manager is logged in
    And a product exists in the system
    When the product manager navigates to the "Update Product" page
    And modifies product information
    And submits the changes
    Then the system should update the product

  Scenario: Product Manager deletes a product
    Given the product manager is logged in
    And a product exists in the system
    When the product manager navigates to the "Delete Product" option
    And confirms the deletion
    Then the system should remove the product from the catalog
