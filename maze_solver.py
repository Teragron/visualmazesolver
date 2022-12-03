from matplotlib import pyplot

# Define the dimensions of the maze
MAZE_WIDTH = 10
MAZE_HEIGHT = 8

# Define the starting position of the robot
robot_x = 0
robot_y = 0

# Define the goal position
goal_x = 4
goal_y = 7

# Define the maze as a grid of booleans, where False represents a wall and
# True represents a free space
maze = [
    [True, True, True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, False, False, True],
    [True, False, True, True, False, True, True, True, False, True],
    [True, False, True, False, False, False, False, True, False, True],
    [True, False, True, False, True, True, False, True, False, True],
    [True, False, True, False, True, False, False, True, False, True],
    [True, False, True, True, True, False, True, True, False, True],
    [True, True, True, True, True, True, True, True, True, True]
]

# Initialize a new figure with pyplot.figure



# Define the robot's direction
# 0 = North, 1 = East, 2 = South, 3 = West
direction = 0

# Define the robot's movement
# 1 = move forward, 0 = do not move
movement = 1

# Define the robot's memory
memory = []

# Define the maximum number of steps the robot should take before giving up
max_steps = 100

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
    
    print(f"Robot position: ({robot_x}, {robot_y}), direction: {direction}")
    fig = pyplot.figure()

    # Add a subplot to the figure
    ax = fig.add_subplot(111)

    # Plot the maze grid as an image on the subplot
    ax.imshow(maze, cmap="gray", interpolation="nearest", origin="upper")

    # Plot the robot as a red circle at its current position
    ax.plot(robot_x, robot_y, "ro")


    # Initialize a new figure with pyplot.figure
    fig = pyplot.figure()


    # Show the figure
    pyplot.show()
    step_count += 1
    
    # If the robot has reached the goal, print a success message
if check_goal(robot_x, robot_y):
    print(f"Robot position: ({robot_x}, {robot_y}), direction: {direction}")
    print(f"The robot has reached the goal in {step_count} steps!")
# Otherwise, print a failure message
else:
    print(f"The robot failed to reach the goal after {max_steps} steps.")

