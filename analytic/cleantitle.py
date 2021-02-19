from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import re

myfile = open('analytic/penyakit.txt')
read = myfile.readlines()
ambil = [x.replace('\n','') for x in read]
myfile.close()

#ambil = ['tenaga kesehatan','covid-19','tiktok','kanker','corona','kleptomania','berat badan','vaksin','kista']

def oneGram(data):
    token = []
    gram = word_tokenize(data)
    for x in gram:
        if x == 'corona' or x == 'covid':
            x = 'covid-19'
        for i in ambil:
            if x == i:
                token.append(x)
    return token

def twoGrams(data):
    token = []
    gram = ngrams(word_tokenize(data), 2)
    temp = [' '.join(kata) for kata in gram]
    for x in temp:
        for i in ambil:
            if x == i:
                token.append(x)
    return token

def clean(data):
    sym = "!\"#$%&()*+.,/:;<=>?@[\]'^_`{|}~\n"
    for x in sym:
        data = data.replace(x, '')  #tidak di stem karena
    return data.lower()

def gabung(title, tanggal):
    data_awal = []
    for x,y in zip(title,tanggal):
        x = clean(x)
        x =  (oneGram(x)+twoGrams(x))
        data_awal.append([x,re.sub(r"[^a-zA-z]+",'', y)])
    return data_awal

def get_final(title,date):
    import calendar
    import numbers
    final = []
    data = gabung(title,date)
    for el in data:
        if len(el[0]) > 0:
            for key in el[0]:
                if key not in [sub[0] for sub in final]:
                    final.append([key] + [0]*13)
                for sub in final:
                    if sub[0] == key:
                        sub[list(calendar.month_abbr).index(el[-1][:3])] += 1

    for n in final:
        n[-1] = sum(x for x in n if isinstance(x, numbers.Number))
    
    return final