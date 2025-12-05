"""
URL configuration for sampleproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sampleapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("first",views.display,name="display"),
    path("second",views.show,name="show"),
    # path("",views.home,name="home"),
    path("new",views.new,name="new"),
    path("one",views.new,name="one"),
    path("two",views.temp,name="two"),
    path("stud",views.stud,name="stud"),
    path("stat",views.stat,name="three"),
    path("parent",views.parent,name="parent.html"),
    path("child",views.child,name="child.html"),
    path("child2",views.child2,name="child2.html"),
    path("index",views.index,name="index.html"),
    path("index",views.index,name="index.html"),
    path("djangoform",views.djangoform,name="djangoform.html"),
    
    path("Book",views.Books1,name="Books1"),
    path("bookview",views.bookview,name="bookview"),
    path("Event1",views.Event,name="Event"),
    path("Production",views.Production,name="Production"),
    path("deletebook/<int:id>",views.deletebook,name="deletebook"),
    path("editbook/<int:id>",views.editbook,name="editbook"),
    path("eventview",views.eventview,name="eventview"),

    path("collegecreate",views.collegecreate,name="collegecrerate"),
    path("collegeview",views.collegeview,name="collegeview"),
    path("deletecollege/<int:id>",views.deletecollege,name="deletecollege"),
    path("collegeedit/<int:id>",views.collegeedit,name="collegeedit"),
    path("collegeupdate/<int:id>",views.collegeupdate,name="collegeupdate"),
    path("image_create",views.image_create,name="image"),
    path("Imageview",views.Imageview,name="image_view"),
    path("author",views.author,name="author.html"),
     path("authorview",views.authorview,name="authorview"),
    path("deleteauthor/<int:id>",views.deleteauthor,name="deleteauthor"),
    path("authoredit/<int:id>",views.authoredit,name="authoredit"),
    path("authorupdate/<int:id>",views.authorupdate,name="authorupdate"),
    path("book1form",views.book1form,name="book1"),
    path("new_mail",views.new_mail,name="new_mail"),








    path("setcookie",views.setcookie,name="setcookie"),
    path("getcookie",views.getcookie,name="getcookie"),
    path("setsession",views.setsession,name="setsession"),
    path("getsession",views.getsession,name="getsession"),
    path("deletesession",views.deletesession,name="deletesession"),


    path("",views.homepage,name="homepage"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("useredit",views.useredit,name="useredit"),
    path("userlogout",views.userlogout,name="userlogout"),

    path("trainercreate/create/",views.Trainercreate.as_view(),name="Trainercreate"),
    path("trainercreate/",views.Trainerlist.as_view(),name="Trainerlist"),
    path("trainercreate/<int:pk>",views.Trainerdetail.as_view(),name="Trainerdetail"),
    path("trainercreate/<int:pk>/update",views.Trainerupdate.as_view(),name="Trainerupdate"),
    path("trainercreate/<int:pk>/delete",views.Trainerdelete.as_view(),name="Trainerdelete"),




path('Bookss/create/',views.book_create_view,name="book_create_view"),
path('Bookss/',views.book_list_view,name="book_list"),
path('Bookss/<int:pk>',views.book_detail_view,name="book_detail"),
path('Bookss/<int:pk>/update',views.book_update_view,name="book_update"),
path('Bookss/<int:pk>/delete',views.book_delete_view,name="book_delete"),



path('today',views.today,name="today"),
path('monday',views.monday,name="monday"),
path('workview',views.workview,name="workview"),
path('workedits/<int:id>',views.workedits,name="workedits"),
path('workupdate/<int:id>',views.workupdate,name="workupdate"),
path('workdelete/<int:id>',views.workdelete,name="workdelete"),



]







if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("",include("sampleapp.urls")),
    # path("",views.new)
#     path("first",views.display,name="display"),
#     path("second",views.show,name="show"),
#     path("",views.home,name="home"),

# ]
