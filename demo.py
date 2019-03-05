from ctypes import *
dll = cdll.LoadLibrary("czJetFileII.dll")
dll.czAPIVersion.restype = c_char_p
apiversion = dll.czAPIVersion()
print(apiversion)

import requests

def download_img(img_url,filename):
    response = requests.get(img_url)
    img_data = response.content
    with open(filename, 'wb') as f:
        f.write(img_data)
download_img('https://www.baidu.com/img/bd_logo1.png','baidu.png')





