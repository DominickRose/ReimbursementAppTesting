Feature: Manager can approve or reject reimbursement requests
    Scenario: Manager decides to not approve a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks an approve request button
        Then  A confirm approval pop-up should appear
        When  The manager enters a comment in the comment input
        When  The manager clicks the cancel approval button
        Then  The confirm approval pop-up should close

    Scenario: Manager decides to not reject a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks the deny request button
        Then  A confirm rejection pop-up should appear
        When  The manager enters a comment in the comment input
        When  The manager clicks the cancel rejection button
        Then  The confirm rejection pop-up should close

    Scenario: Manager wants to approve a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks an approve request button
        Then  A confirm approval pop-up should appear
        When  The manager enters a comment in the comment input
        When  The manager clicks the confirm approval button
        Then  The confirm approval pop-up should close

    Scenario: Manager wants to deny a reimbursement request
        Given The manager is on the manager dashboard page
        When  The manager clicks the deny request button
        Then  A confirm rejection pop-up should appear
        When  The manager enters a comment in the comment input
        When  The manager clicks the confirm rejection button
        Then  The confirm rejection pop-up should close

