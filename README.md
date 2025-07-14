# Python Selenium BDD Hybrid Automation Framework

A robust, scalable test automation framework using **Python**, **Selenium WebDriver**, **Behave (BDD)**, and the **Page Object Model (POM)** architecture.

---

## Project Structure

```
hybrid_framwork_BDD/
│
├── features/
│   ├── login.feature                   # Login test scenarios (valid, invalid, outline)
│   ├── logout.feature                  # Logout scenario
│   ├── sorting_product_list.feature    # Sorting product list scenario (by name, price)
│   ├── steps/
│   │   ├── login_step.py                   # Step definitions for login
│   │   ├── logout_step.py                  # Step definitions for logout
│   │   └── sorting_product_list_step.py    # Step definitions for sorting
│   └── environment.py          # Hooks (setup/teardown)
│
├── pages/
│   ├── login_page.py           # Page class for login and logout
│   └── home_page.py            # Page class for home page
│
├── utils/
│   └── browser_utils.py        # WebDriver initialization and utilities
│
├── reports/                    # Allure reports output (optional)
├── myenv/                      # Python virtual environment
├── conftest.py                 # config to open and close browser   
└── README.md                   # Project documentation
```

---

## Tech Stack

| Component     | Description                           |
|---------------|---------------------------------------|
| **Python**    | Core programming language             |
| **Selenium**  | Browser automation                    |
| **Behave**    | BDD-style test execution              |
| **POM**       | Page Object Model for abstraction     |
| **Allure**    | Rich test reports                     |
| **Logging**   | `logging` module for step tracing     |

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

## How to Run

### 1. Activate virtual environment

```bash
cd hybrid_framwork_BDD
myenv\Scripts\activate
```

### 2. Run All Features

```bash
behave
```

### 3. Run Specific Feature File

```bash
behave features/logout.feature
```

### 4. Run Specific Scenario or Tag

```bash
behave -n "Successfull logout from the application"
```

---

## Hooks (`environment.py`)

- `before_all` → Launches browser  
- `after_all` → Closes browser  

---

## Reporting with Allure

Install Allure CLI:

```bash
pip install allure-behave
```

Run tests and generate report:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
allure serve reports/
```

---

## Notes & Best Practices

- Duplicate step definitions (e.g. `@then('the login form should still be visible')`) should be shared in only one step file to avoid `AmbiguousStep` errors.
- Use `context.<page>` objects carefully — always initialize them before use.
- Use `strip()` or default `''` for empty string handling in Scenario Outlines.
- Structure your Page classes well with locators, actions, and status checkers.

---

## Author

**AnhLT183**  
_A QA Engineer._