import requests
import hashlib
import json
from bs4 import BeautifulSoup

def entrada_data():

    data = input('coloque a data desejada no formato dd/mm/aaaa: ')   #dd/mm/aaaa
    data2 = data[6:10]+data[3:5]+data[0:2]                          #aaaammdd
    return data, data2


def montar_link(data, data2): #http://www.stf.jus.br/portal/diariojusticaeletronico/montarDiarioEletronico.asp?tp_pesquisa=0&dataD=14/09/2021
    url = (f'http://www.stf.jus.br/portal/diariojusticaeletronico/montarDiarioEletronico.asp?tp_pesquisa=0&dataD={data}')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'}
    response = requests.get(url, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    valor = soup.find_all('td')
    try:
        #print (valor[0].text)
        valor1 = (valor[0].text)
        url2 = (f'https://www.stf.jus.br/arquivo/djEletronico/DJE_{data2}_{valor1}.pdf') #https://www.stf.jus.br/arquivo/djEletronico/DJE_20211011_203.pdf
        # print (valor[5].text)
        # valor2 = (valor[5].text)
        # print (valor[10].text)
        # print (valor[15].text)
    except:
        pass

    return url2


def gerar_md5(url):
    m = hashlib.md5()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'}
    r = requests.get(url, headers=headers)
    for data in r.iter_content():
         m.update(data)
    #return m.hexdigest()
    print(m.hexdigest())

try:

    data, data2 = entrada_data()

    url2 = montar_link(data, data2)

    gerar_md5(url2)
except:
    print("Insira um valor valido")







#print ("codigo md5:" ,gerar_md5("https://www3.tjma.jus.br/diario/diarios/2020/diario_31072020_121427_138.pdf"))