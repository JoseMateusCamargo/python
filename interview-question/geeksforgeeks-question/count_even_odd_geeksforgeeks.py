"""
@author: JMC
SOLUTION -> Count Even Odd (geeksforgeeks)

Example:
Input:
1
7
1 2 3 4 5 6 7

Output: 3 4

Explanation: In the given list, there are 3 even numbers (2, 4, 6) and 4 odd elements (1, 3, 5, 7).
"""


# User function Template for python3
# Function to count even and odd
# c_e : variable to store even count
# c_o : variable to store odd count

def count_even_odd(n, arr):
    pair = list()

    # Start code
    c_e = len([x for x in arr if x % 2 == 0])
    c_o = len([x for x in arr if x % 2 != 0])
    # Finish code

    pair.append(c_e)
    pair.append(c_o)
    return pair


# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while testcases > 0:
        # Size of array
        size_array = int(input())

        # Array elements input
        array = input().split()
        # Print (array)
        arr = list()
        for i in array:
            arr.append(int(i))

        # Print (arr)

        # Calling function to count even odd
        a = count_even_odd(size_array, arr)
        print(a[0], a[1])
        testcases -= 1


if __name__ == '__main__':
    main()
