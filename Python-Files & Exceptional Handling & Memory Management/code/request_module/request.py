import requests

url = "http://dimikcomputing.com"

#Save web page in file
response = requests.get(url)
with open("file/dimik.html", "w") as f:
    f.write(response.text)

# Open file at web browser
import os
import requests
import webbrowser as wb

url = "http://dimikcomputing.com"

response = requests.get(url)

with open("dimik.html", "w") as f:
    f.write(response.text)

file_path = os.path.realpath("dimik.html")
print(file_path)

wb.open("file://"+file_path)


#download image from a website
import requests

url = "https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"

request = requests.get(url)

try:
    with open("file/python.jpg", "wb") as f:
        f.write(request.content)
except Exception as e:
    print(e)
else:
    print("Image Successfully Download")




