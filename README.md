# Okta User Management Demo

Python script demonstrating Okta user lifecycle management via REST API.

## What it does
- Lists all users in an Okta tenant
- Creates a new user programmatically
- Triggers password reset
- Deactivates and deletes users (cleanup)

## Tech Stack
- Python 3 + requests
- Okta REST API (SSWS token auth)
- python-dotenv for secure credential management

## Setup
```bash
pip3 install requests python-dotenv
```

Create `.env`:

Run:
```bash
python3 okta_manager.py
```

## Skills demonstrated
- Identity & Access Management (IAM)
- REST API integration
- User provisioning/deprovisioning automation
- Secure credential management

## Author
Damian Ciasnocha — IT Systems Engineer
