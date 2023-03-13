from django.http import HttpResponse


#Expected input format is: http://localhost:8000/add/?first=657&second=30

def addPageView(request):

	addition_variable_1 = int(request.GET.get('first'))  
	""" 
	the int part is important to store the value as INT, else it will be treated as string
	Figured out the int part from https://pythonguides.com/get-data-from-get-request-in-django/
	"""
	addition_variable_2 = int(request.GET.get('second'))
	print("debugging, addvar1 is ", addition_variable_1, "addvar2 is ", addition_variable_2)
	addition_result = addition_variable_1+addition_variable_2
	print("addresult is ", addition_result)
	return HttpResponse(addition_result)
	

#Expected input format is: http://localhost:8000/multiply/?first=2&second=30
def multiplyPageView(request):
	multiply_variable_1 = int(request.GET.get('first'))  #the int part is important to store the value as INT, else it will be treated as string
	multiply_variable_2 = int(request.GET.get('second'))
	multiply_result = multiply_variable_1*multiply_variable_2
	return HttpResponse(multiply_result)
