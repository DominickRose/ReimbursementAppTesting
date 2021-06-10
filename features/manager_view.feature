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