###
# pip install selenium
#pip install pillow
#pip install pytesserat


from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

class Bot:
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito/avito_screenshot.png')

    def tel_recon(self):
        image=Image.open('avito/tel.gif')
        print(image_to_string(image))

    def crop(self, location, size):
        image=Image.open('avito/avito_screenshot.png')
        x=location['x']
        y=location['y']
        width= size['width']
        height= size['height']

        image.crop((x,y, x+width, y+height)).save('avito/tel.gif')
        self.tel_recon()

    def navigate(self):
        self.driver.get('https://www.avito.ru/orenburg/kvartiry/2-k_kvartira_65_m_516_et._1202106358')

        button = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()

        sleep(3)

        self.take_screenshot()

        image=self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location=image.location
        size=image.size
        self.crop(location, size)


def main():
    d = Bot()

if __name__=="__main__":
    main()
