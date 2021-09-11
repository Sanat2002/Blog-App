from django.shortcuts import render,HttpResponseRedirect
from .forms import u_reg
from .models import registration,blog

# making global and then accessing it inside the function by using global keyword
u_logged_in = False

def home(request):
    # declaring variable u_logged_in as global (it is done to use global u_logged_in)
    global u_logged_in # it is used to tell the function that we are using the global u_logged_in
    return render(request,'home.html',{"u_logged_in":u_logged_in})


def register(request):
    a = True
    msg = ""
    all_obj = registration.objects.all()
    o1 = u_reg()
    if request.method == "POST":
        o2 = u_reg(request.POST)
        e = request.POST.get('email')
        f_pass = request.POST.get('fi_password')
        s_pass = request.POST.get('se_password')
        if o2.is_valid():
            for i in range(len(all_obj)):
                if(all_obj[i].email == e and all_obj[i].fi_password == f_pass):
                    a = False
                    msg = "User already exist!!!"
            if f_pass != s_pass:
                msg = "Input the correct password..."
                a = False
            if a:
                msg = "Successfully registered!!!"
                o2.save()
    return render(request,'register.html',{'form':o1,'msg':msg})

obj = object

def login(request):
    global u_logged_in
    global obj
    all_obj = registration.objects.all()
    a = False
    msg = ""
    if request.method == "POST":
        c_email = request.POST.get('c_email')
        c_f_pass = request.POST.get('c_f_pass')
        c_s_pass = request.POST.get('c_s_pass')

        for i in range(len(all_obj)):
            if(all_obj[i].email == c_email and all_obj[i].fi_password == c_f_pass):
                a = True
                obj = all_obj[i]
        
        if(a==False):
            msg = "User not found..."

        if c_f_pass != c_s_pass:
            a=False
            msg = "Input correct password..."
        
        if a:
            u_logged_in = True
            return HttpResponseRedirect("/addblog/0")

    return render(request,'login.html',{"msg":msg})


def addblog(request,id):
    global u_logged_in
    global obj
    msg = ""
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
                    msg = "Blog saved..."
                else:
                    msg = "Please write something in your blog..."
            
        else:
            if request.method =="POST":
                blog_input = request.POST.get("blog_input")
                if blog_input:
                    b = blog(u_email=obj.email,blog_text=blog_input)
                    b.save()
                else:
                    msg = "Please write something in your blog..."
        return render(request,"addblog.html",{"obj":obj,"to_edit_blog":to_edit_blog,"msg":msg})

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
    msg=""
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
                    msg = "User already exist!!!"
            if f_pass != s_pass:
                msg = "Input the correct password..."
                a = False
            if a:
                msg = "Successfully updated!!!"
                o2.save()
        
    return render(request,"updatepr.html",{"form":o1,"msg":msg,"to_update_pr":to_update_pr})