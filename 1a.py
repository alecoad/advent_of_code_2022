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

    # find the list containing the max calories
    max = 0

    for sum in caloric_sums:
        if sum > max:
            max = sum

    print(max)

f.close()
