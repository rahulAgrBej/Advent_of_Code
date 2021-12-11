
f = open('inputs/input.txt', 'r')
crab_subs = f.read()
f.close()

crab_subs = [int(crab_sub) for crab_sub in crab_subs.split(',')]
print(crab_subs)
crab_sub_counts = {}

max_sub = [0, 0]

for crab_sub in crab_subs:
    if not (crab_sub in crab_sub_counts):
        crab_sub_counts[crab_sub] = 0
    
    crab_sub_counts[crab_sub] += 1

    if crab_sub_counts[crab_sub] > max_sub[1]:
        max_sub[0] = crab_sub
        max_sub[1] = crab_sub_counts[crab_sub]

# calculates the fuel used to get to all positions
min_fuel_used = -1
min_sub_position = -1
for crab_sub_i in crab_sub_counts: # calculate cost for all subs to go to crab sub i
    curr_fuel_used = 0
    for crab_sub_j in crab_sub_counts:
        curr_fuel_used += (crab_sub_counts[crab_sub_j] * abs(crab_sub_j - crab_sub_i))
    
    if (curr_fuel_used < min_fuel_used) or (min_fuel_used == -1):
        min_fuel_used = curr_fuel_used
        min_sub_position = crab_sub_i

print(f'Min Fuel Used: {min_fuel_used}')
print(f'Min Crab Sub Position: {min_sub_position}')
