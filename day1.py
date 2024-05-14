def get_calibration_value(string):
    char_array = []
    char_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    char1 = ""
    char2 = ""
    if (string != ""):
        while(char1 == ""):
            for char in string:
                for number in char_numbers:
                    if char == number:
                        char1 = char
        
        while(char2 == ""):
            for char in reversed(string):
                for number in char_numbers:
                    if char == number:
                        char2 = char
        
        char_array.append(char2)
        char_array.append(char1)
            
        return "".join(char_array)
    else:
        print("String is not valid")
        pass


def sum_of_calibrations():
    sum = 0
    try:
        with open("input.txt", "r") as file:
            for content in file:
                calibration_value = get_calibration_value(content.strip())
                print("Calibration value and type: ", calibration_value, type(calibration_value))
                sum += int(calibration_value)
                print(content)
            return sum
    except ValueError:
        print("String value not valid integer")
        return sum

print("Sum of calibrations is: ", sum_of_calibrations())