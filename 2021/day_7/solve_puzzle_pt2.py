
f = open('inputs/input.txt', 'r')
crab_subs = f.read()
f.close()

crab_subs = [int(crab_sub) for crab_sub in crab_subs.split(',')]
crab_sub_counts = {}

max_crab_loc = -1
max_sub = [0, 0]

for crab_sub in crab_subs:
    if not (crab_sub in crab_sub_counts):
        crab_sub_counts[crab_sub] = 0
    
    crab_sub_counts[crab_sub] += 1

    if crab_sub_counts[crab_sub] > max_sub[1]:
        max_sub[0] = crab_sub
        max_sub[1] = crab_sub_counts[crab_sub]
    
    if max_crab_loc < crab_sub:
        max_crab_loc = crab_sub

# calculates the fuel used to get to all positions
min_fuel_used = -1
min_sub_position = -1

for possible_loc in range(max_crab_loc):
    curr_fuel_used = 0
    for crab_sub_i in crab_sub_counts:
        dist = abs(crab_sub_i - possible_loc)
        gaussian_sum = (dist * (dist + 1)) / 2
        curr_fuel_used += (crab_sub_counts[crab_sub_i] * gaussian_sum)

    #print(f'Cost of Moving to {possible_loc} is {curr_fuel_used}')

    if (curr_fuel_used < min_fuel_used) or (min_fuel_used == -1):
        min_fuel_used = curr_fuel_used
        min_sub_position = possible_loc

print(f'Min Fuel Used: {min_fuel_used}')
print(f'Min Crab Sub Position: {min_sub_position}')
