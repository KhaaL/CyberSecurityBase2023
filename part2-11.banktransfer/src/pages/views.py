from django.shortcuts import render
from django.template import loader
from django.db import transaction
from .models import Account


# Create your views here.
# 📄 Relevant documentation: https://docs.djangoproject.com/en/4.1/topics/db/transactions/#tying-transactions-to-http-requests
@transaction.atomic
def transfer(sender, receiver, amount):
	# if amount < 0 then stop.
	acc1 = Account.objects.get(iban=sender)
	acc2 = Account.objects.get(iban=receiver)
	print ("acc1 balance is ", acc1.balance)
	print ("acc2 balance is ", acc2.balance)
	print ("amount is ", amount)

	if amount < 0:
		print ("🟡 negative amount")

	elif amount > acc1.balance:
		print ("🟡 Transfer larger than the balance")

	elif acc1 == acc2:
		print ("🟡 Illegal transfer to self")


	else:
		acc1.balance -= amount
		acc2.balance += amount
		acc1.save()
		acc2.save()


def homePageView(request):
	if request.method == 'POST':
		sender = request.POST.get('from')
		receiver = request.POST.get('to')
		amount = int(request.POST.get('amount'))
		transfer(sender, receiver, amount)

	accounts = Account.objects.all()
	context = {'accounts': accounts}
	return render(request, 'pages/index.html', context)
