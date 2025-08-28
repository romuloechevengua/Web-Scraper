import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com'
response = requests.get(url)

# Verifica se a requisição foi bem sucedida (código 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titulos = soup.find_all('a', class_='feed-post-link')

    #Abrindo o arquivo para escrita
    with open('noticias_g1.txt', 'w', encoding='utf-8' ) as file:
        file.write('Manchetes do G1\n\n')
        for titulo in titulos:
            texto = titulo.get_text().strip()
            link = titulo.get('href')

            file.write(f'Título: {texto}\n')
            file.write(f'Link: {link}\n')
            file.write('---\n')
    print('Dados salvos em noticias_g1.txt com sucesso!')
else:
    print(f'Erro na requisição: {response.status_code}')

