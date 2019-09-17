import requests


base_url="http://artii.herokuapp.com/make?text="
text = 'ASCII art'
url = base_url + text.replace(' ', '+')
font_list = requests.get('http://artii.herokuapp.com/fonts_list').text.split("\n")



response = requests.get(url).text

print(font_list)

