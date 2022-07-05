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
hasPicked = input("Do you want to make a note or read a note? (n/r)\n")
class MakeNote:
  if hasPicked.lower() == "n" or hasPicked.lower() == "N": 
          note = input("What is the name of the note? Do not add spaces and symbols. So please instead of symbols/spaces please just combine the letters together.\n")
          noteContents = input("Please enter the contents of the note. Please note this doesn't work with multilines.\n")
          Data = {"Note name": note, "Note Contents": noteContents}
          db.collection("Data").add(Data)
          print("Saved your note.")
          exit()
  elif hasPicked.lower()  == "R" or hasPicked.lower() == "r":
    docs = db.collection("Data").stream()
    print("Please enter the name of the note you want to read")
    note = input()
    for doc in docs:
      try:  
        if doc.to_dict()["Note name"] == note:
          print(doc.to_dict()["Note contents"])
    
      except:
          print("Could not find the note.")
          exit(400)
MakeTheNote = MakeNote()
