from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.conf import settings
from django.shortcuts import redirect
from base import billing_db_conf
from base.sql import SELECT_SESSIONS, SELECT_HIST
import MySQLdb
def index(request):
    if not request.user.is_authenticated():
        return redirect('/base/signin')
    else:
        billing_bd=MySQLdb.connect(**billing_db_conf)
        cur=billing_bd.cursor()
        cur.execute('select count(*) from sessionsradius')
        names = [row[0] for row in cur.fetchall()]
        cur.close()
        del cur
        billing_bd.close()
        return render(request, 'base/home.html',{'content':names})

def search(request):
    if not request.user.is_authenticated():
        return redirect('/base/signin')
    else:
        if 'search' in request.GET and request.GET['search']:
            search = request.GET['search']
            billing_bd=MySQLdb.connect(**billing_db_conf)
            cur=billing_bd.cursor()
            cur.execute(SELECT_SESSIONS,(("%" + search + "%" ),))
            search=cur.fetchall()
            cur.close()
            del cur
            billing_bd.close()
            return render(request, 'base/search.html',{'search':search})
        return HttpResponse('WTF')

def hist(request):
    if 'search' in request.GET and request.GET['search']:
        sear = request.GET['search']
        billing_bd=MySQLdb.connect(**billing_db_conf)
        cur=billing_bd.cursor()
        cur.execute(SELECT_HIST,(sear,))
        sear=cur.fetchall()
        cur.close()
        del cur
        billing_bd.close()
        return render(request, 'base/hist.html',{'sear':sear})
        #return HttpResponse(sear)

def signin(request):
    if 'username' in request.POST and request.POST['username']:
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/base/')
            # Redirect to a success page.
            else:
            # Return a 'disabled account' error message
                return render(request,"base/login.html")
        else:
        # Return a 'disabled account' error message
            f='error'
            return render(request,"base/login.html")

    else:
        # Return an 'invalid login' error message.
        return render(request,"base/login.html")

def signout(request):
    logout(request)
    return redirect('/base/')

