# using loop
def find_longest_word(sentence):
     words = sentence.split()
     longest_word = ""

     for word in words:
         if len(word) > len(longest_word):
             longest_word = word
     return longest_word
     
sentence = "Madhusudhan is working in MSYS"
print(find_longest_word(sentence))

# built-in---------?

def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

sentence = "Cats quickly jump over fences"
print(find_longest_word(sentence))

# using sorted list

def find_longest_word(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=len)
    return sorted_words[-1]

sentence = "Cats quickly jump over fences"
print(find_longest_word(sentence))