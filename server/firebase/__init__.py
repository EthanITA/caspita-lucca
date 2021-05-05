import os

import firebase_admin
from firebase_admin import credentials

firebase_secret_path = "server/firebase/account-service-secret.json" \
    if __name__ == '__main__' else "account-service-secret.json"
if bool(os.getenv("is_gcloud", '')):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': "caspita-lucca",
    })
else:
    cred = credentials.Certificate('server/firebase/account-service-secret.json')
    firebase_admin.initialize_app(cred)
