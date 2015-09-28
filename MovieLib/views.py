from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from MovieLib.models import Movie
#from MovieLib.models import Movie, Custmer
from django.core.urlresolvers import reverse

#from MovieLib.forms import MovieMixin, MovieCreate, UserContact

#from django.http import HttpResponseRedirect

#from django.contrib import auth

from MovieLib.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
#from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login

import pdb

# Create your views here.

'''def index(request):
    return HttpResponse("Hello Django!")'''
	
class IndexView(TemplateView):
    template_name = 'index.html'

class IndexView(ListView):
    template_name = 'home.html'
   
    model = Movie

'''class IndexView(ListView):
    template_name = 'movie_list.html'

    model = Movie'''


class ListView( ListView):
    #pdb.set_trace()
    template_name = 'index.html'
    model = Movie


class CreateView(MovieCreate, CreateView):
    #pdb.set_trace()
    template_name = 'create.html'
    model = Movie
    fields = ["title","genre","release_date","price"]
    success_url = '/'
    def get_success_url(self):
        return reverse('movie_index')

class UpdateView(UpdateView):
    template_name = 'update.html'
    fields = ["title","genre","release_date","price"]
    model = Movie
    success_url = '/'
    def get_success_url(self):
        return reverse('movie_index')

class DeleteView(MovieMixin, DeleteView):
    template_name = 'delete_confirm.html'
    #fields = ["title","genre","release_date","price"]
    def get_success_url(self):
        return reverse('movie_index')

'''class CreateView(UserContact, CreateView):
    template_name = 'contact.html'
    model = Movie
    fields = ["mname","uname","email","message"]
    success_url = '/'
   # return render(request,"contact.html")

    def get_success_url(self):
        return reverse('movie_index')
        return render(request,"contact.html")'''

'''def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return render(request,"MovieLib/login.html")
       # return HttpResponseRedirect("MovieLib/template/login.html")
    else:
        # Show an error page
        return HttpResponseRedirect("/home/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/logout/")
'''

def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about_us.html")


def base(request):
    return render(request,"base_page.html")

def logout(request):
    return render(request, 'logout.html')


def cancel(request):
    return render(request, 'movie_list.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success')
    else:
        form = UserForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response('register.html', variables,)
 
def register_success(request):
    return render_to_response('success.html', )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def login(request):
    #return render(request, 'accounts/login.html', {})

    return render_to_response('accounts/login.html', { 'user': request.user }, context_instance=RequestContext(request) )
    ''' if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.get(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
            )
	    return HttpResponseRedirect('login.html')'''         



