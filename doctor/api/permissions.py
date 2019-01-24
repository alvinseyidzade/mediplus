from rest_framework.permissions import BasePermission
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self,request ,view , obj):


        return obj.user==request.user