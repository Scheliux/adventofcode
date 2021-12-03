def binaryToDecimal(binary):
    result = 0
    binary = binary[::-1]

    for i, bit in enumerate(binary):
        result += 2 ** i * int(bit)
    
    return result

def task1():
    gamma_binary = ""
    epsilon_binary = ""
    counts = []

    with open("input.txt", "r") as f:
        for line in f:
            if len(counts) == 0:
                for bit in line[:-1]:
                    counts.append(0)
            
            for i, bit in enumerate(line[:-1]):
                if bit == '1':
                    counts[i] += 1
                else:
                    counts[i] -= 1

    print(counts)

    for i in counts:
        if i > 0:
            gamma_binary += "1"
            epsilon_binary += "0"
        else:
            gamma_binary += "0"
            epsilon_binary += "1"
            
    print(gamma_binary)
    print(epsilon_binary)

    gamma = binaryToDecimal(gamma_binary)
    epsilon = binaryToDecimal(epsilon_binary)

    print(gamma)
    print(epsilon)

    print(f"gamma * epsilon = {gamma * epsilon}")

def task2():
    oxygen = 0
    co2 = 0

    with open("input.txt", "r") as f:
        nums = f.read()
        nums = nums.split("\n")
        nums = nums[:-1]

        i = 0
        while len(nums) > 1 and i < len(nums[0]):
            count_ones = 0
            count_zeros = 0

            for num in nums:
                if num[i] == "1":
                    count_ones += 1
                else:
                    count_zeros += 1

            print(f"{count_zeros}, {count_ones}, {i}")
            if count_ones < count_zeros:
                nums = list(filter(lambda x : x[i] == "0", nums))
            else:
                nums = list(filter(lambda x : x[i] == "1", nums))

            i += 1
            print(nums)
        
        oxygen = binaryToDecimal(nums[0])
        
    with open("input.txt", "r") as f:
        nums = f.read()
        nums = nums.split("\n")
        nums = nums[:-1]

        i = 0
        while len(nums) > 1 and i < len(nums[0]):
            count_ones = 0
            count_zeros = 0

            for num in nums:
                if num[i] == "1":
                    count_ones += 1
                else:
                    count_zeros += 1

            print(f"{count_zeros}, {count_ones}, {i}")
            if count_ones < count_zeros:
                nums = list(filter(lambda x : x[i] == "1", nums))
            else:
                nums = list(filter(lambda x : x[i] == "0", nums))

            i += 1
            print(nums)
        
        co2 = binaryToDecimal(nums[0])

    print(f"oxygen * CO2 = {oxygen * co2}")
            

if __name__ == "__main__":
    task2()