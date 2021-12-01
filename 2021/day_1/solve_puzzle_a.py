
# read input
f = open('inputs/input_a.txt')
depths = f.readlines()
f.close()

# counter
num_larger = 0

for idx in range(len(depths)):

    # stripping input of new lines and casting to int
    prev_depth = int(depths[idx - 1].rstrip('\n'))
    curr_depth = int(depths[idx].rstrip('\n'))

    # updating counter
    if curr_depth > prev_depth:
        num_larger += 1

print(f'Number of measurements that are larger than the previous measurement: {num_larger}')