class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name=user_name
        self.followers=0 #setting a default values so that we no need to pass this every time object is created

# user1=User()
# user1.user_name="Phani"
# user1.user_id="001"
# print(user1.user_name)
# print(user1.user_id)


user2=User("002","Lucky")
print(user2)
print(user2.id)
print(user2.name)
print(user2.followers )