from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views import View

class UserView(View):
    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(id=kwargs['pk'])
        return render(request, 'user.html', {'user': user})