from django.shortcuts import render
from doctor.forms import DrForm, DrProfileForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

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
