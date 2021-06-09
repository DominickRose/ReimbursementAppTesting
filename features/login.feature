Feature: Ability to log in to view page

    Scenario: Employee wants to log in
        Given The employee or manager is on the login page
        When  The employee enters their correct username
        When  The employee enters their correct password
        When  The employee or manager clicks the login button
        Then  The page should redirect to the employee dashboard

    Scenario: Manager wants to log in
        Given The employee or manager is on the login page
        When  The manager enters their correct username
        When  The manager enters their correct password
        When  The employee or manager clicks the login button
        Then  The page should redirect to the manager dashboard

    Scenario: A manager or employee enters invalid credentials
        Given The employee or manager is on the login page
        When  The employee enters their correct username
        When  The employee enters an incorrect password
        When  The employee or manager clicks the login button
        Then  The password input should be cleared
        Then  An error message should appear