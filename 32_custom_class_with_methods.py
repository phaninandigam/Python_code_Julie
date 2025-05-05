class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name=user_name
        self.followers=0 #setting a default values so that we no need to pass this every time object is created
        self.following=0

    def follow(self, user):
        user.followers+=1
        self.following+=1



user1=User("001","Phani")
user2=User("002","Lucky")
print(user2) #hash key
print(user2.id, user2.name)
# print(user2.name)
print(user2.followers )

user1.follow(user2)
print(user1.following)
print(user2.followers)