
# function to decide what subset of numbers to continue with
def decision_subset_branch(rating_type, bit_counter, subsetted_nums):

    nums = []

    if rating_type == 'o2':

        # update nums list based on most common bit criteria
        if bit_counter >= 0:
            nums = subsetted_nums['1']
        else:
            nums = subsetted_nums['0']
    elif rating_type == 'co2':

        if bit_counter >= 0:
            nums = subsetted_nums['0']
        else:
            nums = subsetted_nums['1']
    else:
        print('Unknown rating type')

    return nums

# find rating based on a criteria provided
def find_rating(all_nums, decision_criteria):

    # dictionary keeping record of nums starting with 1's or 0;s
    subsetted_nums = {}
    subsetted_nums['1'] = []
    subsetted_nums['0'] = []

    # finding oxygen generator rating
    # most common bit criteria
    bit_idx = 0
    bit_counter = 0
    nums = all_nums

    while len(nums) > 1:
        # find most common bit for a specific bit index
        for num in nums:
            if num[bit_idx] == '1':
                bit_counter += 1
                subsetted_nums['1'].append(num)
            else:
                bit_counter -= 1
                subsetted_nums['0'].append(num)

        bit_idx += 1
        
        # update nums list based on most common bit criteria
        nums = decision_subset_branch(decision_criteria, bit_counter, subsetted_nums)

        # zero out bit counter and currently subsetted data
        bit_counter = 0
        subsetted_nums['1'] = []
        subsetted_nums['0'] = []
        
    rating = int(nums[0], 2)
    
    return rating

f = open('inputs/input.txt')
all_nums = f.readlines()
f.close()

all_nums = [num.rstrip('\n') for num in all_nums]

# Oxygen Generator Rating
o2_rating = find_rating(all_nums, 'o2')
print(f'O2 Generator Rating: {o2_rating}')

# Carbon Scrubber Rating
co2_rating = find_rating(all_nums, 'co2')
print(f'Carbon Dioxide Scrubber Rating: {co2_rating}')

print(f'Product of both ratings: {o2_rating * co2_rating}')
