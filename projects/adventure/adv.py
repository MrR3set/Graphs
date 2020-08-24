from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Utils
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
directions={"n":"s","s":"n","e":"w","w":"e"}
path = []
visited = {}
visited[player.current_room.id] = player.current_room.get_exits()


while len(visited) < len(room_graph):
    if player.current_room.id not in visited:

        visited[player.current_room.id] = player.current_room.get_exits()
        # Removed the path we came in
        last_dir = path[-1]
        visited[player.current_room.id].remove(last_dir)

    while len(visited[player.current_room.id])<1 and len(path)>0:
        # After we visited all the neighboring rooms we must go back on our path until we go back to room with still un visited rooms
        last_dir = path.pop()
        traversal_path.append(last_dir) 
        player.travel(last_dir)
        
    if len(visited[player.current_room.id])>0:
        nextRoom = visited[player.current_room.id].pop(0) 
    # Take out the following room (n,s,w,e) and add it to the traversal path and also to the path. 
    traversal_path.append(nextRoom)
    path.append(directions[nextRoom])
    player.travel(nextRoom)
    

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
