input_sentence = input("Enter a sentence here : ")
sentence = input_sentence.lower()
print(sentence)
count = 0
vowels = ["a","e","i","o","u"]
for char in sentence:
    if char in vowels:
        count = count + 1
print("The number of vowels in a given sentence is : ",count)
