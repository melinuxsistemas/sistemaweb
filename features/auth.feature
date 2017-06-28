Feature: Authentication

    Scenario Outline: User logs in
      Given a user visits the site
      When I log in as "<user>"
      Then I see "<tittle page>"
      Examples:
        | user             | tittle page|
        | uservalid        | "Sistemaweb - Base Page"|
        |userinvalid       | "Sistemaweb - Login     |
