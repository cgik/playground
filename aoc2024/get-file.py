import sys, requests

def get_input_file(day):
    url = "https://adventofcode.com/2024/day/" + day + "/input"

    with open("session.txt", "r") as f:
        session_token = f.read()
        cookies = {"session": session_token}

    r = requests.get(url, cookies=cookies)
    with open(day + "/" "input.txt", "w") as f:
        f.write(r.text)


if __name__ == "__main__":
    day_input = sys.argv[1]
    get_input_file(day_input)