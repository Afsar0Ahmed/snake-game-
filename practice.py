class Footballer:
    def __init__(self,nationality,goal,club):
        self.club = club
        self.nationality = nationality
        self.goal  = goal
    def speed(self):
        print("his speed 30km/h ")


ronaldo = Footballer("christan",806,"menchestar united")
ronaldo.speed()
print(ronaldo.club)

