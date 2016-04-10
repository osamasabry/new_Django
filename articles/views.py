from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from django.conf import settings
from django.contrib.auth import authenticate , login
from .forms import *
from random import randint
from django.core.mail import send_mail , BadHeaderError
from django.shortcuts import redirect
from django.template import RequestContext
from .forms import UserForm, UserProfileForm
from django.shortcuts import render_to_response

# Create your views here.
# ******************************** register ************************************
def register(request):

    return render(request,'articles/register.html')
def registerform(request):
    return render(request,'articles/registration_form.html')

def email_register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'user_img' in request.FILES:
                profile.user_img = request.FILES['user_img']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # for make captcha
    # form_captcha = CaptchaTestForm(request.POST)

    #     # Validate the form: the captcha field will automatically
    #     # check the input
       #  if form.is_valid():
       #      human = True
       #  else:
       #      form_captcha = CaptchaTestForm()    

    # Render the template depending on the context.
    return render(request,
            'articles/email_register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def face_register(request):

    return render(request,'articles/face_register.html')

# ******************************** login ************************************

# ***********osama **********************
def signin(request):
    context = RequestContext(request)
    if "user_id" in request.session:
         return render(request, 'articles/home.html',{'user_id':request.session["user_id"]})
    else:
    # If the request is a HTTP POST, try to pull out the relevant information.
        if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
            username = request.POST['u_name']
            password = request.POST['pass']

            user = authenticate(username=username, password=password)
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    request.session["user_id"] = user.id
                    if request.POST.get('remember_me') == "checked":
                        request.session.set_test_cookie()
                        if request.session.test_cookie_worked():
                            print "cookie wokrs"
                        #set user cookie to remember when logged in again ...
                        request.COOKIES['rememberMe'] = request.POST['remember_me']
                    return render(request, 'articles/home.html',{'User':user})
                    
                else:
                    # An inactive account was used - no logging in!
                    return render(request, 'articles/activeAccount.html')
            else:
                # Bad login details were provided. So we can't log the user in.
                return render(request, 'articles/test.html')

        # The request is not a HTTP POST, so display the login form.
        # This scenario would most likely be a HTTP GET.
        else:
            # No context variables to pass to the template system, hence the
            # blank dictionary object...
            return render(request,'articles/email_login.html',  context)

# ***********osama-- signin**********************
def home(request):
    #check if the user logged in redirect to home page
    if "user_id" in request.session :
        user=request.session['user_id']
        return  render(request, 'articles/home.html',{"User":user})
    
    return render(request,'articles/home.html')

# ***********osama-- randomCode**********************    
def randomConfirm(length=3): 
    return randint(100**(length-1), (100**(length)-1))

# ***********osama-- ForgetPassword**********************

def forgetPass(request):
   
    form = forgetPassForm(request.POST or None)
    # print global_user.user_id
    if form.is_valid():

        email = form.cleaned_data.get("email")
        subject = " Hi ,Somebody recently asked to reset your Facebook password. "
        global msg
        msg = str(randomConfirm())
        print msg
        fromEmail = settings.EMAIL_HOST_USER
        toEmail = [email]
        try:
            send_mail(subject,msg,fromEmail,toEmail,fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/confirm/')

    context = {
        "form" : form,
    }
    return render(request,'articles/forgetPassword.html',{ "form" : form})

# ***********osama-- Confirm**********************

def confirm(request):
    form = confirmPassForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data.get("code")
        if code == msg :
            print code
            print msg
            return HttpResponseRedirect('/reset/')

    context = {
        "form" : form,
    }
    return render(request,'articles/confirmMail.html',{"form" : form})


#********************osama cofirm user_name***************


def confirm_User(request):
    form = confirmUserForm(request.POST or None)
    global global_user
    if form.is_valid():
        user_name = form.cleaned_data.get("username")
        users=User.objects.all()
        try:
            for user in users:
                if user.username==user_name:
                    global_user=user
                    
                    return HttpResponseRedirect('/forgetPassword/')
        except:
            return render(request,'articles/confirm_user.html',{"form" : form})

        return render(request,'articles/confirm_user.html',{"form" : form})

    return render(request,'articles/confirm_user.html',{"form" : form})

 #********************osama cofirm resetpassword***************
def reset(request):
    form = resetForm(request.POST or None)
    context = {
        "form" : form,
    }
    if form.is_valid():
        reset = form.cleaned_data.get("reset")
        confirm_reset=form.cleaned_data.get("resetconfirm")
        if reset == confirm_reset :
            u = User.objects.get(username__exact=global_user)
            u.set_password(reset)
            u.save()
            request.session["user_id"]=u.id
            return render(request,'articles/home.html')
    
    return render(request,'articles/resetpassword.html',{"form" : form})

#**************** Osama Logout******************

def logout(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()

    del request.session['user_id']

    return render(request,'articles/email_login.html')

#************************************ links **********************************
def index(request):

    return render(request,'articles/index.html')

def login(request):
    # return HttpResponse("Hello, world. You're at the article index.")
    return render(request,'articles/login.html')

    
def email_login(request):

    return render(request,'articles/email_login.html')


def face_login(request):

    return render(request,'articles/face_login.html')

# ******************************** article ************************************

def view_selected_articles(request,art_id):
    try:
        article = Article.objects.get(pk=art_id)
        comments = article.comment_set.all()
        output = "<b><font color='red'>Post  "+art_id+"</font></b><br/><br/>"
        output+= "Post Title:  <font color='blue'>"+article.art_title+"</font><br/><br/>"
        output+= "--"+article.art_content+"<br/><br/>"
        output+= "<b><font color='red'>Comments""</font></b><br/>"
        output+= "<ul>"
        for c in comments:
            output+= "<li>"+c.comment_content+"</li>"
        output+= "</ul>"
    except:
        raise Http404("Errrrrrrrror")
        # return HttpResponseNotFound("<h3>Question Not Found</h3>")

    return HttpResponse(output)


def view_all_articles(request):
    # try:

        # post = Posts.objects.get(pk=post_id)
        # comments = post.comments_set.all()
#-------------------------------------------------------------------------
        # article = Article.objects.get(pk=1)
        # comments = article.comment_set.all()
        # output = "Elsayed"
        # for x in comments:
        #   output += "<b>"+ x.Comment_content+"</b>"
        # return HttpResponse(output)
# ------------------------------------------------------------------------
        details = []
        articles = Article.objects.all()
        for article in articles:
            comments = article.comment_set.all()
            details.append(article)
            details.append(comments)

        # article = Article.objects.get(pk=1)
        # comments = article.comment_set.all()
        # output = "Elsayed"
        # for x in comments:
        #   output += "<b>"+ x.Comment_content+"</b>"
        # return HttpResponse(details)

        return render(request,"details.html", {'details':details})


        # {% for comment in profile.user.comment_set.all %}

# ********************************      ************************************        








#function osama 


# def signin(request):
#     users = User.objects.all()
#     try:
#         for user in users:
#             # check for username and pass in DB ...
#             if(user.username == request.POST['u_name'] and user.password == request.POST['pass']):
#             # the password verified for the user ...
#                 if user.is_active:
#                     request.session["user_id"] = user.id
#                     #check if the user marked the remember me checkbox to set cookie ...
#                     if request.POST.get('remember_me') == "checked":
#                         request.session.set_test_cookie()
#                         if request.session.test_cookie_worked():
#                             print "cookie wokrs"
#                         #set user cookie to remember when logged in again ...
#                         request.COOKIES['rememberMe'] = request.POST['remember_me']
#                     return render(request, 'articles/home.html',{'User':user})

#                 else:    
#                     return render(request, 'articles/activeAccount.html')                                             
#     except:
#         try:
#         	if "user_id" in request.session :
#         		return render(request, 'articles/home.html')
#         	else:
#         		return render(request, 'articles/email_login.html')	
#         except:
#         	return render(request, 'articles/email_login.html')	
       
#     return render(request, 'articles/test.html')