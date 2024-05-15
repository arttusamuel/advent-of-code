

# Parse input string to an JSON object
# splits the "Game 2" into list of words and takes the second element
def parse_input_line(line):
    game_id, string = line.split(":")
    game_id = int(game_id.strip().split()[1]) 
    print("GameID: ", game_id)

    throws = string.strip().split(";") # Splits the string
    
    color_counts = {"id": game_id, "red": [], "green": [], "blue": []}

    # Iterate through different throws
    for throw in throws:
        # Split throw by comma and remove leading/trailing whitespace
        colors = throw.strip().split(",")
        print("Colors by throw after ',' split:", colors)
        # Iterate over color-value pairs
        for color_value in colors:
            value, color = color_value.strip().split()
            print("Trying to split color/value pair.", "color:", color, "value:", value)
            color_counts[f"{color}"].append(int(value))
            print("color_counts:", color_counts)

    return color_counts

# Opening the input file
try:
    red_limit = 12
    green_limit = 13
    blue_limit = 14

    games = {"games": []}

    with open("Day2/input-day2.txt", "r") as file:
        for line in file:
            
            game_data = parse_input_line(line)

            print("Trying to save processed line into games: ")

            game_id = game_data["id"]
            red_throws = game_data.get("red", [])
            green_throws = game_data.get("green", [])
            blue_throws = game_data.get("blue", [])
            game_info = {"id": game_id, "red": red_throws, "green": green_throws, "blue": blue_throws}
            games["games"].append(game_info)

        print(games)
except Exception as e:
    print(type(e))    # the exception type
    print(e.args)     # arguments stored in .args
    print(e)        
    


