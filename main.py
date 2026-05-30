import time
import random

file = open("word_list.txt", "r", encoding="utf-8")
full_words_list = file.read().splitlines()

def calculate_wpm(num_of_words, completition_time):
    return num_of_words/completition_time * 60

def calculate_accuracy(words, typing):
    accuracy = 100
    i = 0
    words_typed = typing.split(" ")
    while (i < 25):
        if (words_typed[i] != words[i]):
            accuracy = accuracy - 4
        i = i + 1

    return accuracy

words = random.sample(full_words_list, 25)    

num_of_words = input("How many words do you want to type?")
i = num_of_words
while (i < num_of_words - 1):
    print(f"{words[i]}", end = " ")
    i = i + 1
if (i == num_of_words):
    print(f"{words[1]}")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
start_time = time.time()
typing = input("begin:")
if (typing == "hello world"):
    end_time = time.time()
    completiton_time = (end_time - start_time)
    print(f"{completiton_time} seconds")
    print("100% accuracy")
    print(f"{calculate_wpm(2, completiton_time)} words per minute")
else:
    end_time = time.time()
    completiton_time = (end_time - start_time)
    print(f"{completiton_time} seconds")
    wpm = calculate_wpm(2, completiton_time)
    print(f"{wpm} words per minute")
    accuracy = calculate_accuracy(words, typing)
    print(f"{accuracy}% acurracy")
    raw_wpm = (accuracy/100) * wpm
    print (f"raw words per minute: {raw_wpm}")

