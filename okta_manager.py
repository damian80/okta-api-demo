import os
import requests
from dotenv import load_dotenv

load_dotenv()

ORG_URL = os.getenv('OKTA_ORG_URL')
TOKEN = os.getenv('OKTA_API_TOKEN')

HEADERS = {
    'Authorization': f'SSWS {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def list_users():
    print("\n📋 LISTING ALL USERS:")
    r = requests.get(f"{ORG_URL}/api/v1/users", headers=HEADERS)
    users = r.json()
    for u in users:
        p = u['profile']
        print(f"  - {p['firstName']} {p['lastName']} | {p['email']} | Status: {u['status']}")
    return users

def create_user():
    print("\n➕ CREATING TEST USER...")
    payload = {
        "profile": {
            "firstName": "Test",
            "lastName": "Engineer",
            "email": "test.engineer@harrodian-demo.com",
            "login": "test.engineer@harrodian-demo.com"
        }
    }
    r = requests.post(f"{ORG_URL}/api/v1/users?activate=false", headers=HEADERS, json=payload)
    user = r.json()
    if 'id' in user:
        print(f"  ✅ Created: {user['profile']['email']} (ID: {user['id']})")
        return user['id']
    else:
        print(f"  ⚠️  Error: {user}")
        return None

def deactivate_user(user_id):
    print("\n🔒 DEACTIVATING USER...")
    r = requests.post(f"{ORG_URL}/api/v1/users/{user_id}/lifecycle/deactivate", headers=HEADERS)
    print(f"  ✅ Deactivated (status: {r.status_code})")

def delete_user(user_id):
    print("\n🗑️  DELETING USER (cleanup)...")
    r = requests.delete(f"{ORG_URL}/api/v1/users/{user_id}", headers=HEADERS)
    print(f"  ✅ Deleted (status: {r.status_code})")

def reset_password(user_id):
    print("\n🔑 TRIGGERING PASSWORD RESET...")
    r = requests.post(f"{ORG_URL}/api/v1/users/{user_id}/lifecycle/reset_password?sendEmail=false", headers=HEADERS)
    data = r.json()
    if 'resetPasswordUrl' in data:
        print(f"  ✅ Reset URL generated")
    else:
        print(f"  ✅ Reset triggered (status: {r.status_code})")

print("=" * 50)
print("OKTA USER MANAGEMENT DEMO")
print("=" * 50)

list_users()
user_id = create_user()

if user_id:
    reset_password(user_id)
    deactivate_user(user_id)
    delete_user(user_id)

print("\n" + "=" * 50)
print("✅ Demo complete.")
