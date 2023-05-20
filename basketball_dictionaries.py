# Basketball Dictionaries Assignment

# Challenge 1: Update the Constructor

    # Update the constructor to accept a dictionary with a single player's
    # information instead of individual arguments for the attributes.

class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

# method to format elements and create a cleaner output
    def __repr__(self):
        return "Player: {}, Age: {}, Position: {}, Team: {}, ".format(
            self.name, self.age, self.position, self.team)

# NINJA BONUS :  Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.

    @classmethod
    def get_team(cls, team_list):
        player_objects = []
        for dict in team_list:
            player_objects.append(dict)
        return player_objects

# Challenge 2: Create instances using individual player dictionaries.
    # Given these variables, create Player instances for each of the following dictionaries.
    # # Be sure to instantiate these outside the class definition, in the outer scope.

# List of Players :
kevin = {
    "name": "Kevin Durant",
    "age":34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age":24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age":32, "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# index of players within dictionary to be added to teams generated from for loop in challenge3
players = [
    {
    "name": "Kevin Durant",
    "age":34,
    "position": "small forward",
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum",
    "age":24,
    "position": "small forward",
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving",
    "age":32, "position": "Point Guard",
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard",
    "age":33, "position": "Point Guard",
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid",
    "age":32, "position": "Power Foward",
    "team": "Philidelphia 76ers"
    },
    {
    "name": "",
    "age":16,
    "position": "P",
    "team": "en"
    }
]

# instances of the three players listed in the Player dictionary above >>>
player_kevin = Player(kevin)
print(player_kevin, "\n")

player_jason = Player(jason)
print(player_jason, "\n")

player_kyrie = Player(kyrie)
print(player_kyrie, "\n")

# Challenge 3: Make a list of Player instances from a list of dictionaries
    # Finally, given the example list of players at the top of this module (the one with many players)
    # # write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

    print(new_team, "\n")


