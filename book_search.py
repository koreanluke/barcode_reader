import urllib.parse
import urllib.request
import xml.etree.ElementTree as elemTree 

secret_key = "758560af2a1e7991d010f8d51f172a49"
isbn = "9791"

api_url = "https://www.nl.go.kr/NL/search/openApi/search.do"
api_url += f"?key={secret_key}"
api_url += "&detailSearch=true"
api_url += "&isbnOp=isbn"
api_url += f"&isbnCode={isbn}"

print(api_url)
req = urllib.request.Request(api_url)
with urllib.request.urlopen(req) as response :
    the_page = response.read()
    string_data = the_page.decode('utf-8')
    #print(string_data)
    
    root = elemTree.fromstring(string_data)
    result = root.find("result")
    
    for item in result:
        title = item.find("title_info").text
        print(title)
        author = item.find("author_info").text
        print(author)