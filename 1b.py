with open('input.txt') as f:

    # create a list to store all input values
    elf_calories = []

    for line in f.readlines():
        if line.strip() != '':
            cals = int(line.strip())
            elf_calories.append(cals)
        else:
            elf_calories.append(line.strip())

    print(elf_calories)

    # store the total calories carried by each elf
    caloric_sums = []
    temp_sum = 0

    for item in elf_calories:
        if item != '':
            temp_sum += item
        elif item == '':
            caloric_sums.append(temp_sum)
            temp_sum = 0

    print(caloric_sums)

    # find the list containing the max calories, then eliminate that sum
    max1 = 0

    for sum in caloric_sums:
        if sum > max1:
            max1 = sum

    print(max1)

    # find the list containing the second most calories, then eliminate that sum
    max2 = 0

    for sum in caloric_sums:
        if sum == max1:
            pass
        elif sum > max2:
            max2 = sum

    print(max2)

    # find the list containing the third most calories
    max3 = 0

    for sum in caloric_sums:
        if sum == max1:
            pass
        elif sum == max2:
            pass
        elif sum > max3:
            max3 = sum

    print(max3)

    total_max = max1 + max2 + max3

    print(total_max)

f.close()
