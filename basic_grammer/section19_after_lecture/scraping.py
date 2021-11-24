import requests
from bs4 import BeautifulSoup

# スクレイピング webサイトから情報を抽出すること requestsライブラリが必要
# スクレイビングを許可していないサイトについては行わないようにすること
res = requests.get('https://yubiori-band.com/')
print(res.text)  # htmlが見れる

# scriptタグ内にかかれた文字列だけを取得
soup = BeautifulSoup(res.text, 'html.parser')
for script in soup.find_all('script'):
    print(script)
