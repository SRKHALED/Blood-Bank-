from django.shortcuts import render,redirect
from .models import Donor
from .forms import RegForm,SearchForm,LoginForm
from datetime import date

def home(request):
	template  = 'index.html'
	email,password = setSession(request)
	form = SearchForm()
	return render(request,template,{'form' : form,'email':email, 'password': password})

def showDonor(request):
	email,password = setSession(request)
	template = 'showDonor.html'
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			division = request.POST.get('division').upper()
			city = request.POST.get('city').upper()
			gender = request.POST.get('gender')
			blood = request.POST.get('blood')
			donor_list = Donor.objects.filter(division = division,city = city,
			 blood = blood, gender = gender)
			age_list=[]
			for i in donor_list:
				age = date.today() - i.date_of_birth
				age = int((age.days)/365)
				age_list.append(age)
			mylist = zip(donor_list,age_list)
			return render(request,template,{'donor_list' :mylist,'email':email,'password': password})

def reg(request):
	template = 'reg.html'
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return login(request)
			except:
				pass
	else:
		form = RegForm()
		return render(request,template,{'form' : form})

def profile(request,email,password):
	template = 'profile.html'
	try:
		donor  = Donor.objects.get(email = email, password = password)
		request.session['email'] = email
		request.session['password'] = password
		age = date.today() - donor.date_of_birth
		age = int((age.days)/365)
		return render(request,template,{'donor': donor,'email':email, 'password': password})
	except:
		return redirect('login')

def setSession(request):
	email = request.session.get('email')
	password  = request.session.get('password')
	return email,password

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		email = request.POST.get('email')
		password = request.POST.get('password')
		return redirect('profile',email = email,password = password)
	try:
		del request.session['email']
		del request.session['password']
	except:
		pass
	template = 'log_in.html'
	form = LoginForm()
	return render(request,template,{'form' : form})

def edit(request,d_id):
	email,password = setSession(request)
	template = 'update.html'
	donor = Donor.objects.get(pk = d_id)
	return render(request,template,{'donor': donor,'email':email, 'password': password})

def update(request,d_id):
	donor = Donor.objects.get(pk = d_id)
	contact = request.POST["contact"]
	email = request.POST["email"]
	division = request.POST["division"]
	city = request.POST["city"]
	address = request.POST["address"]
	password = request.POST["password"]
	if password == donor.password:
		Donor.objects.filter(pk = d_id).update(contact=contact,email = email,
			address = address,city = city,division =division)
		donor = Donor.objects.get(pk = d_id)
		return profile(request,donor.email,donor.password)
	return edit(request,d_id)