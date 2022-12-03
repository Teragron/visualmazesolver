from matplotlib import pyplot
import random

# Define the dimensions of the maze
MAZE_WIDTH = 10
MAZE_HEIGHT = 10


maze = []
for _ in range(MAZE_HEIGHT):
    maze.append([True] * MAZE_WIDTH)

# Randomly generate the walls and obstacles in the maze
for y in range(1, MAZE_HEIGHT - 1):
    for x in range(1, MAZE_WIDTH - 1):
        if random.random() < 0.3:
            maze[y][x] = False

# Define the starting position of the robot
# Choose a random starting position for the robot
found_start = False
while not found_start:
    robot_x = random.randint(0, MAZE_WIDTH - 1)
    robot_y = random.randint(0, MAZE_HEIGHT - 1)
    if maze[robot_y][robot_x] and (maze[robot_y - 1][robot_x] or maze[robot_y][robot_x - 1] or maze[robot_y][robot_x + 1] or maze[robot_y + 1][robot_x]):
        found_start = True

# Set the starting position of the robot
robot_x = robot_x
robot_y = robot_y



# Choose a random goal position
found_goal = False
while not found_goal:
    goal_x = random.randint(0, MAZE_WIDTH - 1)
    goal_y = random.randint(0, MAZE_HEIGHT - 1)
    if maze[goal_y][goal_x] and (robot_x, robot_y) != (goal_x, goal_y):
        found_goal = True

# Set the goal position
goal_x = goal_x
goal_y = goal_y

print("Starting Point:", (robot_x, robot_y))
print("Destination Point:", (goal_x, goal_y))


# Define the maze as a grid of booleans, where False represents a wall and
# True represents a free space


# Initialize a new figure with pyplot.figure



# Define the robot's direction
# 0 = North, 1 = East

direction = 0

# Define the robot's movement
# 1 = move forward, 0 = do not move
movement = 1

# Define the robot's memory
memory = []

# Define the maximum number of steps the robot should take before giving up
max_steps = 1000

# Define the current step count
step_count = 0

# Define a function to check if the robot has reached the goal
def check_goal(x, y):
    if x == goal_x and y == goal_y:
        return True
    else:
        return False

# Define a function to move the robot forward
def move_forward(x, y, d):
    if d == 0:
        # If the robot is facing north, decrement the y coordinate
        y -= 1
    elif d == 1:
        # If the robot is facing east, increment the x coordinate
        x += 1
    elif d == 2:
        # If the robot is facing south, increment the y coordinate
        y += 1
    elif d == 3:
        # If the robot is facing west, decrement the x coordinate
        x -= 1
    return x, y

# Define a function to turn the robot left
def turn_left(d):
    # Decrement the direction by 1, but wrap around if necessary
    d = (d - 1) % 4
    return d

# Define a function to turn the robot right
def turn_right(d):
    # Increment the direction by 1, but wrap around if necessary
    d = (d + 1) % 4
    return d

# Define a function to check if the space in front of the robot is free
def check_front(x, y, d):
    if d == 0:
        # If the robot is facing north, check the space above it
        if y > 0 and maze[y - 1][x]:
            return True
        else:
            return False
    elif d == 1:
        # If the robot is facing east, check the space to the right of it
        if x < MAZE_WIDTH - 1 and maze[y][x + 1]:
            return True
        else:
            return False
    elif d == 2:
        # If the robot is facing south, check the space below it
        if y < MAZE_HEIGHT - 1 and maze[y + 1][x]:
            return True
        else:
            return False
    elif d == 3:
        # If the robot is facing west, check the space to the left of it
        if x > 0 and maze[y][x - 1]:
            return True
        else:
            return False

# Main loop
while not check_goal(robot_x, robot_y) and step_count < max_steps:
    print(f"Robot position: ({robot_x}, {robot_y}), direction: {direction}")
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.imshow(maze, cmap="gray", interpolation="nearest", origin="upper")
    ax.plot(robot_x, robot_y, "ro")
    fig = pyplot.figure()
    pyplot.show()
    
    # If the robot is blocked and has not reached the goal, add its current
    # position to its memory
    if not check_front(robot_x, robot_y, direction) and not check_goal(robot_x, robot_y):
        memory.append((robot_x, robot_y))

    # If the robot can move forward, do so
    if check_front(robot_x, robot_y, direction):
        robot_x, robot_y = move_forward(robot_x, robot_y, direction)
    # Otherwise, turn left and try moving forward again
    else:
        direction = turn_left(direction)
        if check_front(robot_x, robot_y, direction):
            robot_x, robot_y = move_forward(robot_x, robot_y, direction)

    # Increment the step count
    

    
    step_count += 1
    
    # If the robot has reached the goal, print a success message
if check_goal(robot_x, robot_y):
    print(f"Robot position: ({robot_x}, {robot_y}), direction: {direction}")
    print(f"The robot has reached the goal in {step_count} steps!")
# Otherwise, print a failure message
else:
    print(f"The robot failed to reach the goal after {max_steps} steps.")

