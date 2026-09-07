import random

class Footballer:
    def __init__(self, name: str, age: int, position: str, nationality: str, overallrating: int, height: int, playstyle: str):
        self.name = name  
        self.age = age  
        self.position = position  
        self.nationality = nationality  
        self.__overall_rating = (overallrating)
        self.height = height
        self.playstyle = playstyle

    def get_overall_rating(self):
        return self.__overall_rating

    def pass_ball(self, target_player: str):
        print(f"{self.name} passes to {target_player}!")


    def dribble(self, defender_name: str):
        print(
            f"{self.name} dribbles {defender_name} using their {self.playstyle} playstyle!"
        )


    def shoot(self):
        outcome = random.choice(["goal", "miss"])
        if outcome == "goal":
            self.__overall_rating += 1  
            if self.__overall_rating > 99:
                print(
                f"GOAL! {self.name} scored! Ovr increased to {self.__overall_rating}."
            )
        else:
            print(f"{self.name} took a shot but missed.")



if __name__ == "__main__":
    teammates = ["Zach", "Niane", "Heinrich", "Byoung", "Jack"]

    player1 = Footballer(
        "Keane", 14, "LW", "Filipino", random.choice(range(78, 98)), 170, "Trickster"
    )  
    player2 = Footballer(
        "Paul", 15, "ST", "Filipino", random.choice(range(78, 98)), 175, "Shooter"
    )  

    
    print("Initial State:")
    print(f"Object 1 ({player1.name}) OVR: {player1.get_overall_rating()}")
    print(f"Object 2 ({player2.name}) OVR: {player2.get_overall_rating()}\n")

    print(f"Perform actions on: {player1.name}") 
    player1.pass_ball(random.choice(teammates))
    player1.dribble("Paul")


    player1._Footballer__overall_rating += (
        1  \
    )
    print(f"{player1.name} scored in training! (+1 OVR)\n")

    print("Demonstrating Object Independence: Final State")
    print(
        f"Object 1 ({player1.name}) OVR: {player1.get_overall_rating()} (UPDATED)"
    )
    print(
        f"Object 2 ({player2.name}) OVR: {player2.get_overall_rating()} (UNCHANGED)"
    )