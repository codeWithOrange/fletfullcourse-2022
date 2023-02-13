class UserModel:
    def __init__(
            self,
            userId:str,
            username:str,
            email:str,
            password:str,
    ):
        self.userId=userId
        self.username=username
        self.email=email
        self.password=password

    def toMap(self):
        return {
            'userId':self.userId,
            'username':self.username,
            'email':self.email,
            'password':self.password

        }
    
    @staticmethod
    def fromMap(map:dict):
        return UserModel(
            userId=map['userId'],
            username=map['username'],
            email=map['email'],
            password=map['password']
        )