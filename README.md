[🇬🇧 English](README.md) | [🇹🇷 Türkçe](README.tr.md)

# Python Behave Selenium Automation

A small hands-on UI test automation project demonstrating
**Python, Behave (BDD), Selenium WebDriver, and negative login validation**.

The project was refactored from an older local automation example into a portable,
reproducible test project with isolated dependencies and executable BDD scenarios.

## Tech Stack

- Python
- Behave
- Selenium WebDriver
- Gherkin / BDD
- Chrome
- Python virtual environment

## Current Scenario

### Negative Login Validation

The current scenario verifies that invalid credentials are rejected by the target application.

```gherkin
Scenario: Reject login with invalid credentials
  When the user enters invalid login credentials
  Then an authentication error message should be displayed