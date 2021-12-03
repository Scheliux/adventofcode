def main():
    count = 0
    with open("input.txt", "r") as f:
        nums = []
        last_sum = -1
        for line in f:
            if len(nums) < 3:
                nums.append(int(line))
            
            if len(nums) == 3:

                if last_sum == -1:
                    print(str(nums) + " : " + str(sum(nums)))
                    last_sum = sum(nums)
                    del(nums[0])
                    continue
                
                if sum(nums) > last_sum:
                    count += 1
                    print(str(nums) + " : " + str(sum(nums)) + " increased")
                else:
                    print(str(nums) + " : " + str(sum(nums)))

                last_sum = sum(nums)
                del(nums[0])
    
    print(count)

if __name__ == "__main__":
    main()