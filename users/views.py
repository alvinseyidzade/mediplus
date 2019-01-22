from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import OrdinaryUserForm,OrdinaryUserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse,HttpResponseRedirect
# Create your views here.




def user_register_view(request):
    registered = False
    user_form = OrdinaryUserForm(data=request.POST)
    profile_form = OrdinaryUserProfile(data=request.POST)
    if request.method == "POST":


        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        else:
            print("WTF")
    else:
        user_form = OrdinaryUserForm(data=request.POST)

    context={
        'user_form': user_form,
        "profile_form":profile_form,
        'registered': registered,
    }
    return render(request, 'ordinaryregister.html', context)
def user_login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_ordinary:
                login(request,user)
                return render(request,'success.html')
            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Account does not active")
    else:
        return render(request,'ordinarylogin.html')


@login_required
def ordinary_log_out(request):
    logout(request)
    return render(request, 'logout.html')


