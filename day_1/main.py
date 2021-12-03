def main():
    count = 0
    with open("input.txt", "r") as f:
        last_num = -1
        for line in f:
            if last_num == -1:
                last_num = int(line)
                continue
            
            if int(line) > last_num:
                count += 1

    print(count)

if __name__ == "__main__":
    main()