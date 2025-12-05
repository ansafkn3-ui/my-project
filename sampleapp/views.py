from django.shortcuts import render,HttpResponse,redirect
from .forms import Employee,Bookform,Eventform,Prodform
from .models import Books,Event,Production,college,Image,Author,Book_s,Trainer,Bookss,work

def display(request):
    return HttpResponse("welccome to django")
def show(request):
    return HttpResponse("<i>welcome home django</i>")
def home(request):
    return HttpResponse("<b>welcome django</b>")
def new(request):
    return render(request,"one.html")
def temp(request):
    a="python"
    b=[10,20,30,40,50]
    c=False
    return render(request,"two.html",
                                {"data":a,"value":b,"view":c})
def stud(request):
    a=["anju","abin","john","ashna","smith"]
    b={"name":"anju","age":25}
    c=[
        {"name":"anju","attendence":True},
    {"name":"abin","attendence":False},
    {"name":"john","attendence":True},
    {"name":"ashna","attendence":False},
    {"name":"smith","attendence":True}
     ]
    return render(request,"stud.html",
                  {"names":a,"dd":b,"attend":c})

def stat(request):
    return render(request,"three.html")

def parent(request):
    return render(request,"parent.html")

def child(request):
    return render(request,"child.html")
def child2(request):
    return render(request,"child2.html")
def index(request):
    return render(request,"index.html")

def djangoform(request):
    emp=Employee()
    return render(request,"djangoform.html",
                  {"data":emp})

