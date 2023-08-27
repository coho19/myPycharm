# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# the usual way of printing out
print("hi pycharm, a newcomer here!")

# another way of printing out

# import the greet() function from the library.py file and executing it inside the main() function
# now the def-structure starts making sense
# it can call functions from elsewhere
# so that create a bigger and more adjustable structure
from library import greet
def main():
    # print("Hi, how do you do?")
    greet()

if __name__=='__main__':
    main()
# don't know why it is this
# it says it will be useful when running more than one py files
