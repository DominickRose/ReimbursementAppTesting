Feature: Manger can view a statistics page

    Scenario: Manager wants to view the statistics page
        Given The manager is on the manager dashboard page
        When  The manager clicks the view all statistics button
        Then  The page should redirect to the statistics page

    Scenario: Manager wants to return to dashboard
        Given The manager is on the statistics page
        When  The manager clicks the back to dashboard button
        Then  The manager should redirect to the manager dashboard page