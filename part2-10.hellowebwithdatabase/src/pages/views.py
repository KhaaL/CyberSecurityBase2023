from django.http import HttpResponse
from .models import Message
# import os # neccesary for relative path to sqlite3 db
# import sys #ibid
# import sqlite3

# supporting documentation: https://docs.djangoproject.com/en/4.1/intro/tutorial02/
# https://docs.djangoproject.com/en/3.0/topics/db/queries/#the-pk-lookup-shortcut
# perhaps relevant? https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.Field.value_from_object


# Create your views here.
#Expected input format is: http://localhost:8000/?id=657 

def homePageView(request):
	input_msg_id = int(request.GET.get('id')) 
#	dbpath = os.path.dirname(os.path.dirname(__file__))
#	dbpath = os.path.join(dbpath, "db.sqlite3")
#	conn = sqlite3.connect(dbpath)
#	cur=conn.cursor()
# NB - The code above is not needed - the SQLite db is already set up and accessible through settings & models pages.
	web_message=Message.objects.get(id=(input_msg_id)).content
	# NB! Use the syntax Modelname-object-method+filter-attribute if needed.
	print("🟡 ", web_message)
	# print(Message.objects.all())
	




	content = (web_message);	
#	content = 'Hello Web!';	
	return HttpResponse(content)
