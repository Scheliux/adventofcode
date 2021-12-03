def main():
    pos_x = 0
    pos_y = 0
    aim = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.split(" ")
            print(line)

            if line[0] == "forward":
                pos_x += int(line[1])
                pos_y += aim * int(line[1])
            elif line[0] == "down":
                aim += int(line[1])
            elif line[0] == "up":
                aim -= int(line[1])
    print(f"{pos_x}, {pos_y}")
    print(str(pos_x * pos_y))

if __name__ == "__main__":
    main()