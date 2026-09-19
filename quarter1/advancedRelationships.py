import random


# 1. PARENT CLASS
class Person:

  def __init__(self, name: str, age: int, nationality: str):
    self.name = name
    self.age = age
    self.nationality = nationality


# 2. DEPENDENCY CLASS
class Match:

  def __init__(self, opponent_name: str, venue: str):
    self.opponent_name = opponent_name
    self.venue = venue


# 3. CHILD CLASS 
class Footballer(Person):

  def __init__(
      self,
      name: str,
      age: int,
      nationality: str,
      position: str,
      overallrating: int,
      height: int,
      playstyle: str,
  ):
    # Call parent class constructor
    super().__init__(name, age, nationality)
    self.position = position
    self.__overall_rating = overallrating
    self.height = height
    self.playstyle = playstyle

  def get_overall_rating(self) -> int:
    return self.__overall_rating

  def pass_ball(self, target_player: str) -> None:
    print(f"{self.name} passes to {target_player}!")

  def dribble(self, defender_name: str) -> None:
    print(
        f"{self.name} dribbles {defender_name} using their {self.playstyle}"
        " playstyle!"
    )

  def shoot(self) -> None:
    outcome = random.choice(["goal", "miss"])
    if outcome == "goal":
      self.__overall_rating += 1
      if self.__overall_rating > 99:
        self.__overall_rating = 99
      print(
          f"GOAL! {self.name} scored! Ovr increased to {self.__overall_rating}."
      )
    else:
      print(f"{self.name} took a shot but missed.")

  # Dependency relationship 
  def play_match(self, match: Match) -> None:
    print(f"{self.name} is playing a match against {match.opponent_name} at {match.venue}!")


# 4. CONTAIN Footballer CLASS
class FootballClub:

  def __init__(
      self,
      name: str,
      overallrating: int,
      transfer_budget: float,
      popularity: int,
      squad: list = None,
  ):
    self.name = name
    self.__overall_rating = overallrating
    self.__transfer_budget = transfer_budget
    self.__popularity = popularity
    self.__squad = squad if squad is not None else []

  def get_overall_rating(self) -> int:
    return self.__overall_rating

  def get_popularity(self) -> int:
    return self.__popularity

  def get_squad(self) -> list:
    return self.__squad

  def get_squad_size(self) -> int:
    return len(self.__squad)

  def add_player(self, player: Footballer) -> None:
    self.__squad.append(player)
    print(f"{player.name} joined {self.name}!")

  def remove_player(self, player: Footballer) -> None:
    if player in self.__squad:
      self.__squad.remove(player)
      print(f"{player.name} left {self.name}.")


player1 = Footballer("Keane", 14, "LW", "Filipino", random.choice(range(78, 98)), 170, "Trickster")  
player2 = Footballer("Paul", 15, "ST", "Filipino", random.choice(range(78, 98)), 175, "Shooter")

print("--- Footballer Actions ---")
print(f"Player: {player1.name} (Overall: {player1.get_overall_rating()})")
player1.pass_ball(player2.name)
player1.dribble("Heinrich")
player1.shoot()

# 3. Test Dependency (Match class)
print("\n--- Match Dependency ---")
upcoming_match = Match(opponent_name="Real Madrid", venue="Santiago Bernabéu")
player1.play_match(upcoming_match)

# 4. Create a FootballClub instance
print("\n--- FootballClub Class ---")
club1 = FootballClub(
    name="Bantayog FC",
    overallrating=88,
    transfer_budget=150000000.0,
    popularity=95
)

# 5. Test Aggregation (Adding and managing players)
club1.add_player(player1)
club1.add_player(player2)

print(f"\nCurrent Squad Size: {club1.get_squad_size()}")
print("Squad List:", [player.name for player in club1.get_squad()])

# Remove a player to test squad reduction
club1.remove_player(player2)
print(f"Updated Squad Size: {club1.get_squad_size()}")