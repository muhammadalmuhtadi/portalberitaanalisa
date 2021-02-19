from analisa.models import Detik,Kompas,Antara

def save(data, namamodel):           
    for b in data:
        simpan = namamodel(
            token       = b[0],
            january     = b[1],
            february    = b[2],
            march       = b[3],
            april       = b[4],
            may         = b[5],
            june        = b[6],
            july        = b[7],
            august      = b[8],
            september   = b[9],
            october     = b[10],
            november    = b[11],
            december    = b[12],
            total       = b[13],
            )
        simpan.save()
