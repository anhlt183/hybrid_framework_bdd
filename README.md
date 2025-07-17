# Python Selenium BDD Hybrid Automation Framework

A robust, scalable test automation framework using **Python**, **Playwright**, **Behave (BDD)**, and the **Page Object Model (POM)** architecture.

---

## Project Structure

```
hybrid_framwork_BDD/
│
├── features/
│   ├── login.feature                   # Login test scenarios (valid, invalid, outline)
│   ├── logout.feature                  # Logout scenario
│   └── sorting_product_list.feature    # Sorting product list scenario (by name, price)
│
├── pages/
│   ├── login_page.py           # Page class for login and logout
│   ├── home_page.py            # Page class for home page
│   └── locators/
│       ├── login_locators.py            # Locators for login page
│       └── home_locators.py             # Locators for home page
│
├── step_definations/
│   ├── login_steps.py                   # Step definitions for login
│   ├── logout_steps.py                  # Step definitions for logout
│   └── sorting_product_list_steps.py    # Step definitions for sorting
│
├── reports/                    # Allure reports output (optional)
├── myenv/                      # Python virtual environment
├── conftest.py                 # config to open and close browser   
└── README.md                   # Project documentation
```

---

## Tech Stack

| Component       | Description                           |
|---------------  |---------------------------------------|
| **Python**      | Core programming language             |
| **Playwright**  | End-to-End Browser Automation         |
| **Pytest**      | Python testing framework              |
| **POM**         | Page Object Model for abstraction     |
| **Allure**      | Rich test reports                     |
| **Logging**     | `logging` module for step tracing     |

---

## Features Covered

### **Login Functionality**

- Successful login with valid credentials  
- Login failure with invalid credentials  
- Scenario Outline for data-driven invalid login test cases  
- Form validation for blank fields

### **Logout Functionality**

- Log out from the Home page  
- Redirects back to login page  
- Login form remains visible after logout  

### **Sorting product list on Home page Functionality**

- Sorting product list with Name (A to Z) order 
- Sorting product list with Name (Z to A) order  
- Sorting product list with Price (low to high) order  
- Sorting product list with Price (high to low) order  

---

## Installation steps
1. In Terminal, select the root folder project `cd hybrid_framwork_BDD`
2. Create virtual environment management directory `python -m venv myenv`
3. Activate virtual environment `myenv\Scripts\activate`
4. Install all project dependencies with `pip install -r requirements.txt`

## Run test
Run all test `pytest`
Run specific feature file `pytest features/logout.feature`
Run specific scenarion in a feature file `pytest features/logout.feature -k "Successfull logout from the application"`

## Reporting with Allure

Install Allure CLI:

```bash
pip install allure-pytest
```

Run tests and generate report:

```bash
pytest -v step_definations/logout_steps.py --alluredir=allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure serve reports/
```

---

## Notes & Best Practices
- Use `strip()` or default `''` for empty string handling in Scenario Outlines.
- Structure your Page classes well with locators, actions, and status checkers.
---

## Author

**AnhLT183**  
_A QA Engineer._