import random #for random CPU move selection
import art #import the art.py file
import time #for delay in printing

#Title screen
print(art.art.get("title"))

#inital stats
p1_stats = {"Name": "", "HP": 10, "Power": 0}
cpu_stats = {"Name": "", "HP": 10, "Power": 0}
#Paper  #Sissor #Rock
moveset = ["Punch", "Kick", "Headbutt", "Power"]


#ui displayes HP and Power
def ui(p1y, p1x, cpuy, cpux):
  p1hp = ""
  p1pwr = ""
  cpuhp = ""
  cpupwr = ""
  #player HP display
  for x in range(-1, p1y - 1):
    p1hp = p1hp + "█"
  for x in range(-1, 9 - p1y):
    p1hp = p1hp + "▒"
#cpu HP display
  for x in range(-1, cpuy - 1):
    cpuhp = cpuhp + "█"
  for x in range(-1, 9 - cpuy):
    cpuhp = cpuhp + "▒"
#player power display
  for x in range(-1, p1x - 1):
    p1pwr = p1pwr + "█"
  for x in range(-1, 9 - p1x):
    p1pwr = p1pwr + "▒"
#cpu power display
  for x in range(-1, cpux - 1):
    cpupwr = cpupwr + "█"
  for x in range(-1, 9 - cpux):
    cpupwr = cpupwr + "▒"

  print("  P1 HP:" + p1hp + "  |  P1 PW:" + p1pwr + "    VS.    " +
        " CPU HP:" + cpuhp + "  | CPU PW:" + cpupwr)
  #print(" CPU HP:" + cpuhp + "  | CPU PW:" + cpupwr)


#debug print stats
#print(p1_stats)
#print(cpu_stats)

#setup player 1
p1_name = ""
while p1_name == "":
  p1_name = input("What is your name?\n")

print("Welcome " + str(p1_name) + "!\nThis is it, your big moment!\n")
#update P1 stats
p1_stats.update({"Name": p1_name})

#setup cpu
cpu_names = ["Aviator Biden", "Elon X", "Slug"]
cpu_name = cpu_names[random.randint(0, 2)]
#update cpu stats
cpu_stats.update({"Name": cpu_name})

#debug print stats
#print(p1_stats)
#print(cpu_stats)


#game ends
def game_end(result):
  if result == "playerlose":
    print(art.art.get("lose"))
    update_match = open("results.txt", "w")
    update_match.write(str("l"))
    try_again = input("Rematch? Yes or No?\n")
    if try_again in ("Y", "Yes", "yes", "y"):
      p1_stats.update({"HP": 10})
      p1_stats.update({"Power": 0})
      cpu_stats.update({"HP": 10})
      cpu_stats.update({"Power": 0})
      battle(p1_action(), cpu_action())
    else:
      print(art.art.get("gameover"))
      exit()

  else:
    print(art.art.get("win"))
    update_match = open("results.txt", "w")
    update_match.write(str("w"))
    try_again = input("Rematch? Yes or No?\n")
    if try_again in ("Y", "Yes", "yes", "y"):
      p1_stats.update({"HP": 10})
      p1_stats.update({"Power": 0})
      cpu_stats.update({"HP": 10})
      cpu_stats.update({"Power": 0})
      battle(p1_action(), cpu_action())
    else:
      print(art.art.get("gameover"))
      exit()


def p1_status(hp_mod, power_mod):
  hp_update = min(10, max(0, p1_stats.get("HP") - hp_mod))
  power_update = min(10, max(0, p1_stats.get("Power") + power_mod))
  if hp_update < 1:
    game_end("playerlose")  #trigger end of game
  else:
    p1_stats.update({"HP": hp_update})
    p1_stats.update({"Power": power_update})


def cpu_status(hp_mod, power_mod):
  hp_update = min(10, max(0, cpu_stats.get("HP") - hp_mod))
  power_update = min(10, max(0, cpu_stats.get("Power") + power_mod))
  if hp_update < 1:
    game_end("cpulose")  #trigger end of game
  else:
    cpu_stats.update({"HP": hp_update})
    cpu_stats.update({"Power": power_update})


#Announce fight
print(art.art.get(cpu_stats.get("Name")))
print(str(p1_name) + " Vs. " + str(cpu_stats.get("Name")))
time.sleep(1)
#results and taunt
last_match = open("results.txt", "r")
result = last_match.read(4)
if result == "l":
  print("\nWelcome back loser! Back for more?\n")
  time.sleep(1)
elif result == "w":
  print("\nYou're back huh? You got lucky last time!\n")
  time.sleep(1)
else:
  print("\nFresh meat for the grinder!\n")
  time.sleep(1)


#function P1 Select Move
def p1_action():
  time.sleep(1)
  print("\n--------------------------------------------------------------------------------------------\n")
  ui(p1_stats["HP"], p1_stats["Power"], cpu_stats["HP"], cpu_stats["Power"])
  print("\n--------------------------------------------------------------------------------------------")
  #time.sleep(1) #annoying delay!
  print("\n"+ p1_stats.get("Name")+" Prepare Thy Self\n")
  p1_choose = ""
  p1_choice_vaild = False
  #while p1_choose not in moveset:
  while not p1_choice_vaild:
    p1_choose = input("Choose your move!\n - Punch\n - Kick\n - Headbutt\n - Power\n").title()
    if p1_choose in moveset:
      p1_choice_vaild = True
    else:
      print("\nInvaild choice! Try again\n")

  if p1_choose == "Power" and p1_stats["Power"] < 10:
    return "Power_Fail"
  else:
    return p1_choose


