# The engine schematic (your puzzle input) consists of a visual representation of the engine. 
# There are lots of numbers and symbols you don't really understand, but apparently any number 
# adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
# (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
# 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; 
# their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
# Task is to count sum of all integers that has a symbol other than a '.' adjacent to it.

# Test matrix
test_matrix = [
['#', '.', '.' , '.', '#', '.' '.', '.'],
['.', '.', '.', '1', '.', '.' '.', '.'],
['.', '.', '.', '.', '.', '.' '.', '#'],
['.', '.', '.', '.', '.', '.' '.', '.'],
['.', '2', '.', '3', '3', '3', '.', '.'],
['.', '.', '.', '.', '#', '.' '.', '.'],
['.', '4', '4', '#', '.', '.' '#', '.'],
['.', '.', '.', '.', '.', '.' '5', '.']
]

# Not in use at the moment
def create_matrix(x, y):
    matrix = [[0]*y for _ in range(x)]
    if x % 2 == 1:
        middle_row_index = x // 2
        middle_row = matrix[middle_row_index]
        middle_row[0:1] = [-1]
        middle_row[-1:] = [1]
        middle_row[1:-1] = [0] * (y-2)

# Creates a row (list) where 0's take integers place 
def create_matrix_row(y):
    row = [0]*y
    row[0:1] = [-1]
    row[-1:] = [1]
    row[1:-1] = [0] * (y-2)
    return row

# Testing matrix and row formation
create_matrix(3,5)
create_matrix_row(5)

# Format input data to a matrix -- Should work --
def format_to_matrix():
    data = []
    try:
        with open('Day3/test_data.txt', "r") as file:
            lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                char_list = list(line)
                char_list.insert(0, '.') # Additional dot to first element
                char_list.insert(-1, '.') # Additional dot to last element
                data.append(char_list)

            data.insert(0, ['.'] * len(char_list)) # Additional dot -row to first element
            data.append(['.'] * len(char_list)) # Additional dot -row to last element
            print("\nData input:\n", data)
        return data
    except Exception as e:
        print("Unexpected", e)
    return 

# Setting all integers that are not adjacent to a non '.' symbol
def sum_values_with_adjacents(input_matrix):
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    sum = 0

    for i in range(rows):
        for j in range(cols):
            if input_matrix[i][j].isdigit():
                # Check neighbours
                # Checking integer length since input is by chars
                int_len = 1
                int_string = input_matrix[i][j]

                # Catches indexError, but program doesn't process integers on the edges
                try:
                    while(input_matrix[i][j+int_len].isdigit()):
                        int_string += input_matrix[i][j+int_len]
                        int_len += 1               
                        print("int_string :", int_string) # Seems to work properly
                except IndexError as e:
                    print("An IndexError occurred:", "e")
                    continue

                # Create a matrix of neigbours to check, takes influence of a "convolution" type processing. 
                neighbours_row = create_matrix_row(int_len+2) # Matrix row with int placed with 1's
                print(neighbours_row)
                add_sum = False # Change to True when sum needs to be counted
                for di in [-1, 0, 1]:
                    for dj in neighbours_row:
                        if di == 0 and dj == 0:
                            print("di and dj at 0, on top of integer to be summed")
                            continue  # Skip the current element
                        x = i + di                        
                        y = j + dj
                        print(f"Row {i} column {j}. Neighbour matrix Row {di} column {dj}.")
                        print(f"Setting x {x} and y {y}.")

                        if 0 <= x < rows and 0 <= y < cols: # Prevents index out of bounds
                            if input_matrix[x][y] == '.':
                                print(f"input_matrix({x},{y}) is '.'")
                            if input_matrix[x][y] != '.':
                                print(f"input_matrix({x},{y}) not '.', sum the value.")
                                add_sum = True
                                break
                            
                # When symbol is noticed -> add_sum is True -> adds int_string to sum
                if add_sum == True:
                    print("\nTo be summed: ", int_string, "\n")
                    sum += int(int_string) # Add value to sum
                    add_sum = False
                    break
    return sum

real_matrix = format_to_matrix()
answer = sum_values_with_adjacents(real_matrix)
print(answer)
