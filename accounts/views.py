from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from travello.models import Contact , Trips , Destination

from .forms import SearchForm
# Create your views here.

def login(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):

    if request.method =="POST":
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        
        if password1 == password2:  
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print('User created')
        else:
            messages.info(request,'passwords are not matching')
            return redirect('register')
        return redirect('login')
    else:
        return render(request,'register.html')


def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']

        cont = Contact(name=name,email=email,message=message,subject=subject)
        cont.save()
        return redirect('/')
    else:
        return render(request,"contact.html")
    
def trips(request):
    if request.method =="POST":
        name = request.POST['name']
        ph_num = request.POST['ph_num']
        place = request.POST['place']
        img = request.FILES['trip_pic']
        date = request.POST['date']
        mess = request.POST['messag']

        cont = Trips(name=name,phone_number=ph_num,date=date,place=place,description=mess,img=img)
        cont.save()
        return redirect('/')
    else:
        return render(request,"trips.html")




def search_view(request):
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():
        destination = form.cleaned_data.get('destination')
        checkin = form.cleaned_data.get('checkin')
        checkout = form.cleaned_data.get('checkout')
        guests = form.cleaned_data.get('guests')

        results = Destination.objects.all()

        if destination:
            results = results.filter(name__icontains=destination)

        # Add additional filters as needed
        # if checkin and checkout:
        #     results = results.filter(availability__date__range=(checkin, checkout))

        # if guests:
        #     results = results.filter(max_guests__gte=guests)

    context = {
        'form': form,
        'results': results
    }
    return render(request, 'search.html', context)
def about(request):
    return render(request,"about.html")

