[🇬🇧 English](README.md) | [🇹🇷 Türkçe](README.tr.md)

# Python Behave Selenium Automation

**Python, Behave (BDD), Selenium WebDriver ve negative login validation** odaklı küçük bir hands-on UI test automation projesi.

Bu proje eski bir local automation örneğinden alınarak daha taşınabilir,
tekrarlanabilir ve recruiter-friendly bir test projesine dönüştürülmüştür.

## Tech Stack

- Python
- Behave
- Selenium WebDriver
- Gherkin / BDD
- Chrome
- Python virtual environment

## Mevcut Senaryo

### Negative Login Validation

Mevcut senaryo, geçersiz kullanıcı bilgilerinin target application tarafından reddedildiğini doğrular.

```gherkin
Scenario: Reject login with invalid credentials
  When the user enters invalid login credentials
  Then an authentication error message should be displayed