Feature: Manager can filter reimbursements according to status

    Scenario: Manager wants to view all pending requests
        Given The manager is on the manager dashboard page
        When the manager selects pending from the filter drop-down menu
        Then  The table should display only pending requests

    Scenario: Manager wants to view all approved requests
        Given The manager is on the manager dashboard page
        When the manager selects approved from the filter drop-down menu
        Then  The table should display only approved requests   

    Scenario: Manager wants to view all rejected requests
        Given The manager is on the manager dashboard page
        When the manager selects rejected from the filter drop-down menu
        Then  The table should display only rejected requests


Feature: Manager can approve or reject reimbursement requests

    Scenario: Manager wants to approve a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks an approve request button
        Then  A confirmation pop-up should appear
        When  The manager enters a reason in the reason input
        When  The manager clicks the confirm approval button
        Then  The confirmation pop-up should close

    Scenario: Manager decides to not approve a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks an approve request button
        Then  A confirmation pop-up should appear
        When  The manager enters a reason in the reason input
        When  The manager clicks the cancel approval button
        Then  The confirmation pop-up should close

    Scenario: Manager wants to deny a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks the deny request button
        Then  A confirmation pop-up should appear
        When  The manager enters a reason in the reason input
        When  The manager clicks the confirm approval button
        Then  The confirmation pop-up should close

    Scenario: Manager decides to not reject a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks the deny request button
        Then  A confirmation pop-up should appear
        When  The manager enters a reason in the reason input
        When  The manager clicks the cancel approval button
        Then  The confirmation pop-up should close

Feature: Manger can view a statistics page


    Scenario: Manager wants to view the statistics page
        Given The manager is on the manager dashboard page
        When  The manager clicks the view all statistics button
        Then  The page should redirect to the statistics page

    Scenario: Manager wants to return to dashboard
        Given The manager is on the statistics page
        When  The manager clicks the back to dashboard button
        Then  The manager should redirect to the manager dashboard page