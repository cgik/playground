import sys

def process_file(file_input):
    array_of_numbers = []
    results = 0

    with open(file_input, "r") as f:
        for line in f:
            array_of_numbers.append(line.split())

    for i in range(len(array_of_numbers)):
        results += safe_and_unsafe(array_of_numbers[i])

    print(results)

def safe_and_unsafe(array_input):
    nums = [int(x) for x in array_input]
    if nums[1] - nums[0] > 0:
        direction = "asc"
    elif nums[1] - nums[0] < 0:
        direction = "desc"
    else:
        return 0

    mistakes = 0

    for i in range(len(nums)-1):

        diff = nums[i+1] - nums[i]

        if direction == "asc":
            if diff > 3 or diff <= 0:
                mistakes += 1
        if direction == "desc":
            if diff >= 0 or diff < -3:
                mistakes += 1

    if mistakes > 0:
        return 0

    # print(f"Like the others {array_input}")
    return 1

if __name__ =="__main__":
    file = sys.argv[1]
    process_file(file)