import requests
import os

urls = ['https://www.hdwallpapers.in/thumbs/2019/astronaut_5-t2.jpg',
        'https://www.hdwallpapers.in/thumbs/2018/saturn_solar_system_4k_8k-t2.jpg',
        'https://www.hdwallpapers.in/thumbs/2018/macbook_5k-t2.jpg',
        'https://www.hdwallpapers.in/thumbs/2018/ubuntu_studio-t2.jpg',
        'https://www.hdwallpapers.in/thumbs/2018/apple_macbook_pro_4k-t2.jpg']

def get_file(url):
    r= requests.get(url, stream=True)
    return r

def get_name(url):
    name = url.split('/')[-1]

    folder = name.split('.')[0]

    if not os.path.exists(folder):
        os.makedirs(folder)

    path= os.path.abspath(folder)

    return path+'/'+name

def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)
            # print(chunk)

def main():
    for url in urls:
        save_image(get_name(url),get_file(url))

if __name__=="__main__":
    main()