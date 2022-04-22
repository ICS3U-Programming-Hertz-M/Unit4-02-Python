#!/usr/bin/env python3

# Created by: Hertz Antonella
# Created on: Arp-22-2022
# This program uses a do while loop and calculate the factorial


def main():
    # this function uses a do while loop
    loop_counter = 0
    factorial = 1
    # Ask the user to enter a whole number
    user_num = input(" Enter a whole number: ")
    print("")

    # calculate the factorio from 0 to the user number
    try:
        user_num_as_int = int(user_num)

        if user_num_as_int < 0:
            print("please enter a positive number..")
            exit()
        else:

            while True:
                loop_counter = loop_counter + 1
                print("Tracking {} time through loop.".format(loop_counter))
                factorial = factorial * loop_counter
                if loop_counter >= user_num_as_int:
                    break
            print("{}! = is {}".format(user_num_as_int, factorial))

    except:
        print("")
        print("invalid input")
        exit()


if __name__ == "__main__":
    main()
