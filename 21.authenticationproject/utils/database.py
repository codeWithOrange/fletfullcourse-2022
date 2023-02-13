import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyDxHj-vwGe8PzJin6f2QVR2BQMSC4NkibY",
  'authDomain': "authfletproject.firebaseapp.com",
  'databaseURL': "https://authfletproject-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "authfletproject",
  'storageBucket': "authfletproject.appspot.com",
  'messagingSenderId': "935126692974",
  'appId': "1:935126692974:web:8b1c50642c4dbc1b44e27f",
  'measurementId': "G-N7LJXES293"
};

databaseFirebase=pyrebase.initialize_app(firebaseConfig)
auth=databaseFirebase.auth()
database=databaseFirebase.database()



