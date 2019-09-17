#웹 브라우저 컨트롤

import webbrowser


url1 = "https://search.daum.net/search?q="
keywords = ['아이유','설현','수지']

for keyword in keywords:   
    webbrowser.open(url1 + keyword)