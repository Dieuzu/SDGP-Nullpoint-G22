def firebase():
    import pyrebase
    import os

    firebaseConfig = {
        "apiKey": "AIzaSyCeXR5EW5_hbrXoZ8eAdcCcXP6To7LMtNo",
        "authDomain": "assignment-manager-b9138.firebaseapp.com",
        "projectId": "assignment-manager-b9138",
        "storageBucket": "assignment-manager-b9138.appspot.com",
        "messagingSenderId": "497245345518",
        "appId": "1:497245345518:web:88d2a75f1a9616d1f245ff",
        "measurementId": "G-8YRRW7N1GW",
        "databaseURL" : ""
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()

    path_on_cloud = "images/[object File]"
    filename = os.path.splitext(path_on_cloud)

    storage.child(path_on_cloud).download("D:\\Git_repose\\SDGP-Nullpoint-G22\\input\\file.docx")




