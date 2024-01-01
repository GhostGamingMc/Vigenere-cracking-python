# Vigenere-cracking-python

## Description:

This Python program is designed to analyze an input text, identify repeating three-character pairs, determine the distances between these pairs, and then attempt to find the most likely key length for a Vigenère cipher used in the encryption. Finally, it extracts the key and decrypts the original text.

## Version:

Ensure you use the correct version of the program; you can choose between German and English text. In the different programs, the letter probability is tailored for the specific language.

## Features:

- Identification of repeating three-character pairs in the input text.
- Calculation of distances between the identified pairs.
- Analysis of common factors and their frequencies among the distances.
- User input for selecting a potential key length.
- Splitting the text into segments based on the chosen key length.
- Utilization of frequency analysis to find the most likely Vigenère cipher key for each segment.
- Output of the probable key and the decrypted text.

**Note:** The program is designed for texts with a minimum length of 300 characters to ensure effective analysis and accurate results.

## Usage:

1. Run the program.
2. Input the text to be decrypted (ensure it is already normalized).
3. The program will identify repeating three-character pairs and calculate the distances between them.
4. Common factors among the distances will be analyzed to suggest potential key lengths.
5. Choose a key length based on the provided suggestions.
6. The program will split the text into segments according to the selected key length.
7. For each segment, it will find the most probable Vigenère cipher key using frequency analysis.
8. The final key will be presented along with the decrypted text.

## Feedback:

I value your feedback and welcome any comments, suggestions, or bug reports related to this program. Your input helps me improve the functionality and address any issues that may arise.
