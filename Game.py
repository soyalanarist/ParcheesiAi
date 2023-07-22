from Player import Player
from GameGUI import GameGUI as gui

# create 4 players
red = Player("red")
blue = Player("blue")
green = Player("green")
yellow = Player("yellow")
players = [red, blue, green, yellow]

# decide starting player
tie = True
highest = 0

while tie:
    rolls = []
    for player in players:
        who_rolled = player.get_color()
        roll_value = player.roll_die()
        rolls.append((who_rolled, roll_value))
        print(who_rolled + " rolled a " + str(roll_value))

    # check if any of the rolls are equal
    rolls_set = set(roll[1] for roll in rolls)
    print("the rolls are:", rolls) # debug")
    print("the unique rolls are:", rolls_set) # debug
    print("") # debug
    if len(rolls) == len(rolls_set):
        tie = False


    # make players include only the players who tied for highest roll
    players = []
    highest = max(rolls_set)
    for roll in rolls:
        if roll[1] == highest:
            if roll[0] == "red":
                players.append(red)
            elif roll[0] == "blue":
                players.append(blue)
            elif roll[0] == "green":
                players.append(green)
            elif roll[0] == "yellow":
                players.append(yellow)

print("the first player is:", players[0].get_color()) # debug
# who goes first
goes_first = players[0].get_color()
goes_first_index = 0

# reset players to default order
players = [red, blue, green, yellow]

for player in players:
    if player.get_color() == goes_first:
        if player.get_color() == "red":
            goes_first_index = 0
        elif player.get_color() == "blue":
            goes_first_index = 1
        elif player.get_color() == "green":
            goes_first_index = 2
        elif player.get_color() == "yellow":
            goes_first_index = 3

for roll in rolls:
    if roll[1] == goes_first:
        goes_first_index = rolls.index(roll)

players = players[goes_first_index:] + players[:goes_first_index]
print("the order of play is:") # debug
for player in players:
    print(player.get_color()) # debug




# everyone rolls once
# for player in players:
#     roll = player.roll()

gui()