def Books1(request):
    if request.method=='POST':
        z=Bookform(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("saved successfully")
    x=Bookform()
    return render(request,"books.html",{"data":x})

def bookview(request):
    x=Books.objects.all()
    return render(request,"viewbook.html",{"view":x})


def Event1(request):
    if request.method=='POST':
        z=Eventform(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("saved successfully")
    x=Eventform()
    return render(request,"events.html",{"data":x})

def eventview(request):
    x=Event.objects.all()
    return render(request,"viewevent.html",{"view":x})


def Production(request):
    if request.method=='POST':
        z=Prodform(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("saved successfully")
    x=Prodform()
    return render(request,"Production.html",{"data":x})







def deletebook(request,id):
    x=Books.objects.get(id=id)
    x.delete()
    return redirect("bookview")
    # return HttpResponse("delete successfully")

def editbook(request,id):
    x=Books.objects.get(id=id)
    if request.method=="POST":
        z=Bookform(request.POST,instance=x)
        if z.is_valid():
            z.save()
            return redirect(bookview)
        else:
                return HttpResponse("not working ")
    return render(request,"editbook.html",{"edit":x})


def collegecreate(request):
    if request.method=="POST":
        n=request.POST["name"]
        p=request.POST["place"]
        ph=request.POST["phone"]
        x=college.objects.create(name=n,place=p,phone=ph)
        x.save()
        return HttpResponse("saved successfully")
    return render(request,"college.html")

def collegeview(request):
    x=college.objects.all()
    return render(request,"viewcollege.html",{"view":x})

def deletecollege(request,id):
    x=college.objects.get(id=id)
    x.delete()
    return redirect("collegeview")
    # return HttpResponse("delete successfully")

def collegeedit(request,id):
    x=college.objects.get(id=id)
    return render(request,"collegeedit.html",{"edit":x})

def collegeupdate(request,id):
    if request.method=="POST":
        name=request.POST["name"]
        place=request.POST ["place"]
        phone=request.POST["phone"]
        x=college.objects.get(id=id)
        x.name=name
        x.place=place
        x.phone=phone
        x.save()
        return redirect ("collegeview")
    
def image_create(request):
    if request.method=="POST":
        name=request.POST["name"]
        img=request.FILES["image"]
        x=Image.objects.create(name=name,img=img)
        x.save()
        return HttpResponse("saved")
    else:
        return render(request,"image.html")
    

def Imageview(request):
    x=Image.objects.all()
    return render(request,"image_view.html",{"view":x})

def author(request):
 if request.method=="POST":
    n=request.POST["name"]
    e=request.POST["email"]
    ph=request.POST["phone"]
    x=Author.objects.create(name=n,email=e,phone=ph)
    x.save()
    return HttpResponse("saved successfully")
 return render(request,"author.html") 


def authorview(request):
    x=Author.objects.all()
    return render(request,"authorview.html",{"view":x})

def deleteauthor(request,id):
    x=Author.objects.get(id=id)
    x.delete()
    return redirect("authorview")
    # return HttpResponse("delete successfully")

def authoredit(request,id):
    x=Author.objects.get(id=id)
    return render(request,"authoredit.html",{"edit":x})

def authorupdate(request,id):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        x=Author.objects.get(id=id)
        x.name=name
        x.email=email
        x.phone=phone
        x.save()
        return HttpResponse("<script>alert('updated successfully!');window.location.href='http://127.0.0.1:8000/authorview';</script>")

def book1form(request):
    if request.method=="POST":
        author_id=request.POST['author_id']
        book_name=request.POST['book_name']
        xx=Author.objects.get(id=author_id)
        x=Book_s.objects.create(author_id=xx,book_name=book_name)
        x.save()
        return HttpResponse("worked")
    else:
        x=Author.objects.all()
        return render(request,"book1.html",{"views":x})
    
def book_view(request):
    x=Book_s.objects.all()
    return render(request,"book_view.html",{"view":x})
























def setcookie(request):
    r=HttpResponse("cookie is set")
    r.set_cookie("django","its a framework")
    return r
def getcookie(request):
    r=request.COOKIES['django']
    return HttpResponse(r)

def setsession(request):
    request.session['name']='ammu'
    return HttpResponse("session set")
def getsession(request):
    x=request.session['name']
    return HttpResponse(x)
def deletesession(request):
    del request.session['name']
    return HttpResponse("session deleted")


def homepage(request):
    return render(request,"home1.html")
def userlogin(request):
    if request.method=="POST":
        x=request.POST["username"]
        y=request.POST["password"]
        if x == "" or y == "":
            return render(request,"userlogin.html",{"error":"please enter both username and password"})
        else:
            request.session['username']=x
            return redirect(useredit)
    else:
        return render(request,"userlogin.html")
def useredit(request):
    if 'username' in request.session:
        x=request.session['username']
        return render(request,"useredit.html",{"data":x})
    else:
        return redirect(userlogin)
def userlogout(request):
    if 'username' in request.session:
        del request.session['username']
    return render(request,"home1.html",{"message":"you have been logged out"})

from sampleproject import settings
from django.core.mail import send_mail

def new_mail(request):
    subject="this is mail from django"
    msg="django is a framework"
    to="keerthanagopi112@gmail.com"
    r=send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if r==1:
        a="success"
    else:
        a="failed"
    return HttpResponse(a)

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
class Trainercreate (CreateView):
    model=Trainer
    template_name="trainercreate.html"
    fields="__all__"
    success_url="/trainercreate/"
class Trainerlist (ListView):
    model=Trainer
    template_name='trainer_list.html'
    context_object_name="a"
class Trainerdetail (DetailView):
    model=Trainer
    template_name="trainer_detail.html"
    context_object_name="a"
class Trainerupdate(UpdateView):
    model=Trainer
    template_name="trainercreate.html"
    fields="__all__"
    success_url="/trainercreate/"
    
class Trainerdelete(DeleteView):
    model=Trainer
    template_name="trainerdelete.html"
    fields="__all__"
    success_url="/trainercreate/"



def book_create_view(request):
    view=CreateView.as_view(
        model=Bookss,
        template_name="book_form.html",
        fields="__all__",
        success_url="/Bookss/"
    )
    return view(request)

def book_list_view(request):
    view=ListView.as_view(
        model=Bookss,
        template_name="book_list.html",
        context_object_name="b"
    )
    return view(request)

def book_detail_view(request,pk):
    view=DetailView.as_view(
        model=Bookss,
        template_name="book_detail.html",
        context_object_name="b"
    )
    return view(request,pk=pk)

def book_update_view(request,pk):
    view=UpdateView.as_view(
        model=Bookss,
        template_name="book_form.html",
        fields="__all__",
        success_url="/Bookss/"
    )
    return view(request,pk=pk)

def book_delete_view(request,pk):
    view=DeleteView.as_view(
        model=Bookss,
        template_name="book_delete.html",
        success_url="/Bookss/"
    )
    return view(request,pk=pk)


def today (request):
    return render (request,"today.html")

def monday(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        x=work.objects.create(name=name, gender=gender)
        x.save()
        return redirect(workview)
    else:
        return HttpResponse("not worked")
    
def workview(request):
    viewdata=work.objects.all()
    return render(request, "workview.html",{'view': viewdata})

def workedits(request,id):
    edit=work.objects.get(id=id)
    return render(request,"workedits.html",{"edit":edit})
def workdelete(request,id):
    x = work.objects.get(id=id)
    x.delete()
    return redirect(workview)
def workupdate(request,id):
    if request.method=='POST':
        ids=request.POST['name']
        gender=request.POST['gender']
        x=work.objects.get(id=id)
        x.name=ids
        x.gender=gender
        x.save()
    return redirect(workview)
    # return HttpResponse("updated successfully")
    