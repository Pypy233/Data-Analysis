from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from CsvUtil import CsvUtil
from pyquery import PyQuery as pq


class SafeTMall:
    def __init__(self, keywords):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.keywords = keywords
        self.max_page = 100
        self.csv_util = CsvUtil(self.keywords)

    def index_page(self, page):
        print('正在爬取第', page, '页')
        try:
            url = 'https://s.taobao.com/search?q=' + quote(self.keywords)
            self.driver.get(url)
            if page > 1:
                input = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#mainsrp-pager    div.form > input')))
                submit = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                '#mainsrp-pager div.form > span.btn.J_Submit')))
                input.clear()
                input.send_keys(page)
                submit.click()
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
            )
            self.wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, '.m-itemlist .items .item')))
            self.get_products()
        except TimeoutException:
            self.index_page(page)

    def get_products(self):
        html = self.driver.page_source
        doc = pq(html)
        items = doc('#mainsrp-itemlist .items .item').items()
        for item in items:
            product = {
                'image': item.find('.pic .img').attr('data-src'),
                'price': item.find('.price').text(),
                'deal': item.find('.deal-cnt').text(),
                'title': item.find('.title').text(),
                'shop': item.find('.shop').text(),
                'location': item.find('.location').text()
            }
            print(product)
            self.csv_util.write_csv(product_dict=product)
            print('\n')


def main():
    print('Enter the keywords, like 键盘 etc...')
    keywords = input()
    tmall = SafeTMall(keywords)
    for i in range(1, tmall.max_page + 1):
        tmall.index_page(i)
    tmall.driver.close()


if __name__ == '__main__':
    main()
