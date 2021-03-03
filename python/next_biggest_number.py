#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])

def next_biggest_number(num):
    #TODO: Implement me!
    # first convert the int to a string
    num = str(num)
    # start on the right and find the first digit
    # that is smaller than the digit next to it
    for i in range (len(num)-1,0,-1):
        if num[i] > num[i-1]:
            break
    # if no greater number is possible, print -1
    if i == 1 and num[i] <= num[i-1]:
        print -1
        return
    # find the smallest digit on the right side of
    # (i-1)'th digit that is greater than number [i-1]
    x = num[i-1]
    smallest = i
    for j in range(i+1,len(num)):
        if num[j] > x and num[j] < num[smallest]:
            smallest = j


    #swap the smallest digit found above with (i-1)
    num[smallest],num[i-1] = num[i-1], num[smallest]

    # x is the final number
    x = 0
    # convert the list up to i-1 into number
    for j in range(i):
        x = x * 10 + num[j]

    # sort the digits after i-1 in ascending order
    num = sorted(num[i:])
    num = str(num)
    # convert the remaining sorted digits into the number
    for j in range(len(num)-i):
        x = x * 10 + num[j]
    num = int(num)
    return 0

if __name__ == "__main__":
    main()



