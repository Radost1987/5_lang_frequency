import os
import re
from collections import Counter

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open (filepath) as file:
        input_data=file.readlines()
        return input_data
    
def get_list_of_words(data):
    if not data:
        print('Пустой текст')   
    all_words=[]
    for words in data:
        all_words+=re.findall(r'\w+',words.lower())
    return all_words
        
def get_most_frequent_words(data):   
    number_of_words=Counter(data)
    most_frequent_words=number_of_words.most_common(10)
    for word in range(len(most_frequent_words)):
        print(most_frequent_words[word][0],most_frequent_words[word][1])
        
if __name__ == '__main__':
    filepath=input('Введите абсолютный путь до файла ')
    text_strings=load_data(filepath)
    if load_data(filepath) is not None:
        wordlist=get_list_of_words(text_strings)
        get_most_frequent_words(wordlist)
    else:
        print('Неверный путь до файла')
