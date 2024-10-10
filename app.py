import spacy

llm = spacy.load("en_core_web_lg")

secret_word = "pasta"

token_secret_word = llm(secret_word)
print(token_secret_word)

given_word = input("Guess my secret word: ")
token_given_word = llm(given_word)
print(token_given_word)

if secret_word == given_word:
    similarity = 1
else:
    similarity = token_given_word.similarity(token_secret_word)


if similarity ==1:
    message = "You won !"
else:
    message = "You word '"+given_word+"' get you up to "+str(similarity*100)+" °C"

print(message)


# https://www.geeksforgeeks.org/python-word-similarity-using-spacy/

