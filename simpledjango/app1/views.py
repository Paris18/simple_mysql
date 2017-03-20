from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from datetime import date
from .models import User



def getlist(request):
	dd = User.objects.all()
	data = {}
	for d in dd:
		data[d.u_no] = d.name
	return render(request, "userlist.html",{'data':data})


def get_details(request):
	usr_id = request.GET['id']
	uname = request.GET['name']
	print 'hi'
	d = User.objects.get(u_no = usr_id,name = uname)
	return render(request, "userinfo.html",{'usrinfo':  {'name':d.name,'address':d.address,'dob':d.DOB ,'age':d.age,'mob_no' : d.mob_no,'email':d.email } })



def register(request):
	if request.method == 'GET':
		return render(request, "register.html",{})
	if request.POST:
		print 'hi'
		namec = request.POST['name']
		# dt = request.POST['DOB']
		dt = datetime.datetime.strptime(request.POST['DOB'], "%Y-%m-%d").date()
		adress = request.POST['adress']
		email_id = request.POST['email']
		mob_nom = request.POST['mob_no']
		today = date.today()
		ageb = today.year - dt.year -((today.month, today.day) < (dt.month, dt.day))
		# print ageb
		# print request.form
		# data = json.loads(request.body)
		# print data
		if(len(namec) == 0 or len(adress) == 0 or len(email_id) == 0):
			return render_to_response('alertmessage.html',{"message" :'all feilds are neccesory'})
		if User.objects.filter(name = namec,mob_no = mob_nom).exists():
			return HttpResponse("user already exists")
		else:
			n = User.objects.count()
			n += 1
			d = User(u_no= n,name = namec, DOB = dt, age = ageb, address = adress, mob_no = mob_nom, email = email_id)
			d.save()
			return HttpResponse("done")

