import requests

url = 'https://spiska.pythonanywhere.com/api/shops/'

file = {'img' : open('resizedBeach1.jpg', 'rb')}

data = {
    'name' : 'Noutbuklar olami3',
    'description' : "siz bu yerda o'zingizga yoqqan noutbukni topishingiz mumkin",
    'password' : '@Qwerty11',
    'viloyat' : 1,
    'tuman' : 4
}

r = requests.post(url, data=data, files=file)
d = r.json()
print(d)

