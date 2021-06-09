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



Feature: Employee can add or delete reimbursement requests

    Scenario: The Employee wants to create a new request
        Given The employee is on the employee dashboard page
        When  The employee clicks the new request button
        Then  The new request dialogue should appear
        When  The employee enters the amount of the request
        When  The employee enters the reason for the request
        When  The employee enters the submit request button
        Then  The new request dialogue should close
        Then  The new request should appear in the table

    Scenario: The employee decides not to submit a new request
        Given The employee is on the employee dashboard page
        When  The employee clicks the new request button
        Then  The new request dialogue should appear
        When  The employee enters the amount of the request
        When  The employee enters the reason for the request
        When  The employee clicks the cancel button
        Then  The new request dialogue should close

    Scenario: The employee wants to delete a request
        Given The employee is on the employee dashboard page
        When  The employee clicks the delete button on a request
        Then  A confirmation pop-up should appear
        When  The employee clicks the confirm delete button
        Then  The confirmation pop-up should close
        Then  The request should no longer be in the table

     Scenario: The employee decides not to delete a request
        Given The employee is on the employee dashboard page
        When  The employee clicks the delete button on a request
        Then  A confirmation pop-up should appear
        When  The employee clicks the cancel delete button
        Then  The confirmation pop-up should close