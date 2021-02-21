#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])

    # start on the right and find the first digit
    # that is smaller than the digit next to it

    for i in range (n-1,0,-1):
        if number[i] > number[i-1]:
            break
    # if no greater number is possible, print -1
    if i == 1 and number[i] <= number[i-1]:
        print -1
        return
    # find the smallest digit on the right side of
    # (i-1)'th digit that is greater than number [i-1]
    x = number[i-1]
    smallest = i
    for j in range(i+1,n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j

    #swap the smallest digit found above with (i-1)
    number[smallest],number[i-1] = number[i-1], number[smallest]

    # x is the final number
    x = 0
    # convert the list up to i-1 into number
    for j in range(i):
        x = x * 10 + number[j]

    # sort the digits after i-1 in ascending order
    number = sorted(number[i:])
    # convert the remaining sorted digits into the number
    for j in range(n-i):
        x = x * 10 + number[j]


def next_biggest_number(num):
    #TODO: Implement me!
    return 0

if __name__ == "__main__":
    main()



