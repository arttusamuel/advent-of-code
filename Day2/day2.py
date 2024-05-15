# Parse input string to an JSON object
# splits the "Game 2" into list of words and takes the second element
def parse_input_line(line):
    game_id, string = line.split(":")
    game_id = int(game_id.strip().split()[1]) 
    throws = string.strip().split(";") # Splits the string
    color_counts = {"id": game_id, "red": [], "green": [], "blue": []}

    # Iterate through different throws
    for throw in throws:
        # Split throw by comma and remove leading/trailing whitespace
        colors = throw.strip().split(",")
        # Iterate over color-value pairs
        for color_value in colors:
            value, color = color_value.strip().split()
            color_counts[f"{color}"].append(int(value))

    return color_counts

# Converting all input data to better format -> returning a JSON dict
def save_data_to_json():
    try:
        games = {"games": []}

        with open("Day2/input-day2.txt", "r") as file:
            for line in file:
                
                game_data = parse_input_line(line)
                game_id = game_data["id"]
                red_throws = game_data.get("red", [])
                green_throws = game_data.get("green", [])
                blue_throws = game_data.get("blue", [])
                game_info = {"id": game_id, "red": red_throws, "green": green_throws, "blue": blue_throws}
                games["games"].append(game_info)
        return games
    
    except Exception as e:
        print(type(e))    # the exception type
        print(e.args)     # arguments stored in .args
        print(e)        

def sum_of_ids():
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    games = save_data_to_json()
    sum_of_ids = 0

    for data_list in games["games"]:
        print("Red max:", max(data_list["red"]))
        print("Green max:", max(data_list["green"]))
        print("Blue max:", max(data_list["blue"]))

        if red_limit >= max(data_list["red"]) and green_limit >= max(data_list["green"]) and blue_limit >= max(data_list["blue"]):
            sum_of_ids += data_list["id"]
    return sum_of_ids

result = sum_of_ids()
print("Result for the advent of code 2023 day2 is:")
print(result)