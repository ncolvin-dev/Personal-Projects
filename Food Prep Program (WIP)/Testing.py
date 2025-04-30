data = "This is a sample string containing various words, including the word Ingredients and more."
search_word = "Ingredients"
word_length = len(search_word)
data_length = len(data)

found = False
for i in range(data_length - word_length + 1):
    if data[i:i + word_length] == search_word:
        print(f"'{search_word}' found in the data at position {i}.")
        found = True
        break

if not found:
    print(f"'{search_word}' not found in the data.")
