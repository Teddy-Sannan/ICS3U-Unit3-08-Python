#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This program determines if a year
#  is a leap year


def main():
    while True:
        try:
            # calculates if year is a leap year
            # input
            year = int(input("Please enter a year: "))
            print()

            # process and output
            if year % 4 == 0 and year % 100 != 0:
                print("It is a leap year")
            if year % 4 != 0:
                print("It is not a leap year")
            if year % 4 == 0 and year % 100 == 0:
                if year % 400 != 0:
                    print("It is not a leap year")
                if year % 400 == 0 and year % 100 == 0:
                    print("It is a leap year")

        # prevents crashing
        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        # breaks out of loop
        else:
            break


if __name__ == "__main__":
    main()
