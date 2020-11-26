import requests
URL = "http://18.212.183.253/info.php"
params = {'unique_num':'p1','url':'http://1.246.40.183:8080/?action=stream'}
res = requests.get(URL, params=params)