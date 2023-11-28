import random

def generate_maze(size):
    maze = [["🌿" if random.random() < 0.3 else " " for _ in range(size)] for _ in range(size)]
    maze[0][0] = "🚶"  # Player
    maze[-1][-1] = "🏁"  # Finish
    return maze

def display_maze(maze):
    for row in maze:
        print(" ".join(row))

def navigate_maze(maze):
    while True:
        display_maze(maze)

        user_move = input("Enter your move (W/A/S/D, Q to quit): ").upper()

        if user_move == "Q":
            print("Quitting the maze.")
            break
        elif user_move in ("W", "A", "S", "D"):
            move_result = make_move(maze, user_move)
            if move_result == "E":
                print("Congratulations! You reached the end of the maze.")
                break
        else:
            print("Invalid move. Use W/A/S/D to move or Q to quit.")

def make_move(maze, direction):
    player_position = find_player(maze)
    x, y = player_position

    if direction == "W" and x > 0 and maze[x - 1][y] != "🌿":
        maze[x][y] = " "
        x -= 1
    elif direction == "A" and y > 0 and maze[x][y - 1] != "🌿":
        maze[x][y] = " "
        y -= 1
    elif direction == "S" and x < len(maze) - 1 and maze[x + 1][y] != "🌿":
        maze[x][y] = " "
        x += 1
    elif direction == "D" and y < len(maze[0]) - 1 and maze[x][y + 1] != "🌿":
        maze[x][y] = " "
        y += 1

    maze[x][y] = "🚶"

    if maze[x][y] == "🏁":
        return "E"
    else:
        return None


def find_player(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "🚶":
                return i, j

if __name__ == "__main__":
    maze_size = int(input("Enter the size of the maze: "))
    maze = generate_maze(maze_size)

    print("Welcome to the Emoji Maze Game! 🌟")
    navigate_maze(maze)
