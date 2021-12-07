
f = open('inputs/input.txt', 'r')
lanternfish = f.read()
f.close()

lanternfish = [int(curr_fish) for curr_fish in lanternfish.split(',')]

num_days = 80

print(f'Initial Input: {lanternfish}')

for day_idx in range(num_days):

    for fish_idx in range(len(lanternfish)):
        
        if lanternfish[fish_idx] == 0:
            lanternfish.append(8)
            lanternfish[fish_idx] = 6
        else:
            lanternfish[fish_idx] = (lanternfish[fish_idx] - 1)

    print(f'Day: {day_idx + 1}, Number of fish: {len(lanternfish)}')