#funcation CPU Select Move
def cpu_action():
  if cpu_stats["Power"] < 10:
    return moveset[random.randint(0, 2)]
  else:
    return moveset[random.randint(0, 3)]  #include power in randint if 10 power


def battle(p1_pick, cpu_pick):
  #print(p1_stats) #for debugging
  #print(cpu_stats) #for debugging
  #print("Player 1 choose " + p1_pick) #for debugging
  #print("CPU choose " + cpu_pick) #for debugging
  #Non-standard attack and block
  if p1_pick == "Power_Fail":
    #Power failure (CPU will not select power unless PW = 10)
    print("\n+ Nothing happens..... +\n")
    time.sleep(1)
    print(".....\n")
    time.sleep(1)
    print("\n+ I cannae do it capt'n I dinnae have the poower! +")
    time.sleep(1)
    print(art.art.get("doh"))
    time.sleep(1)
    print("\n+ You don't have sufficent power! you hurt yourself in the confusion for 2 damage and lost any power you had! +\n")
    p1_status(2, -10)
    cpu_status(0, 0)
    battle(p1_action(), cpu_action())
  elif p1_pick == cpu_pick:
    #both player and cpu select the same, cancel out.
    print(art.art.get("doh"))
    time.sleep(1)
    print("\n+ You both strike each other with the same move! +\n+ No damage inflicted by neither combatant! +\n")
    p1_status(0, 0)
    cpu_status(0, 0)
    battle(p1_action(), cpu_action())
  elif p1_pick == "Power":
    #Player hits CPU with Power
    print(art.art.get("pow"))
    time.sleep(1)
    print("\n+ You strike " + str(cpu_stats.get("Name")) + " with your power move! +\n+ You inflict 3 damage, nice! +\n")
    p1_status(0, -10)
    cpu_status(3, 0)
    battle(p1_action(), cpu_action())
  elif cpu_pick == "Power":
    #CPU hits player with Power
    print(art.art.get("ow"))
    time.sleep(1)
    print(
    str("\n+ "+cpu_stats.get("Name")) + " hits you with a power move! +\n+ You take 3 damage, damn! +\n")
    print("\n+ CPU hits player with Power +\n")
    p1_status(3, 0)
    cpu_status(0, -10)
    battle(p1_action(), cpu_action())
  #regular moves (i.e. rock paper sissor rules)
  elif p1_pick == "Punch":
    if cpu_pick == "Headbutt":
      #print("You punch CPU for 1 damage")
      print(art.art.get("pow"))
      time.sleep(1)
      print("\n+ You sucker punch " + str(cpu_stats.get("Name")) + " +\n+ You inflict 1 damage, nice! +\n")
      p1_status(0, 0)
      cpu_status(1, 2)
      battle(p1_action(), cpu_action())
    else:
      #print("CPU kicks Player for 1 damage")
      print(art.art.get("ow"))
      time.sleep(1)
      print(str("\n+ "+cpu_stats.get("Name")) + " gives you a good kicking! +\n+ You take 1 damage, :( +\n")
      p1_status(1, 2)
      cpu_status(0, 0)
      battle(p1_action(), cpu_action())
  elif p1_pick == "Kick":
    if cpu_pick == "Punch":
      #print("You kick CPU for 1 damage")
      print(art.art.get("pow"))
      time.sleep(1)
      print("\n+ You deliver a swift kick to " + str(cpu_stats.get("Name")) + " +\n+ You inflict 1 damage, nice! +\n")
      p1_status(0, 0)
      cpu_status(1, 2)
      battle(p1_action(), cpu_action())
    else:
      #print("CPU headbutts Player for 1 damage")
      print(art.art.get("ow"))
      time.sleep(1)
      print("\n+ "+str(cpu_stats.get("Name")) + " headbutts you... come on ref! +\n+ You take 1 damage! +\n")
      p1_status(1, 2)
      cpu_status(0, 0)
      battle(p1_action(), cpu_action())
  elif p1_pick == "Headbutt":
    if cpu_pick == "Kick":
      #print("You Headbutt CPU for 1 damage")
      print(art.art.get("pow"))
      time.sleep(1)
      print("\n+ You headbutt " + str(cpu_stats.get("Name")) + " +\n+ You inflict 1 damage, 'ave it! +\n")
      p1_status(0, 0)
      cpu_status(1, 2)
      battle(p1_action(), cpu_action())
    else:
      #print("CPU Punches Player for 1 damage")
      print(art.art.get("ow"))
      time.sleep(1)
      print("\n+ "+str(cpu_stats.get("Name")) + " sucker punches you! +\n+ You take 1 damage! +\n")
      p1_status(1, +2)
      cpu_status(0, 0)
      battle(p1_action(), cpu_action())
  else:
    print("Seems lke you found an error in the code!")


battle(p1_action(), cpu_action())
