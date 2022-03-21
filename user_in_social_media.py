class User:
    def __init__(self, firstName, lastName, likesCount, friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount =likesCount
        self.friendsName = friendsName
        print("User created name: " + self.firstName)

    def fullName(self):
        print("Hi I'm " + self.firstName + " " + self.lastName)

    def fullProfile(self):
        print("Full Name: " + self.firstName + " " + self.lastName)
        print("Likes    : " + str(self.likesCount))
        print("Friends")
        for friend in self.friendsName:
            print("  -" + friend)

userOne = User("Abbey", "Santos", 20,["Yae", "Ningguang", "Baal", "Beidou"])
userOne.fullProfile()