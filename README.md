# Platzi-Commerce-API
Platzi-Commerce-API Automation Framework  Professional API Automation Testing Framework for E-Commerce Services using Python, Pytest, Requests and allure report.

---

## 🚀 Tech Stack

* Python 3.11
* Pytest
* Requests
* Allure Report
* JSON Schema Validation
* Pydantic
* GitHub Actions CI/CD

---

## 📁 Project Structure

```bash
PLATZI-COMMERCE-API/
│
├── .github/
│   └── workflows/
│       └── api-automation.yml
│
├── clients/
│   └── api_client.py
│
├── data/
│   ├── login_invalid.json
│   └── login_valid.json
│
├── endpoints/
│   └── auth_endpoint.py
│
├── models/
│   └── auth_model.py
│
├── schemas/
│   └── auth_schema.py
│
├── services/
│   └── auth_service.py
│
├── tests/
│   ├── api/
│   ├── e2e/
│   └── functional/
│       └── test_auth_api.py
│
├── utils/
│   └── file_reader.py
│
├── allure-results/
├── allure-report/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .env
```

---

## ✨ Features

* API testing with Pytest
* JSON Schema Validation
* Request & Response Validation
* Pydantic Data Models
* Allure Reporting
* Environment Variable Support
* GitHub Actions CI Integration
* Scalable Framework Structure
* Service Layer Pattern
* Reusable API Client

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/platzi-commerce-api.git
cd platzi-commerce-api
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Linux / MacOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create `.env` file:

```env
BASE_URL=https://api.example.com
```

---

## ▶️ Running Test

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test

```bash
pytest tests/functional/test_auth_api.py -v
```

### Run Positive Test

```bash
pytest -m positive
```

---

## 📊 Allure Report

### Generate Allure Result

```bash
pytest tests/ --alluredir=allure-results
```

### Open Allure Report

```bash
allure serve allure-results
```

### Generate Static Report

```bash
allure generate allure-results --clean -o allure-report
```

---

## 🔄 GitHub Actions CI/CD

This project uses GitHub Actions for Continuous Integration.

### Workflow Features

* Automatic test execution
* Allure report generation
* Artifact upload
* Multi-branch support
* Pull Request validation

Workflow file:

```bash
.github/workflows/api-automation.yml
```

---

## 🧪 Test Categories

| Category   | Description                  |
| ---------- | ---------------------------- |
| Functional | Validate API functionality   |
| Smoke      | Critical endpoint validation |
| Regression | Full API regression testing  |
| E2E        | End-to-end workflow testing  |

---

## 📌 Example Test

```python
@pytest.mark.smoke
def test_login_success(auth_service):
    response = auth_service.login(valid_payload)

    assert response.status_code == 200
```

---

## 📈 Reporting

Allure report includes:

* Request payload
* Response payload
* Test steps
* Attachments
* Execution history
* Failed test details

---

## 🛠 Future Improvements

* Docker Integration
* Jenkins Pipeline
* Parallel Execution
* Dynamic Environment Config
* API Contract Testing
* Performance Testing
* Slack Notification
* Auto Deploy Allure Report

---

## 👨‍💻 Author

Disky Adit

QA Automation Engineer

---

## 📄 License

This project is intended for portfolio, and automation testing practice.
