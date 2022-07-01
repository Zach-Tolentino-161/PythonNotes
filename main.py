import firebase_admin, time, subprocess, platform
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("credentials/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
def sleep(sec):
    time.sleep(sec)
def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear",
                     shell=True)
hasPicked = input("Do you want to make a note? (n)\n")
if hasPicked == "n" or "N": 
        note = input("What is the name of the note?\n")
        print("If you want to save the note, press s")
        noteContents = input("Please enter the contents of the note. Please know this doesn't work with multilines. Sorry I am still learning code\n")
        Data = {"Note name": note, "Note contents": noteContents}
        db.collection("Data").add(Data)
        clear()
        exit()