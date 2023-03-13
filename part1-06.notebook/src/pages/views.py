from django.shortcuts import render

# Create your views here.

def addPageView(request):
	items = request.session.get('items', [])

	print("entering homePageView", items)
	print ("current items", items)

	if request.method == 'POST':
		item = request.POST.get('content', '').strip() # make sure that the HTML input form name matches 'content'. content=key. https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict
		print ("entering if statement at homePageView, length is ", len(item))
		print ("item", item)
		print ("items", items)
		if len(items) > 9:
			print ("poping due to above 10")
			items.pop(0)
		if len(item) > 0:
			print ("appending due to above 0")
			items.append(item)
		request.session['items'] = items

	return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
	items = request.session.get('items', [])
	print("entering erasePageView")
	print ("current items", items)
	if len(items) > 0:
#		print ("purging items")
#		del items[:]
#		items.clear()
################
#
#  The commands above does not help clear out the stored information in the browser session. One way to clear individual session would be through del request.session, but in this case flush() works just as well.
#  https://docs.djangoproject.com/en/3.1/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.__delitem__
#
# ################
		request.session.flush()
		print ("items after purge ", items)


	return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])
	print("entering homePageView")
	print ("current items", items)

	if request.method == 'POST':
		item = request.POST.get('content', '').strip() # make sure that the HTML input form name matches 'content'. content=key. https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.QueryDict
		print ("entering if statement at homePageView, length is ", len(item))
		print ("item", item)
		print ("items", items)
		if len(items) > 9:
			print ("poping due to above 10")
			items.pop(0)
		if len(item) > 0:
			print ("appending due to above 0")
			items.append(item)
		request.session['items'] = items


	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})



"""
Hi all, so I have thrown together some code that resembles a notebook as per this programming excercise: https://cybersecuritybase.mooc.fi/module-2.1/2-servers#programming-exercise-notebook
Most functionality is intact, but I can't for my life understand why when i empty the contents of the list 'items' once /erase is visited, it is still present in homepageview. 

Also, I'm really confused the following:
 - by the list 'items' and how it is used in various instances. E.g., row 56: request.session['items'] is populated by... items? 🤯

My code dump is here: https://tmc.mooc.fi/paste/_dWeWb5FuRqDu9bVOoIkdg


And the error code I get from TMC is 
"NoteTest: test_adding
1 != 0 : 11. note after cleanup and reloading is present: Response should not contain 'KexCSzXVcm'"


Feedback would be much appriciated. Along with any other suggestions that could improve my code 🙂
"""