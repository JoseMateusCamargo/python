"""
@author: JMC
SOLUTION -> Average Min Max (geeksforgeeks)

Example:
Input:
1
5
6 4 8 12 3

Output: 6

Explanation: Minimum element in the list is 3 and maximum is 12, so average excluding min and max is 18/3 = 6.
"""


# Function to calculate average

def calc_average(nums):
    return int(
        (sum(nums) - min(nums) - max(nums)) / (len(nums) - 2))  # soma elementos da lista - max e min e / pela media


# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while testcases > 0:
        size_arr = int(input())

        a = input().split()
        arr = list()

        for i in range(0, size_arr, 1):
            arr.append(int(a[i]))

        print(calc_average(arr))

        testcases -= 1


if __name__ == '__main__':
    main()
