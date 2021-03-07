from django.shortcuts import render
from doctor.forms import DrForm, DrProfileForm
from django.views import generic
#import for login and loguot functionality
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

def register(request):
    registered = False

    if request.method == 'POST':
        dr_form = DrForm(data=request.POST)
        dr_profile_form = DrProfileForm(data=request.POST)

        if dr_form.is_valid() and dr_profile_form.is_valid():
            dr = dr_form.save()
            dr.set_password(dr.password) # Hashing the password
            dr.save()

            profile = dr_profile_form.save(commit=False)
            profile.user = dr

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(dr_form.errors,dr_profile_form.errors)
    else:
        dr_form = DrForm()
        dr_profile_form = DrProfileForm()

    context = {'DrForm':dr_form, 'DrProfileForm':dr_profile_form, 'registered':registered}
    return render(request,'registration.html',context)


def dr_login(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return response("Account is not active! Cntact your admin.")
        else:
            print("Authentication faised for {}".format(username))
            return HttpResponse("Authentication failed, Please enter correct credentials!")
    else:
        return render(request,'login.html',{})


@login_required
def dr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in successfully!")
