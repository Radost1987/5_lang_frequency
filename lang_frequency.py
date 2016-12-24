import os
import re
from collections import Counter

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open (filepath,encoding='utf-8') as file:
        input_data=file.read()
        return input_data
    
def get_list_of_words(data):
    if not data:
        print('Пустой текст')   
    all_words=re.findall(r'\w+',data.lower())    
    return all_words
        
def get_number_words_repetitions(data): 
    number_of_words=Counter(data)
    return number_of_words
 

def get_most_frequent_words(data):
    print('10 самых часто встречаемых слов в данном тексте')
    number_frequent_words=10
    most_frequent_words=data.most_common(number_frequent_words)  
    for word, number in most_frequent_words:
        print(word,number)
        
if __name__ == '__main__':
    filepath=input('Введите абсолютный путь до файла ')
    full_text=load_data(filepath)
    if full_text is not None:
        wordlist=get_list_of_words(full_text)
        number_words_repetitions=get_number_words_repetitions(wordlist)
        get_most_frequent_words(number_words_repetitions)
    else:
        print('Неверный путь до файла')
        
