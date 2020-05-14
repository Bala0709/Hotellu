from django.shortcuts import render
from django.http import HttpResponse
from hotellu_app.models import User #AccessRecord,Topic,WebPage
# from hotellu_app.forms import FormName, NewUserForm, AuthUserForm, AuthUserProfileInfoForm
from hotellu_app.forms import AuthUserForm, AuthUserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_records': webpages_list}
    my_dict = {'insert_me': "Hello inside views.py file", 'number':10, 'text': [12,34,5,6]}
    return render(request, 'hotellu_app/index.html',context=my_dict)#, context=date_dict)


def user_index(request):
    user_name_list = User.objects.order_by('first_name')
    # user_name_list = User.objects.all()
    name_dict = {'names': user_name_list}
    return render(request, 'hotellu_app/users.html', context= name_dict)

def form_page(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name:" +form.cleaned_data['name'])
            print("Email:" +form.cleaned_data['email'])
            print("Text:" +form.cleaned_data['text'])



    return render(request, 'hotellu_app/forms.html', {'form':form})

def user_form(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR IN FORM')

    return render(request, 'hotellu_app/user_form.html', {'form': form})


def base_html(request):
    return render(request, 'hotellu_app/base.html')

def other_html(request):
    return render(request, 'hotellu_app/other.html')

def relative_html(request):
    return render(request, 'hotellu_app/relative_url_path.html')

def register_html(request):

    registered = False

    if request.method == "POST":
        user_form = AuthUserForm(data = request.POST)
        profile_form = AuthUserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = AuthUserForm()
        profile_form = AuthUserProfileInfoForm()


    return render(request, 'hotellu_app/registration.html', {'user_form': user_form,'profile_form': profile_form,'registered': registered})

@login_required
def special_info(request):
    return HttpResponse("You are logged in")


@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse('index'))
    return render(request, 'hotellu_app/login.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('hotellu_app/user'))
                return render(request, 'hotellu_app/index.html')

            else:
                return HttpResponse("Account not active")

        else:
            print("Logged tried logged in and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details provided")

    else:
        return render(request, 'hotellu_app/login.html', {})
