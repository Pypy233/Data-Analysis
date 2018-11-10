import scrapy
from taobao.items import TaobaoItem


class TmallSpider(scrapy.Spider):
    name = "tmall"
    allowed_domains =["http://www.tmall.com"]
    start_urls = ("http://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.JnyabL&cat=50025135"
                  "&sort=d&style=g&from=mallfp..pc_1_searchbutton&tmhkmain=0#J_Filter",)
    count = 0

    def parse(self, response):
         TmallSpider.count += 1
         divs = response.xpath('//div[@id="J_ItemList"]/div[@class="product  "]/div')  #<div class="product-iWrap">是区分他们的共同元素
         if not divs:
             self.log("List Page error __%s" %response.url)

         for div in divs:
            item = TaobaoItem()
            item["GOODS_PRICE"] = div.xpath('p[@class="productPrice"]/em/@title')[0].extract()
            item["GOODS_NAME"] = div.xpath('p[@class="productTitle"]/a/@title')[0].extract()
            goods_url = div.xpath('p[@class="productTitle"]/a/@href')[0].extract()
            item["GOODS_URL"] = goods_url  if "http:" in goods_url else ("http:"+ goods_url)
            yield scrapy.Request(url = item["GOODS_URL"],meta = {"item":item},callback = self.parse_detail,dont_filter=True)
            print(item["GOODS_NAME"])

    def parse_detail(self, response):#处理打开商品链接的那个页面
        item = response.meta["item"]
        divs = response.xpath('//div[@class="slogo"]/a')
        item["SHOP_NAME"] = divs.xpath('//strong/text()')[0].extract()
        shop_url = divs.xpath('@href')[0].extract()
        item["SHOP_URL"] = shop_url if "http:" in  shop_url else ("http"+ shop_url)
      #  print(item["GOODS_PRICE"],item["GOODS_NAME"], item["GOODS_URL"],item["SHOP_NAME"],item["SHOP_URL"]
        yield item
