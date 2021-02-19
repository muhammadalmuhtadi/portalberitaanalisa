from .models import Detik,Kompas,Antara

def barFunc(namamodel,batas):
    nama, angka = [], []
    data = (nama,angka)
    get_db = namamodel.objects.values_list('token','total')
    for x in get_db:
        if x[1] > batas:
            nama.append(x[0])
            angka.append(x[1])

    return data



def pieFunc():
    def get_top(tokens, scores):
        top = {}

        #Normalisasi Code (Delete?)
        scores_min, scores_max = min(scores), max(scores)
        for i, val in enumerate(scores):
            scores[i] = (val-scores_min) / (scores_max-scores_min)
            scores[i] = round(scores[i], 2)

        tops = sorted(zip(scores, tokens), reverse=True)[:3]    

        for x in tops:
            top[x[1]]=x[0]

        return top  

    def get_total(dict1,dict2):
        dict3 = {**dict1, **dict2}
        for key, value in dict3.items():
            if key in dict1 and key in dict2:
                dict3[key] = value + dict1[key]

        return dict3

    top_detik = get_top(barFunc(Detik,0)[0], barFunc(Detik,0)[1])
    top_kompas = get_top(barFunc(Antara,0)[0], barFunc(Antara,0)[1])
    top_antara = get_top(barFunc(Kompas,0)[0], barFunc(Kompas,0)[1])    
    
    pie = get_total(get_total(top_detik,top_kompas),top_antara)

    return pie