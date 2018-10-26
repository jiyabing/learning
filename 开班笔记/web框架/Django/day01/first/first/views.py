from django.http import HttpResponse

def show_views(request, name, age):
	return HttpResponse('参数1：'+name+'参数2：'+age)

def run_views(request):
	return HttpResponse('这是一个测试')

def run1_views(request, num):
	return HttpResponse('请求的参数是：'+num)

def run2_views(request, num1, num2):
	return HttpResponse('数字1：'+num1+' 数字2：'+num2)