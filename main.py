# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#89CFF0",  # TODO: Choose color
        "head": "do-sammy",  # TODO: Choose head
        "tail": "do-sammy",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data



def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
    print(my_head)
    print(board_width)
    print(board_height)

    if my_neck["x"] < my_head["x"] :  # Neck is left of head, don't move left
        is_move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:  # Neck is right of head, don't move right
        is_move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:# Neck is below head, don't move down
        is_move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:  # Neck is above head, don't move up
        is_move_safe["up"] = False
    
   
    # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds
    if my_head["x"] == board_width - 1:  # Head is at the left edge of the board
        is_move_safe["right"] = False
    if my_head["x"] == 0:  # Head is at the right edge of the board
        is_move_safe["left"] = False
    if my_head["y"] == board_height - 1:  # Head is at the top edge of the board
        is_move_safe["up"] = False
    if my_head["y"] == 0:  # Head is at the bottom edge of the board
        is_move_safe["down"] = False    

    # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
# Prevent moving into the snake's own body
    # Prevent moving into the snake's own body
    my_body = game_state['you']['body']
    xBody = []
    yBody = []
    my_head = my_body[0]  # Head of the snake

    # Check all body segments except the tail (in case it moves away)
    for i in range(len(my_body)):
        if(my_body[i]["x"] == my_head['x']):
            xBody.append(my_body[i]) 

    for i in range(len(my_body)):
        if(my_body[i]["y"] == my_head['y']):
            yBody.append(my_body[i]) 
    for i in range(len(yBody)):
        if(yBody[i]["x"] - my_head['x'] == -1):
            is_move_safe["left"] = False
        if(yBody[i]["x"] - my_head['x'] == 1):
            is_move_safe["right"] = False
    for i in range(len(xBody)):
        if(xBody[i]["y"] - my_head['y'] == -1):
            is_move_safe["down"] = False
        if(xBody[i]["y"] - my_head['y'] == 1):
            is_move_safe["up"] = False

        



    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    # opponents = game_state['board']['snakes']

    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}

    # Choose a random move from the safe ones
    next_move = random.choice(safe_moves)
    print(safe_moves)
    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    food = game_state['board']['food']
    closestFood = food[0]
    for i in range(len(food)):
        if (abs(food[i]['x'] - my_head['x'] )+ abs(food[i]['y'] - my_head['y']) < abs(closestFood['x'] - my_head['x'] )+ abs(closestFood['y'] - my_head['y']) ):
            closestFood = food[i]
    
    distanceX = closestFood['x'] - my_head['x']
    distanceY = closestFood['y'] - my_head['y']
    direction = None
    if(abs(distanceX) > abs(distanceY)):
        if(distanceX):
            direction = 'left'
        else:
            direction = 'right'
    else:
        if(distanceY):
            direction = 'down'
        else:
            direction = 'up'
    if(game_state['you']['health'] < 30):
        next_move = direction
    elif(game_state['you']['health'] >= 30):
        closestFoodList = []
     #end HERE: sanger code lock in lfg 



    print(f"MOVE {game_state['turn']}: {next_move}")
    if "right" in safe_moves:
        return {"move": "right"}

    # If there are safe moves, select a move
    next_move = random.choice(safe_moves)
    print(safe_moves)
    print(f"MOVE {game_state['turn']}: {next_move}")

    return {"move": next_move}





# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
