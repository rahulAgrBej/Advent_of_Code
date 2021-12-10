
f = open('inputs/input.txt', 'r')
lanternfish = f.read()
f.close()

num_days = 256

lanternfish = [int(curr_fish) for curr_fish in lanternfish.split(',')]

curr_fish_counts = []
for i in range(9):
    curr_fish_counts.append(0)

print(lanternfish)
print(curr_fish_counts)

# initial counts
for i in range(len(lanternfish)):
    curr_idx_counter = lanternfish[i]
    curr_fish_counts[curr_idx_counter] += 1

print(f'Day 0: {curr_fish_counts}')

for day_idx in range(num_days):

    # update fish counters for a given day
    update_counter = curr_fish_counts[8]
    for counter_idx in reversed(range(8)):
        
        prev_counter = curr_fish_counts[counter_idx]
        curr_fish_counts[counter_idx] = update_counter

        if counter_idx == 0:
            curr_fish_counts[6] += prev_counter
            curr_fish_counts[8] = prev_counter

        update_counter = prev_counter
    
    print(f'Day {1 + day_idx}: {curr_fish_counts}')

total_fish = 0
for idx in range(len(curr_fish_counts)):
    total_fish += curr_fish_counts[idx]

print(f'Total Fish: {total_fish}')
