class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Creating Player instances
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

players = [
    {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age":32, "position": "Power Foward", "team": "Philidelphia 76ers"},
    {"name": "", "age":16, "position": "P", "team": "en"}
]

new_team = []

for player_dict in players:
    new_player = Player(player_dict)
    new_team.append(new_player)
