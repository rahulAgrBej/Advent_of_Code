

f = open('inputs/input.txt', 'r')
depths = f.readlines()
f.close()

# cleaning data set to be ints
depths = [int(depth.rstrip('\n')) for depth in depths]

num_larger = 0

for idx in range(len(depths))[:-3]:

    num_0 = depths[idx]
    num_1 = depths[idx + 3]

    if num_1 > num_0:
        num_larger += 1

print(f'Number of measurement groups that are larger than the previous measurement: {num_larger}')