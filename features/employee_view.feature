Feature: Employee can view requests based on status

    Scenario: The Employee wants to view all pending requests
        Given The employee is on the employee dashboard page
        When  The employee selects pending from the filter drop-down menu
        Then  The table should display only pending requests

    Scenario: The Employee wants to view all approved requests
        Given The employee is on the employee dashboard page
        When  The employee selects approved from the filter drop-down menu
        Then  The table should display only approved requests

    Scenario: The Employee wants to view all rejected requests
        Given The employee is on the employee dashboard page
        When  The employee selects rejected from the filter drop-down menu
        Then  The table should display only rejected requests