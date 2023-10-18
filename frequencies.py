#  Write a program to print the frequencies of elements in an array.

# Using Dictionary:

# Initialize an array
my_array = [1, 2, 2, 3, 1, 4, 2, 3, 5]

# Create an empty dictionary to store frequencies
element_freq = {}

# Loop through the array
for element in my_array:
    # Check if the element is in the dictionary
    if element in element_freq:
        # If it is, increment the count
        element_freq[element] += 1
    else:
        # If it's not, add it to the dictionary with a count of 1
        element_freq[element] = 1

# Print the frequencies
for element, frequency in element_freq.items():
    print(f"Element {element} appears {frequency} times.")


# using-set-------
def print_element_frequencies(arr):
    unique_elements = set(arr)
    
    for element in unique_elements:
        count = arr.count(element)
        print(f"{element}: {count}")

# Example usage:
my_array = [1, 2, 2, 3, 3, 3]
print_element_frequencies(my_array)



