# Credit Approval System

A modern web application for managing credit approval processes and loan management built with Django and Django REST Framework.

## Features

- Customer management system
- Loan application processing
- Credit limit management
- Loan repayment tracking
- RESTful API endpoints
- Docker containerization support

## Project Structure

```
credit_approval_system/
├── api/
│   ├── models.py      # Database models
│   ├── views.py       # API endpoints
│   ├── serializers.py # Data serialization
│   └── urls.py        # API routing
├── credit_approval_system/
│   └── settings.py    # Project configuration
├── requirements.txt   # Project dependencies
├── Dockerfile         # Docker configuration
└── docker-compose.yml # Docker Compose configuration
```

## Technology Stack

- Backend: Django 5.2.1
- API Framework: Django REST Framework 3.14.0
- Database: PostgreSQL (via psycopg2)
- Message Broker: Redis
- Task Queue: Celery
- Web Server: Gunicorn

## Installation

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- PostgreSQL
- Redis

### Using Docker (Recommended)

1. Clone the repository
2. Build and run containers:
   ```bash
   docker-compose up --build
   ```

### Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (copy from .env.example):
   ```bash
   cp .env.example .env
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

The API provides endpoints for:
- Customer management (CRUD operations)
- Loan applications
- Credit limit management
- Loan repayment tracking

## Database Schema

### Customer Model
- Customer ID (auto-generated)
- First Name
- Last Name
- Age
- Phone Number
- Monthly Salary
- Approved Credit Limit
- Current Debt

### Loan Model
- Loan ID (auto-generated)
- Customer ID (foreign key)
- Loan Amount
- Tenure
- Interest Rate
- Monthly Repayment
- EMIs Paid on Time
- Start Date
- End Date

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

