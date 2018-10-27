from django.shortcuts import render
from .models import Doctor
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
