class ClubMembers:
    def __init__(self, name, birthdate, age, favorite_food, goal):
        self.name = name
        self.birthdate = birthdate
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def introduce1(self):
        print("Name: ", self.name)
        print("Birthdate: ", self.birthdate)
        print("Age: ", self.age)
        print("Favoritefood: ", self.favorite_food)
        print("Goal: ", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthdate, age, favorite_food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthdate, age, favorite_food, goal)

    def introduce2(self):
        print("Name: ", self.name)
        print("Birthdate: ", self.birthdate)
        print("Age: ", self.age)
        print("Favoritefood: ", self.favorite_food)
        print("Goal: ", self.goal)
        print("Position", self.position)

m_1 = ClubMembers("Tom", "January 16", 14, "Ice Cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef strogranoff", "To be the world's greatest chef", "Treasurer")

m_1.introduce1()
o_4.introduce2()
