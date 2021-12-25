
from os import get_terminal_size


def read_data(file_path):

    # reading in data file
    f = open(file_path, 'r')
    data = f.readlines()
    f.close()

    in_signals = []
    out_signals = []

    for line in data:
        line = line.rstrip('\n')

        # separate input from output signals
        curr_in_sigs, curr_out_sigs = line.split(' | ')
        curr_in_sigs = curr_in_sigs.split(' ')
        curr_out_sigs = curr_out_sigs.split(' ')

        # collecting current input and output signals
        in_signals.append(curr_in_sigs)
        out_signals.append(curr_out_sigs)
    
    return in_signals, out_signals

# separates letters that are shared and different between two strings
def diff_letters(in_0, in_1):

    different_letters = []

    if len(in_1) > in_0:
        temp = in_0
        in_0 = in_1
        in_1 = temp
    
    for letter_idx in range(len(in_0)):
        
        if letter_idx > (len(in_1) - 1):
            different_letters.append(in_0[letter_idx])
            continue

        if in_0[letter_idx] != in_1[letter_idx]:
            different_letters.append(in_0[letter_idx])
        else:
            same_letters.append()

    
    return None

def decode_digits(in_signals, out_signals):

    real_digits = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9
    }
    
    encoded_digits = {}

    decoded_digits = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: ''
    }

    letter_translation = {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': ''
    }

    curr_letter_freqs = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0
    }
    
    # get current letter frequencies
    for in_sig in in_signals:
        for letter in in_sig:
            curr_letter_freqs[letter] += 1

        if len(in_sig) == 2:
            decoded_digits[1] = sorted(in_sig)
        elif len(in_sig) == 4:
            decoded_digits[4] = sorted(in_sig)
        elif len(in_sig) == 3:
            decoded_digits[7] = sorted(in_sig)
        elif len(in_sig) == 7:
            decoded_digits[8] == sorted(in_sig)

    d_g_potential = []
    
    for letter in curr_letter_freqs:
        if curr_letter_freqs[letter] == 6: # case for b
            letter_translation[letter] = 'b'
        elif curr_letter_freqs[letter] == 4: # case for e
            letter_translation[letter] = 'e'
        elif curr_letter_freqs[letter] == 9: # case for f
            letter_translation[letter] = 'f'

            # now finding c
            if letter == decoded_digits[1][0]:
                c_translate = decoded_digits[1][1]
            else:
                c_translate = decoded_digits[1][0]
            
            letter_translation[c_translate] = 'c'

            # now finding a
            potential_a = []
            for letter in curr_letter_freqs:
                if curr_letter_freqs[letter] == 8:
                    potential_a.append(letter)
            
            if c_translate == potential_a[0]:
                a_translate = potential_a[1]
            else:
                a_translate = potential_a[0]
            
            letter_translation[a_translate] = 'a'
        elif curr_letter_freqs[letter] == 7:
            d_g_potential.append(letter)
    
    if d_g_potential[0] in decoded_digits[4]:
        d_translate = d_g_potential[0]
        g_translate = d_g_potential[1]
    else:
        d_translate = d_g_potential[1]
        g_translate = d_g_potential[0]
    
    letter_translation[d_translate] = 'd'
    letter_translation[g_translate] = 'g'

    for in_sig in in_signals:
        decoded_signal = ''
        for letter in in_sig:
            decoded_signal += letter_translation[letter]
        
        decoded_signal = ''.join(sorted(decoded_signal))
        encoded_signal = ''.join(sorted(in_sig))
        
        encoded_digits[encoded_signal] = real_digits[decoded_signal]
    
    final_num = ''
    for out_sig in out_signals:
        out_sig = ''.join(sorted(out_sig))
        final_num += str(encoded_digits[out_sig])
    
    return int(final_num)

in_signals, out_signals = read_data('inputs/input.txt')


total = 0
for signal_idx in range(len(in_signals)):
    total += decode_digits(in_signals[signal_idx], out_signals[signal_idx])

print(f'Total: {total}')