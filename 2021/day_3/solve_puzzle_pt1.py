
f = open('inputs/input.txt')
nums = f.readlines()
f.close()

nums = [num.rstrip('\n') for num in nums]

counters = [0] * len(nums[0])

for num in nums:
    for bit_idx in range(len(num)):
        bit = num[bit_idx]
        if bit == '1':
            counters[bit_idx] += 1
        else:
            counters[bit_idx] -= 1

gamma_rate_binary = ''
epsilon_rate_binary = ''

print(counters)

for bit_counter in counters:

    final_bit = ''

    if bit_counter > 0:
        gamma_final_bit = '1'
        epsilon_final_bit = '0'
    else:
        gamma_final_bit = '0'
        epsilon_final_bit = '1'
    
    gamma_rate_binary = gamma_rate_binary + gamma_final_bit
    epsilon_rate_binary = epsilon_rate_binary + epsilon_final_bit

print(f'Gamma Rate Binary: {gamma_rate_binary}')

gamma_rate = int(gamma_rate_binary, 2)

print(f'Gamma Rate: {gamma_rate}')

epsilon_rate = int(epsilon_rate_binary, 2)

print(f'Epsilon Rate: {epsilon_rate}')

print(f'Product of Gamma and Epsilon rates: {gamma_rate * epsilon_rate}')
