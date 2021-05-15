import firebase_admin
from firebase_admin import credentials
from server import is_production

firebase_secret_path = "server/firebase/account-service-secret.json"

if is_production:
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': "caspita-lucca",
    })
else:
    cred = credentials.Certificate(firebase_secret_path)
    firebase_admin.initialize_app(cred)
