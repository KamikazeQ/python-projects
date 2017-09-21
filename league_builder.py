import csv

if __name__ == "__main__":
    '''
    Create variables and programming logic to divide the 18 players into three teams: Sharks, Dragons and Raptors. 
    Make sure the teams have the same number of players on them, and that the experience players are divided equally 
    across the three teams.
    '''

    # Create list for sorting
    experienced = []
    not_experienced = []

    # Create teams as lists
    Sharks = []
    Dragons = []
    Raptors = []

    # Used for identifying team
    turn = 1

    # Opens and reads the csv.  Places the experienced and inexperienced into two different lists.
    with open('soccer_players.csv') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for row in rows[1:]:
            if row[2] == 'YES':
                del row[1]
                experienced.append(row)
            else:
                del row[1]
                not_experienced.append(row)

    # Assigns experienced kids among the three teams
    while len(experienced):
        if turn == 1:
            Sharks.append(experienced.pop())
            turn = 2
        elif turn == 2:
            Dragons.append(experienced.pop())
            turn = 3
        elif turn == 3:
            Raptors.append(experienced.pop())
            turn = 1

    # Assigns experienced kids among the three teams
    while len(not_experienced):
        if turn == 1:
            Sharks.append(not_experienced.pop())
            turn = 2
        elif turn == 2:
            Dragons.append(not_experienced.pop())
            turn = 3
        elif turn == 3:
            Raptors.append(not_experienced.pop())
            turn = 1

    '''
    Create a text file named teams.txt that includes the name of a team, followed by the players on that team. List 
    all three teams and their players.
    '''
    '''
    TO EXCEED EXPECTATIONS:
    In the list of teams, include the team name on one line, followed by a separate line for each player. Include the 
    player's name, whether the player has experience playing soccer, and the player's guardian names. Separate each 
    bit of player information by a comma.
    '''

    # Create the main output file
    file = open("teams.txt", "w")
    file.write("Sharks\n")
    # Used to iterate through team list
    count = 0
    # writes the info and creates the letters
    for item in Sharks:
        file.write("Player: {}, is Experienced: {},"
                   " name of guardians: {}\n".format(Sharks[count][0], Sharks[count][1], Sharks[count][2]))
        # Create letter
        letter = open(str.lower(Sharks[count][0]).replace(" ", "_") + ".txt", "w")
        letter.write("Dear {},\n\n"
                     "Your child, {}, has been assigned to the Sharks team.\nThe first practice is scheduled for "
                     "October 1st at 5PM.".format(Sharks[count][2], Sharks[count][0]))
        count += 1
    file.write("\n")
    file.write("Dragons\n")
    count = 0
    for item in Dragons:
        file.write("Player: {}, is Experienced: {},"
                   " name of guardians: {}\n".format(Dragons[count][0], Dragons[count][1], Dragons[count][2]))
        # Create letter
        letter = open(str.lower(Dragons[count][0]).replace(" ", "_") + ".txt", "w")
        letter.write("Dear {},\n\n"
                     "Your child, {}, has been assigned to the Dragons team.\nThe first practice is scheduled for "
                     "October 1st at 5PM.".format(Dragons[count][2], Dragons[count][0]))
        count += 1
    file.write("\n")
    file.write("Raptors\n")
    count = 0
    for item in Raptors:
        file.write("Player: {}, is Experienced: {},"
                   " name of guardians: {}\n".format(Raptors[count][0], Raptors[count][1], Raptors[count][2]))
        # Create letter
        letter = open(str.lower(Raptors[count][0]).replace(" ", "_") + ".txt", "w")
        letter.write("Dear {},\n\n"
                     "Your child, {}, has been assigned to the Raptors team.\nThe first practice is scheduled for "
                     "October 1st at 5PM.".format(Raptors[count][2], Raptors[count][0]))
        count += 1
    file.write("\n")

