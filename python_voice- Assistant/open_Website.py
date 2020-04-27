import webbrowser

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")
Website=""
# to search 
query = "sensors used in arduino"
  
for j in search(query, tld="co.in", num=1, stop=1, pause=2):
    print(j)
    Website=j
webbrowser.open(Website)
