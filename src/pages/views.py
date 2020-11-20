from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):

	print("REQUEST IS ", request)
	print("ARGS IS ", args)
	print("KWARGS IS ", kwargs)
	# string of HTML code
	return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about airbnb",
		"my_number": 123,
		"my_list": [11, 21, 31, 24, 53]
	}
	return render(request, "about.html", my_context)