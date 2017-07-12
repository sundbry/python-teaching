import random


warriors = ["Steph Curry", "Klay Thompson", "Draymond Green", "Kevin Durant", "Andre Iguodala"]
cavaliers = ["LeBron James", "Kyrie Irving", "Kevin Love", "JR Smith", "Tristian Thompson"]
teams = [warriors, cavaliers]
team_names = ["Golden State Warriors", "Cleveland Cavaliers"]

def print_team_lineup(roster):
  print("The starting lineup is: ")
  for player in roster:
    print player + " "

# This is a comment
# print_team_lineup(warriors)

def print_starting_lineups():
  print("2017 NBA Championship Finals")
  print("")
  for team in teams:
    print_team_lineup(team)

def simulate_game():
  winning_team = None
  while winning_team == None:
    warriors_score = random.randint(75, 166)
    cavs_score = random.randint(80, 150)
    if cavs_score < warriors_score:
      winning_team = "Golden State Warriors"
    if warriors_score < cavs_score:
      winning_team = "Cleveland Cavaliers"
    if warriors_score == cavs_score:
      print("Overtime!")
      winning_team = None

  #winning_team = random.choice(team_names)
  print("Final score:")
  print("Golden State Warriors: " + str(warriors_score))
  print("Cleveland Cavaliers: " + str(cavs_score))
  print("The " + winning_team + " won!")
  return winning_team

def print_mvp(winning_team_name):
  mvp = "Nobody"
  if winning_team_name == "Golden State Warriors":
    mvp = random.choice(warriors)
  if winning_team_name == "Cleveland Cavaliers":
    mvp = random.choice(cavaliers)
  print("The MVP of the game is " + mvp)

print_starting_lineups()
print("")
winner = simulate_game()
print_mvp(winner)
