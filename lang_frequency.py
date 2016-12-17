import os
import re
from collections import Counter

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open (filepath) as file:
        input_data=file.read()
        return input_data
    
def get_list_of_words(data):
    if not data:
        print('Пустой текст')   
    all_words=re.findall(r'\w+',data.lower())    
    return all_words
        
def get_most_frequent_words(data): 
    NUMBER_FREQUENT_WORDS=10
    number_of_words=Counter(data)
    most_frequent_words=number_of_words.most_common(NUMBER_FREQUENT_WORDS)  
    for word in most_frequent_words:
        print(word[0],word[1])
        
if __name__ == '__main__':
    filepath=input('Введите абсолютный путь до файла ')
    text_strings=load_data(filepath)
    if load_data(filepath) is not None:
        wordlist=get_list_of_words(text_strings)
        get_most_frequent_words(wordlist)
    else:
        print('Неверный путь до файла')
        
