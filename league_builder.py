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

    # Assignes experienced kids among the three teams
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

    # Assignes experienced kids among the three teams
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
    In the list of teams, include the team name on one line, followed by a separate line for each player. Include the 
    player's name, whether the player has experience playing soccer, and the player's guardian names. Separate each 
    bit of player information by a comma.
    '''