from math import gcd
from collections import Counter

# Function to identify 3-character pairs in the input text
def find_3_char_pairs(input_str):
    found = set()  # Set for found 3-character pairs
    found_frequency = []  # List for frequencies of occurrences

    # Loop through the string for 3-character pairs
    for i in range(len(input_str) - 2):
        current_3_char_pair = input_str[i: i + 3]

        # Check if the pair has already been found
        if current_3_char_pair not in found:
            found.add(current_3_char_pair)
            found_frequency.append(1)

            # Count occurrences
            found_frequency[-1] += input_str[i + 3:].count(current_3_char_pair)

    # Remove single occurrences
    found = [pair for pair, frequency in zip(found, found_frequency) if frequency != 1]

    return found

# Function to calculate distances between found 3-character pairs
def calculate_distances(input_str, found_pairs):
    distances = set()  # Set to ensure unique distances
    for pair in found_pairs:
        positions = [pos for pos, char in enumerate(input_str) if input_str[pos:pos+3] == pair]
        if len(positions) > 1:  # Only if the pair occurs more than once
            distances.update([positions[i+1] - positions[i] for i in range(len(positions)-1)])

    # Sort distances and return
    sorted_distances = sorted(distances)
    return sorted_distances

# Function to find divisors of a number, excluding 1 and 2
def find_divisors_without_1_2(number):
    divisors = []
    for i in range(3, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Function to find common divisors and their frequencies
def find_divisors_and_frequencies(numbers):
    common_divisor = gcd(*numbers)

    divisors_and_frequencies = Counter()

    # Iterate through the numbers for divisors
    for number in numbers:
        divisors = find_divisors_without_1_2(number)
        divisors_and_frequencies.update(divisors)

    # Ignore divisors 1 and 2
    del divisors_and_frequencies[1]
    del divisors_and_frequencies[2]

    # Split divisors and frequencies into two lists
    divisors_list, frequencies_list = zip(*[(t, h) for t, h in divisors_and_frequencies.items() if h != 1])

    # Sort the lists by frequency
    sorted_lists = sorted(zip(frequencies_list, divisors_list), reverse=False)
    frequencies_list, divisors_list = zip(*sorted_lists)

    return divisors_list, frequencies_list

# Function to split the text according to the key length
def split_input_text(key_length, input_str):
    input_split = [""] * key_length

    # Split the input text according to the key length
    for i in range(len(input_str)):
        index = i % key_length
        input_split[index] += input_str[i]

    input_split = [part for part in input_split if part]
    return input_split

# Function for Caesar decryption
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                # Calculate decrypted character for uppercase letters
                decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                # Calculate decrypted character for lowercase letters
                decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Function to find the most probable shift for Caesar decryption
def find_most_probable_shift(text):
    alphabet_table = []

    # Create a table with the alphabet for calculating letter probabilities
    for char in range(ord('A'), ord('Z') + 1):
        alphabet_table.append([chr(char)])
    
    # Probabilities for the frequency of letters in English
    letter_probability = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.09, 6.03, 6.73, 8.94, 2.52, 1.01, 1.39, 0.00, 0.98, 0.12]
    difference_of_all_shifts = []

    # For all 26 possible shifts
    for shift in range(25):
        difference = 0
        probability_of_all_letters = []
        decrypted_text = caesar_decrypt(text, shift)

        # For all 26 letters
        for letter in range(25):
            number_of_letters = 0

            # For all characters in the decrypted text
            for character in decrypted_text:
                if character.upper() == alphabet_table[letter][0]:
                    number_of_letters += 1

            percentage = number_of_letters / len(text) * 100
            probability_of_all_letters.append(percentage)

        # Calculate the difference between expected and actual probabilities
        for i in range(25):
            difference = difference + abs(letter_probability[i] - probability_of_all_letters[i])
        difference_of_all_shifts.append(difference)

    # Sort shifts by difference (smaller is better)
    sorted_alphabet = sorted(zip(difference_of_all_shifts, alphabet_table), reverse=False)
    return sorted_alphabet[0]

# Main program start if the file is executed directly
if __name__ == "__main__":
    keyword = ""
    # User input for the text to be decrypted
    input_str = input("Enter your text (Please make sure it is already normalized): ")

    # Identify 3-character pairs in the text
    found_pairs = find_3_char_pairs(input_str)

    # Calculate distances between the found pairs
    distances = calculate_distances(input_str, found_pairs)

    # Identify common divisors and their frequencies
    divisors_list, frequencies_list = find_divisors_and_frequencies(distances)

    # Output the found divisors and their frequencies
    for i in range(len(divisors_list)):
        print("The key length", divisors_list[i], "has frequency:", frequencies_list[i])

    # User input for selecting the key length
    key_length = int(input("Choose a key length (does not have to be the one with the highest probability): "))
    
    # Split the text into parts according to the key length
    text_split = split_input_text(key_length, input_str)
    
    # Iterate through the split text parts  
    for i, text in enumerate(text_split):
        # Find the most probable shift for each text part
        most_probable_shift = find_most_probable_shift(text)
        keyword += str(most_probable_shift[1])
        cleaned_keyword = keyword.replace("[", "").replace("]", "").replace("'", "")
        # Output the results
        print("The most probable shift for position", (i + 1), "is:", most_probable_shift[1])
    print("The keyword is likely: " , cleaned_keyword)
