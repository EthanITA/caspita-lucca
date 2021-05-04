import os

import firebase_admin
from firebase_admin import credentials

if bool(os.getenv("is_gcloud", '')):
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': "caspita-lucca",
    })
else:
    cred = credentials.Certificate('account-service-secret.json')
    firebase_admin.initialize_app(cred)
