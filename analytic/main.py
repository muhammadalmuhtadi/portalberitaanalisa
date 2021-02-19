from .cleantitle import get_final
from portalberita.models import detik,antara,kompas

def chart_detik():
    detik_judul,detik_tanggal = [],[]
    for x in detik.objects.values_list('title','date'):
        detik_judul.append(x[0])
        detik_tanggal.append(x[1])
    data = get_final(detik_judul,detik_tanggal)
    return data

def chart_kompas():
    kompas_judul,kompas_tanggal = [],[]
    for x in kompas.objects.values_list('title','date'):
        kompas_judul.append(x[0])
        kompas_tanggal.append(x[1])
    data = get_final(kompas_judul,kompas_tanggal)
    return data

def chart_antara():
    antara_judul,antara_tanggal = [],[]
    for x in antara.objects.values_list('title','date'):
        antara_judul.append(x[0])
        antara_tanggal.append(x[1])
    data = get_final(antara_judul,antara_tanggal)
    return data

detik_data= chart_detik()
kompas_data = chart_kompas()
antara_data = chart_antara()

