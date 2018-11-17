import csv


class CsvUtil:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name + '.csv', 'w') as file:
            csv_writer = csv.writer(file)
            csv_head = ['商品', '店铺', '价格', '成交量', '图片链接', '地点']
            csv_writer.writerow(csv_head)

    def write_csv(self, product_dict):
        with open(self.file_name + '.csv', 'a+') as file:
            csv_writer = csv.writer(file)
            name = product_dict['title']
            shop = product_dict['shop']
            price_str = product_dict['price']
            idx = price_str.find('\n')
            if idx >= 0:
                price = float(price_str[idx:])
            else:
                price = 0
            deal_str = product_dict['deal']
            idx = deal_str.find('人')
            if idx >= 0:
                deal = int(deal_str[:idx])
            else:
                deal = 0
            image_link = product_dict['image']
            location = product_dict['location']
            data_row = [name, shop, price, deal, image_link, location]
            csv_writer.writerow(data_row)


# csv_util = CsvUtil('显示器')
# product_dict = {'image': '//g-search3.alicdn.com/img/bao/uploaded/i4/i2/2414673821/'
#                          'O1CN01AL6aSX1e63qGJrRnm_!!0-item_pic.jpg',
#                 'price': '¥\n2599.00', 'deal': '523人付款',
#                 'title': 'AOC 32英寸曲面2K\n显示\n器\n144Hz吃鸡游戏1ms响应电竞高清液晶台式电脑'
#                          '\n显示\n器\nCQ32G1曲屏网咖网吧屏幕PS4壁挂',
#                 'shop': '本晨数码专营店', 'location': '福建 福州'}
# csv_util.write_csv(product_dict=product_dict)
