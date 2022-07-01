import firebase_admin, time, subprocess, platform
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
docs = db.collection("Data").stream()
print("Please enter the name of the note you want to read")
note = input()
for doc in docs:
    if doc.to_dict()["Note name"] == note:
        print(doc.to_dict()["Note contents"])
        exit()