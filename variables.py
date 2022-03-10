#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# Global and local variables

# global variable
variable_X = 25


def local_variable():

    # this shows local variables
    variable_X = 10
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print(
        "Local variable_X, variable_Y, variable_Z: {0} + {1} = {2}".format(
            variable_X, variable_Y, variable_Z
        )
    )


def global_variable():
    # this shows global variables
    global variable_X
    variable_X = variable_X + 1
    variable_Y = 30
    variable_Z = variable_X + variable_Y
    print(
        "Global variable_X, variable_Y, variable_Z: {0} + {1} = {2}".format(
            variable_X, variable_Y, variable_Z
        )
    )


def main():
    # this function shows local and global variables
    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
