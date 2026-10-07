# AcxiomCRM

AcxiomCRM is a role-based Customer Relationship Management web application developed for the Acxiom technical assessment.

## Features

- User authentication
- Role-based authorization
- Customer management
- Lead management
- Opportunity management
- Follow-up management
- Dashboard and KPI cards
- Chart.js analytics
- Audit logging
- REST APIs
- Server-side validation
- Business-rule validation

## Technology Stack

- Python
- Django
- Django REST Framework
- SQLite
- Bootstrap
- JavaScript
- Chart.js

## Modules

- Authentication
- Dashboard
- Customers
- Leads
- Opportunities
- Follow-Ups
- Audit Logs
- REST APIs

## API Endpoints

- GET /api/customers/
- POST /api/customers/
- GET /api/leads/
- POST /api/leads/
- GET /api/opportunities/
- POST /api/opportunities/

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py setup_demo
python manage.py runserver

