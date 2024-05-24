# import urllib.request
# import urllib.parse
from urllib.request import urlopen

response = urlopen("http://www.packtpub.com")
response
response.readline()

# url = "http://www.rockvalleycollege.edu"

# data_dictionary = {"id": "0123456789"}
# data = urllib.parse.urlencode(data_dictionary)
# data = data.encode("ascii")

# with urllib.request.urlopen("http://httpbin.org/post", data) as response:
#     print(response.read().decode("utf-8"))
