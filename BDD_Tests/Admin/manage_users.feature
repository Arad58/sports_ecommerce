Feature: Manage Users
  As an Admin
  I want to create, read, update, and delete users
  So that I can manage the system access

  Scenario: Admin creates an user
    Given the admin is logged in
    When the admin navigates to the "Create User" option
    And enters valid user details
    And submits the form
    Then the new user should be created
    And the user should appear in the system

  Scenario: Admin reads an user
    Given the admin is logged in
    When the admin searches for a user
    Then the system should display the user's details

  Scenario: Admin updates an user
    Given the admin is logged in
    And a user exists in the system
    When the admin navigates to the "Update User" option
    And modifies user information
    And saves the changes
    Then the system should update the user

  Scenario: Admin deletes an user
    Given the admin is logged in
    And a user exists in the system
    When the admin navigates to the "Delete User" option
    And confirms the deletion
    Then the system should remove the user from the database
