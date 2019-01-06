from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Doctor
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import DoctorForm,DoctorProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def list_view(request):
    doctor=Doctor.objects.all()
    context={
        'doctor':doctor
    }
    return render(request,'list.html',context)
class DocDetailview(DetailView):
    template_name='detailview.html'
    model=Doctor
    context_object_name = 'doctor'

def doctor_register_view(request):
    registered=False
    if request.method == "POST":
        user_form=DoctorForm(data=request.POST)
        doctor_profile = DoctorProfile(data=request.POST)

        if user_form.is_valid() and doctor_profile.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=doctor_profile.save(commit=False)
            profile.user = user
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            registered=True
        else:
            print("WTF")
    else:
        user_form = DoctorForm(data=request.POST)
        doctor_profile = DoctorProfile(data=request.POST)
    context={
        'user_form': user_form,
        'doctor_profile': doctor_profile,
        'registered': registered,
    }
    return render(request, 'register.html', context)

def doctor_login_view(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active and user.is_doctor:
                login(request,user)
                return render(request,'success.html')
            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Account does not active")
    else:
        return render(request,'login.html')


@login_required
def doctor_log_out(request):
    logout(request)
    return render(request,'logout.html')
