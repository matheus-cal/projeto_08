from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.submarino.com.br/categoria/livros?chave=prf_hm_tt_0_1_livros')

def get_category():
    driver.find_element_by_xpath('//*[@id="main-top"]/div[6]/div/div/div/div/div/div[2]/div/div/a/div/picture/img').click()
    driver.implicitly_wait(3)
    

def get_pagination():
    driver.implicitly_wait(3)
    
    link_list = list()

    pagination = driver.find_element_by_xpath('//ul[@class="pagination-product-grid pagination"]')
    link_item = pagination.find_elements_by_css_selector('a')
    
    for item in link_item:
        link_list.append(item.get_attribute('href'))

    return link_list


def get_books():
    driver.implicitly_wait(3)
    
    book_list = list()

    library = driver.find_element_by_xpath('//div[@class="row product-grid no-gutters main-grid"]')
    books = library.find_elements_by_xpath('//div[@class="product-grid-item ColUI-gjy0oc-0 ifczFg ViewUI-sc-1ijittn-6 iXIDWU"]')
    for book in books:
        book_links = book.find_element_by_css_selector('a')
        book_list.append(book_links.get_attribute('href'))

    return book_list

    # print(book_list)

def get_books_info():

    driver.implicitly_wait(3)

    book_name = driver.find_element_by_xpath('//h1[@id="product-name-default"]')  
    book_name = str(book_name.text)
    book_price = driver.find_element_by_xpath('//span[@class="price__SalesPrice-sc-1i11rkh-2 jjADsQ TextUI-sc-12tokcy-0 CIZtP"]')
    book_price = str(book_price.text)

    driver.implicitly_wait(6)

    return book_name, book_price


if __name__ == '__main__':

    # get_category()
    # get_pagination()
    # get_books()
    # print(get_books_info())

    with open('books.txt', 'w') as file:
        get_category()
        pagination = get_pagination()
        for page in pagination:
            driver.get(page)
            file.write(f'Page: {page}\n')
            books_links = get_books()
            for book in books_links:
                driver.get(book)
                book_name, book_price = get_books_info()
                file.write('Nome: ')
                file.write(f'{book_name}')
                file.write('\n')
                file.write('Preço: ')
                file.write(f'{book_price}')
                file.write('\n')

            file.write('\n--------\n')

        print ('Ok')