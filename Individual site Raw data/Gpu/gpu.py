
from bs4 import BeautifulSoup
import requests
import time
import threading

# output csv file declared here
filename = "gpudata.csv"

f = open(filename, 'w', encoding='utf-8-sig')

headers = "Product_Title,Price,Shop_Name,Category,Availability,G-Price\n"

f.write(headers)


def webscrapCvillageGpu():

    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get(
            'https://www.computervillage.com.bd/graphics-card?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all('div', class_='grid-view-item')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find(
                'h4', class_='h4 grid-view-item__title text-truncate-2')

            title = product_name.a.text.replace(",", "").upper()

            product_price = product.find('span', class_='money')

            tk = product_price.text.replace(",", "").replace("৳", "")

            g_price = tk.replace('Call For Price', 'null')

            #print(tk)

            availability = product.find(
                'span', class_='sticker-stock-l bg-red')

            if availability:
                stock = availability.text

            else:
                stock = 'In Stock'

            #print(stock)

            data = title + "," + tk + "," + "COMPUTER VILLAGE" + \
                "," + "GPU" + "," + stock + "," + g_price + "\n"

            f.write(data)

        time.sleep(5)


def webscrapTechlandGpu():

    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
             20, 21, 22, 23, 24, 25, 26]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get(
            'https://www.techlandbd.com/pc-components/graphics-card?page={}'.format(page)).text

        # source_link = requests.get('https://www.techlandbd.com/shop-computer-mouse?page=40').text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_thumb = body.find_all('div', class_='product-thumb')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find('div', class_='name')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='price')

            if product_price:
                tk = product_price.span.text

            else:
                tk = 'N/A'

            g_price = tk.replace('N/A', 'null')

            availability = product.find('div', class_='cart-group')
            stock = availability.a.text

            #print(stock)

            data = (title.replace(",", "") + "," + tk.replace("৳", "").replace(",",
                    "") + "," + "TECHLAND" + "," + "GPU" + "," + stock.replace("Add to Cart", "In Stock") + "," + g_price.replace("৳", "").replace(",",
                    "") + "\n")

            f.write(data)

        time.sleep(5)


def webscrapStartechGpu():
    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
             13, 14, 15, 16, 17, 18, 19, 20, 21]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get(
            'https://www.startech.com.bd/component/graphics-card?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all('div', class_='p-item')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find('h4', class_='p-item-name')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='p-item-price')

            tk = product_price.span.text.replace(",", "").replace("৳", "")

            g_price = tk.replace('TBA', 'null')

            # int(tk)

            availability = product.find('div', class_='actions')
            stock = availability.span.text

            #print(stock)

            data = (title.replace(",", "") + "," + tk.replace("৳", "").replace(",",
                    "") + "," + "STARTECH" + "," + "GPU" + "," + stock.replace("shopping_cart Buy Now", "In Stock") + "," + g_price + "\n")

            f.write(data)
        time.sleep(5)


def webscrapRyansGpu():
    pages = [1, 2, 3, 4, 5]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get(
            'https://www.ryanscomputers.com/category/desktop-component-graphics-card?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_info = body.find_all('div', class_='card h-100')

        # using loop for grabing whole page data

        for product in product_info:

            product_name = product.find(
                'p', class_='card-text p-0 m-0 list-view-text')

            title = product_name.a.text.replace(",", "").upper()

            product_price = product.find(
                'p', class_='pr-text cat-sp-text pb-1')
            
            old_price = product.find(
                'del', class_='text-muted')

            product_price = product.find(
                'p', class_='pr-text cat-sp-text pb-1')

            if old_price:
                old_price.clear()
                #print(old_price)
            elif product_price:
                tk = product_price.text.replace(
                    "Tk", "").replace(",", "").strip()

            else:
                tk = 'N/A'

            tk = product_price.text.replace("Tk", "").replace(",", "").strip()

            g_price = tk

            availability = product.find(
                'button', class_='btn cart-btn')
            #stock = availability.text
            if availability:
                newstock = 'In Stock'
            else:
                newstock = 'Out of Stock'
            #print(newstock)

            data = title + "," + tk + "," + "RYANS" + "," + \
                "GPU" + "," + newstock + "," + g_price + "\n"

            f.write(data)
        time.sleep(5)


def webscrapSkylandGpu():

    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get(
            'https://www.skyland.com.bd/product-category/components/graphics-card/page/{}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all(
            'div', class_='box-text box-text-products text-center grid-style-2')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find(
                'p', class_='name product-title woocommerce-loop-product__title')

            title = product_name.a.text.replace(",", "").upper()
            product_price = product.find(
                'span', class_='woocommerce-Price-amount amount')

            if product_price:
                tk = product_price.text.replace(",", "").replace("৳", "")
                tk = int(tk)

            else:
                tk = 'N/A'

            tk = str(tk)
            g_price = tk.replace('N/A', 'null')

            availability = product.find('div', class_='out-of-stock-label')
            if availability:
                stock = availability.text
                #print(stock)

            else:
                stock = 'In Stock'

            data = title + "," + tk + "," + "Skyland" + "," + \
                "GPU" + "," + stock + "," + g_price + "\n"

            f.write(data)

        time.sleep(5)


threading.Thread(target=webscrapCvillageGpu).start()
threading.Thread(target=webscrapTechlandGpu).start()
threading.Thread(target=webscrapStartechGpu).start()
threading.Thread(target=webscrapRyansGpu).start()
threading.Thread(target=webscrapSkylandGpu).start()
