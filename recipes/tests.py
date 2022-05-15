import requests

id='0001'
response = requests.get('http://127.0.0.1:8000/recipes/recipes/')
print(response.text)    # レスポンスのHTMLを文字列で取得