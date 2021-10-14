import requests
import hashlib
from bs4 import BeautifulSoup

def entrada_data():

    data = input('coloque a data desejada no formato dd/mm/aaaa: ')   #dd/mm/aaaa
    data2 = data[6:10]+data[3:5]+data[0:2]                            #aaaammdd
    return data, data2


def montar_link(data, data2):
    url = (f'http://www.stf.jus.br/portal/diariojusticaeletronico/montarDiarioEletronico.asp?tp_pesquisa=0&dataD={data}')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'}
    response = requests.get(url, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    valor = soup.find_all('td')
    try:
        valor1 = (valor[0].text)
        if len(valor1) == 2:
            valor1 = ('0'+valor1)
        elif len(valor1) == 1:
            valor1 = ('00'+valor1)
        url1 = (f'https://www.stf.jus.br/arquivo/djEletronico/DJE_{data2}_{valor1}.pdf')
    except:
        pass
    try:
        valor2 = (valor[5].text)
        if len(valor2) == 2:
            valor2 = ('0'+valor2)
        elif len(valor2) == 1:
            valor2 = ('00'+valor2)
        url2 = (f'https://www.stf.jus.br/arquivo/djEletronico/DJE_{data2}_{valor2}.pdf')
    except:
        url2 = None
    try:
        valor3 = (valor[10].text)
        if len(valor3) == 2:
            valor3 = ('0'+valor3)
        elif len(valor1) == 1:
            valor3 = ('00'+valor3)
        url3 = (f'https://www.stf.jus.br/arquivo/djEletronico/DJE_{data2}_{valor3}.pdf')
    except:
        url3 = None
    return url1, url2, url3


def gerar_md5(url):
    m = hashlib.md5()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'}
    r = requests.get(url, headers=headers)
    for data in r.iter_content():
         m.update(data)
    print(f'{m.hexdigest()}')


data, data2 = entrada_data()


try:
    url1 = montar_link(data, data2)[0]
    gerar_md5(url1)
except:
    print("Erro: Talvez você tenha colocado uma data que não possui diário ou inserido uma entrada no formato errado.")
try:
    url2 = montar_link(data, data2)[1]
    gerar_md5(url2)
except:
    pass
try:
    url3 = montar_link(data, data2)[2]
    gerar_md5(url3)
except:
    pass
