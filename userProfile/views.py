from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth.models import User

#import Group for assign Users
from django.contrib.auth.models import Group

#Now use SignUpForm there for create user
from .forms import SignUpForm, LoginForm, PassChangeForm, UserUpdate, ProfileUpdate

# import this for login, logout and authenticate
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# for Changing password, now we will not import passwordChangeForm there
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, UserChangeForm

# Create your views here.
def usercreate(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            #form.save()
            #First create author n Manager groups and give permission in both according to us
            # assign in a group, but first import Group and then this code for aasign createuser in Author
            user = form.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            messages.success(request, "Your Account is Created.")
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfully Logged In")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, "user/login.html", {'form': form})

    else:
        return redirect('/')

# first import UserChangeForm
def user_dashboard(request):
    if request.user.is_authenticated:
        #get all groups Info not User in group
        #group_name = Group.objects.values_list()
        #group = list(group_name)
        #print(group)

        #get user's group info, but first import User and then get in template
        group = request.user.groups.all()

        # for profile
        if request.method == "POST":
            u_form = UserUpdate(request.POST, instance=request.user)
            p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()

        else:
            u_form = UserUpdate(instance=request.user)
            p_form = ProfileUpdate(instance=request.user.profile)

        return render(request, "user/dashboard.html", {'name': request.user, 'group': group, 'u_form': u_form,
                                                       'p_form': p_form})
    else:
        return HttpResponseRedirect('/login/')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("/")

def user_update(request):
    if request.user.is_authenticated:
        post_list = Post.objects.all()

        #get all groups Info not User in group
        #group_name = Group.objects.values_list()
        #group = list(group_name)
        #print(group)

        #get user's group info, but first import User and then get in template
        group = request.user.groups.all()

        # for profile
        if request.method == "POST":
            u_form = UserUpdate(request.POST, instance=request.user)
            p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()

        else:
            u_form = UserUpdate(instance=request.user)
            p_form = ProfileUpdate(instance=request.user.profile)

        return render(request, "home/userupdate.html", {'name':request.user, 'posts':post_list, 'group':group, 'u_form':u_form, 'p_form':p_form})
    else:
        return HttpResponseRedirect('/login/')

#change password with old password, and import from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
def user_change_pass(request):
    if request.method == "POST":
        fm = PassChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            #first import update session auth, and now forcefully logout after change password
            update_session_auth_hash(request, fm.user)
            messages.success(request, "Password Change Successfully")
            return HttpResponseRedirect("/profile/")
    else:
        fm = PassChangeForm(user=request.user)
    return render(request, "user/resetPass.html", {'form': fm})

#change password without old password, and import from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
#def user_change_pass1(request):
    # if we dont want chnage password without old password then we only change 1 thing
    # PasswordChangeForm()  =  SetPasswordForm()
