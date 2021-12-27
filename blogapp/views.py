from django.shortcuts import render,HttpResponseRedirect
from .forms import u_reg
from .models import registration,blog
from django.conf import settings
from django.core.mail import send_mail
import uuid
from django.contrib import messages

# if in case in mongodb the document 'id'(it is not a object _id(default)) does not exist then , delete the whole data base and create new one 

# making global and then accessing it inside the function by using global keyword
u_logged_in = False

def home(request):
    # declaring variable u_logged_in as global (it is done to use global u_logged_in)
    global u_logged_in # it is used to tell the function that we are using the global u_logged_in
    return render(request,'home.html',{"u_logged_in":u_logged_in})


def register(request):
    a = True
    o1 = u_reg()
    if request.method == "POST":

        e = request.POST.get('email')
        f_pass = request.POST.get('fi_password')
        s_pass = request.POST.get('se_password')
        o2 = u_reg(request.POST)
        if o2.is_valid():

            if registration.objects.filter(email=e,fi_password=f_pass).first(): # use filter instead of get because if there is no object that satisfies the condition then it gives error and filter returns the list of objects and .first() -> return the first object so use .first()
                a = False
                messages.error(request,"User already exist!!!")
            
            if registration.objects.filter(email = e).first():
                a = False
                messages.error(request,"Email already exist!!!")

            if f_pass != s_pass:
                messages.error(request,"Input the correct password")
                a = False
            if a:
                # send mail
                auth_token = str(uuid.uuid4())

                send_verfication_email(e,auth_token)

                u = o2.save()
                u.auth_token = auth_token
                u.save()
                messages.success(request,"Please check your g-mail to verify account...")
    return render(request,'register.html',{'form':o1})

obj = object

def login(request):
    global u_logged_in
    global obj
    a = False
    if request.method == "POST":
        c_email = request.POST.get('c_email')
        c_f_pass = request.POST.get('c_f_pass')
        c_s_pass = request.POST.get('c_s_pass')

        # i have used verified as charfield because booleanfield is giving error while i am filtering
        u_l = registration.objects.filter(email=c_email,fi_password=c_f_pass,verified="true").first()
        # u_l = registration.objects.filter(verified=True) # give error
        if u_l:
            a = True
            obj = u_l

        if(a==False):
            messages.error(request,"User not found...")

        if c_f_pass != c_s_pass:
            a=False
            messages.error(request,"Input correct password...")
        
        if a:
            u_logged_in = True
            return HttpResponseRedirect("/addblog/0")

    return render(request,'login.html')


def addblog(request,id):
    global u_logged_in
    global obj
    to_edit_blog=object
    if(u_logged_in):
        if id:
            to_edit_blog = blog.objects.get(id=id)
            if request.method =="POST":
                blog_input = request.POST.get('blog_input')
                # we can also update the data or object using only model class only we have to give id of object to which we are going to update
                if blog_input:
                    a_edit_blog = blog(id=id,u_email=to_edit_blog.u_email,blog_text=blog_input)
                    a_edit_blog.save()
                    messages.success(request,"Blog saved...")
                else:
                    messages.success(request,"Please write something in your blog...")
            
        else:
            if request.method =="POST":
                blog_input = request.POST.get("blog_input")
                if blog_input:
                    b = blog(u_email=obj.email,blog_text=blog_input)
                    b.save()
                else:
                    messages.success(request,"Please write something in your blog...")
        return render(request,"addblog.html",{"obj":obj,"to_edit_blog":to_edit_blog})

    return HttpResponseRedirect("/login")


def signout(request):
    global u_logged_in
    u_logged_in = False
    return HttpResponseRedirect("/")


def showblog(request,g_email):
    global u_logged_in
    global obj
    all_u_blogs = []
    all_blog = blog.objects.all()
    if u_logged_in:
        for blogs in all_blog:
            if blogs.u_email == g_email:
                all_u_blogs.append({"b_id":blogs.id,"blog_text":blogs.blog_text})

        return render(request,"showblog.html",{"all_u_blogs":all_u_blogs,"obj":obj})
    
    return HttpResponseRedirect("/login")


def deleteblog(request,id):
    to_delete_blog = blog.objects.get(id=id)
    to_delete_blog.delete()
    return HttpResponseRedirect("/showblog/"+to_delete_blog.u_email)


def updatepr(request,id):
    to_update_pr = ""
    a = True
    
    all_obj = registration.objects.all()
    to_update_pr = registration.objects.get(id=id)
    o1 = u_reg(instance=to_update_pr)

    if request.method == "POST":
        o2 = u_reg(request.POST,instance=to_update_pr)
        e = request.POST.get('email')
        f_pass = request.POST.get('fi_password')
        s_pass = request.POST.get('se_password')

        if o2.is_valid():
            for i in range(len(all_obj)):
                if(all_obj[i].email == e and all_obj[i].fi_password == f_pass and all_obj[i].id != id):
                    a = False
                    messages.error(request,"User already exist!!!")

            if f_pass != s_pass:
                messages.error(request,"Input the correct password...")
                a = False
            if a:
                messages.success(request,"Successfully updated!!!")
                o2.save()
        
    return render(request,"updatepr.html",{"form":o1,"to_update_pr":to_update_pr})


def send_verfication_email(email,auth_token):
    subject = "To verify account..."
    message = f'Please click the link to do verification http://127.0.0.1:8000/verify/{auth_token}'
    send_from = settings.EMAIL_HOST_USER
    receiver = [email]
    send_mail(subject,message,send_from,receiver)


def verify_email(request,token):
    to_verify_e = registration.objects.get(auth_token=token)
    
    if to_verify_e:
        # to update the object
        a = registration(id=to_verify_e.id,name=to_verify_e.name,email=to_verify_e.email,address=to_verify_e.address,country=to_verify_e.country,state=to_verify_e.state,fi_password=to_verify_e.fi_password,se_password=to_verify_e.se_password,phone=to_verify_e.phone,gender=to_verify_e.gender,is_tick=to_verify_e.is_tick,auth_token=to_verify_e.auth_token,verified="true")
        a.save()
        messages.success(request,"Email Verified!!! You can Login now...")
        return HttpResponseRedirect("/login")
    else:
        return HttpResponseRedirect("/register")