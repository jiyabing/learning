#coding:gbk
import sys,json
import urllib.request

def get_whether(city_name):  
	city_code_dict = {'北京': '101010100', '上海': '101020100','天津': '101030100','重庆': '101040100','武汉':'101200101'}  
	if len(city_name) == 0:  
		print("city name is null")
		sys.exit()
	if city_name not in city_code_dict:  
		print("city not exists") 
		sys.exit()  
	postal_code = city_code_dict[city_name]  
	if postal_code.isdigit() == False:  
		print("input is not number!")
		sys.exit()
	
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}		
	url = "http://www.weather.com.cn/data/cityinfo/"+postal_code+".html"
	#url = 'http://www.weather.com.cn/weather1d/101200101.shtml'
	
	html = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(html)
	
	content = res.read()  
	print(content.decode('utf-8'))   
	#result_dict = json.loads(content) #从网页爬取的json转化成字典 
	#print(result_dict)
	#item = result_dict.get('weatherinfo')  #取字典的值用get方法  
	#print result_dict['weatherinfo']['city']   
	#print ("%s天气:%s,最高温度:%s,最低温度:%s" %(item.get('city'),item.get('weather'), item.get('temp2'), item.get('temp1')))

get_whether('武汉')
