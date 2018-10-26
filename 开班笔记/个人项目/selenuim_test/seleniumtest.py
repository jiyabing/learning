from selenium import webdriver


#url = 'https://www.douban.com/'

#driver = webdriver.Chrome()
#driver.get(url)
#driver.implicitly_wait(5)
#driver.find_element_by_id('form_email').clear()
#driver.find_element_by_id('form_email').send_keys('1079902100@qq.com')
#driver.find_element_by_id('form_password').clear()
#driver.find_element_by_id('form_password').send_keys('19900914jyb')
#driver.find_element_by_class_name('bn-submit').click()
#print(driver.page_source)
#with open('douban.html', 'w', encoding='utf-8') as fw:
#   fw.write(driver.page_source)
    

# 异步加载数据
url2 = 'https://www.jianshu.com/p/17dc3193660b'
driver = webdriver.Chrome()
driver.get(url2)
driver.implicitly_wait(20)
author = driver.find_element_by_xpath('//span[@class="name"]/a').text
date_time = driver.find_element_by_xpath('//span[@class="publish-time"]').text
include_collections = driver.find_elements_by_xpath('//div[@class="include-collection"]/a/div')
print(author, date_time)
for include_collection in include_collections:
    print(include_collection.text)