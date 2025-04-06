import os
import sys

def combine_logs_process_file(file_input):
    # f = open(file_input, "r")
    with open(file_input, "r") as f:
        left = []
        right = []

        for line in f:
            split_lines = line.split()

            if split_lines:
                left.append(int(split_lines[0]))
                right.append(int(split_lines[1]))

        left.sort()
        right.sort()

        # f.close()

        print(diff_between_lists(left, right))
        print(similarity_score(left, right))

def diff_between_lists(arr1, arr2):
    total = []

    for i in range(len(arr1)):
        totaled = abs(arr1[i] - arr2[i])
        total.append(totaled)

    return sum(total)

def similarity_score(arr1, arr2):
    total = []
    total_values = {}

    for i in set(arr2):
        total_values[i] = arr2.count(i)

    # return total_values[32788]
    for x in range(len(arr1)):
        multiply_by = total_values.get(arr1[x], 0)
        if multiply_by != 0:
            totaled = multiply_by * arr1[x]
            total.append(totaled)

    return sum(total)

if __name__ == "__main__":
    file = sys.argv[1]
    combine_logs_process_file(file)