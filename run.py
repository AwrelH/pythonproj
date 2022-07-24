# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
fahr = 'fahrenheit'
cel = 'celcius'
global option_value

def degrees():
    """
    Function to convert celcius to fahrenheit and vice versa.
    """
    print('You have choosen the degrees option')
    print('What do you wish to convert? (Fahrenheit or (C)elcius?')
    option = str(input('enter you option: '))
    if option == 'F':
        option_value = int(input('Write down your temperature:\n'))
        celcius_value = round((option_value-32) * 5 / 9, 1)
        print(f'You value of {option_value}F equals {celcius_value} degrees Celcius')
        new_values = input('Do you wish to try a new value, press (Y) or (N) to go back to Start')
        if new_values == 'Y':
            degrees()
        if new_values == 'N':
            welcome()
    if option == 'C':
        option_value = int(input('Write down your temperature:\n'))
        fahrenheit_value = round((option_value*1.8) + 32, 1)
        print(f'You value of {option_value}C equals {fahrenheit_value} degrees Fahrenheit')
        new_values = input('Do you wish to try a new value,\npress (Y) or (N) to go back to Start')
        if new_values == 'Y':
            degrees()
        if new_values == 'N':
            welcome()


def welcome():
    """
    Print welcome message
    """
    message = """welcome to converter!\n
    convert values:\n
    1 = celcius/fahrenheit\n
    2 = meters/feet\n
    3 = kilogram/pound\n
    4 = liters/us gallons\n
    make your choice my entering on of the obove(1-4) options.
    """
    print(message)
    choice = int(input())
    if choice == 1:
        degrees()
# def main():


welcome()