from django.shortcuts import render

from hosts.models import Host


import pandas

# Create your views here.
def host_aggregate_view(request):
	obj = Host.objects.all()
	fields = Host._meta.fields
	
	host_acceptance_rate = []
	for i in obj:
		host_acceptance_rate.append(i.hostacceptancerate)



	context = {
		'har': host_acceptance_rate,
		'fields':fields
	}



	return render(request, "hosts/details.html", context)