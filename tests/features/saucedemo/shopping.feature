Feature: Shopping

  Scenario: Verify thank you message when checkout
    Given The saucedemo login_page is displayed
    When I login as a standard user
    When I shop an item from products_page
    And I click the checkout button from cart_page
    And I fill the user information in checkout_page
    And I click the finish button from checkout_overview_page
    Then I validate thank you message from complete_page
