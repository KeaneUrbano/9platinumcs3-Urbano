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



class FootballClub:
    def __init__(self, name: str, age: int, overallrating: int, transfer_budget: int, popularity: int, squad_size: list = []):
        self.name = name  
        self.age = age  
        self.__overall_rating = (overallrating)
        self.__transfer_budget = transfer_budget
        self.__popularity = popularity
        self.__squad_size = squad_size

    def get_overall_rating(self):
        return self.__overall_rating
    def get_transfer_budget(self):
        return self.__transfer_budget
    def get_popularity(self):
        return self.__popularity
    
    def get_squad_size(self):
        return self.__squad_size

    def add_player(self, player: Footballer) -> None:
        self.__squad_size.append(player)

    def remove_player(self, player: Footballer) -> None:
        if player in self.__squad_size:
            self.__squad_size.remove(player)


#--- BEFORE ASSOCIATION ---
print("--- BEFORE RELATIONSHIP ---")
print("player 1 = Footballer('Keane', 14, 'LW', 'Filipino', 85, 170, 'Flair')")
print("player 2 = Footballer('Heinrich', 15, 'CAM', 'Filipino', 82, 168, 'Playmaker')")
print("club = FootballClub('Bantayog F.C', 2026, 88, 50000000, 90)")
player1 = Footballer("Keane", 14, "LW", "Filipino", 85, 170, "Flair")
player2 = Footballer("Heinrich", 15, "CAM", "Filipino", 82, 168, "Playmaker")
club = FootballClub("Bantayog F.C", 2026, 88, 50000000, 90)


# --- Association Being Formed ---
print("---BUILDING RELATIONSHIP---")
print("club.add_player(player1)")
print("club.add_player(player2)")
club.add_player(player1)
club.add_player(player2)

# --- After Relationship ---
print("---AFTER RELATIONSHIP---")
print(f"Club Name: {club.name}")
print(f"Total Players in Squad: {len(club.get_squad_size())}")
print(f"Player 1: {club.get_squad_size()[0].name}, Position: {club.get_squad_size()[0].position}")
print(f"Player 2: {club.get_squad_size()[1].name}, Position: {club.get_squad_size()[1].position}")