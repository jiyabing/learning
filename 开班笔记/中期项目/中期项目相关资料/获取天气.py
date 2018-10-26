#coding:gbk
import sys,json
import urllib.request

def get_whether(city_name):  
	city_code_dict = {'����': '101010100', '�Ϻ�': '101020100','���': '101030100','����': '101040100','�人':'101200101'}  
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
	#result_dict = json.loads(content) #����ҳ��ȡ��jsonת�����ֵ� 
	#print(result_dict)
	#item = result_dict.get('weatherinfo')  #ȡ�ֵ��ֵ��get����  
	#print result_dict['weatherinfo']['city']   
	#print ("%s����:%s,����¶�:%s,����¶�:%s" %(item.get('city'),item.get('weather'), item.get('temp2'), item.get('temp1')))

get_whether('�人')
