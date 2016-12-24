from django.shortcuts import render
from django.shortcuts import render_to_response , HttpResponse , redirect
from django.core.exceptions import PermissionDenied
#from django.contrib.auth.decorators import login_required
import os , json
from django.contrib.auth.models import User
from .forms import UploadFileForm
from labs import  settings
from .models import Phone
from .forms import PhoneForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def handle_uploaded_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def show(request):
     return render(request ,"index.html" , {'username' : request.user.username})



def phones_view(request):
     result = "OK!"
     if request.method == "POST" and request.POST['name']  and request.POST['manufacturer'] and request.POST['price'] and request.POST['date'] and request.POST['rate'] and request.FILES['image']:
         if request.user.is_authenticated():

             print("is_authenticated")
             form = PhoneForm(request.POST, request.FILES)
             if form.is_valid():
                 print("is_valid")
                 Phone.objects.create(name=request.POST['name'],
                                      manufacturer=request.POST['manufacturer'],
                                      price=request.POST['price'],
                                      rate=request.POST['rate'],
                                      date=request.POST['date'],
                                      image=request.FILES['image'])
             else:
                 print("Invalid")

         return render(request, "phones.html", {'result': result, 'user': request.user})

     elif request.method == "GET":
         if not Phone.objects:
             print("empty")
             return render( request , "phones.html", {'user': request.user})
         else:
             phone_list = Phone.objects.all()
             paginator = Paginator(phone_list , 6)
             page = request.GET.get('page')
             try:
                 phone = paginator.page(page)
             except PageNotAnInteger:
                 phone = paginator.page(1)
             except EmptyPage:
                 phone = paginator.page(paginator.num_pages)
             print("OK")
             return render(request , "phones.html", {'phone': phone, 'user': request.user})

     elif request.method == "DELETE" and request.user.is_superuser:
         Phone.objects.get(id=request.GET['phone']).delete()
         return HttpResponse(json.dumps({"status": "ok"}), content_type="application/json")
     elif request.method == "POST":
         return redirect('/info/show')

         '''
             if form.is_valid():

                 handle_uploaded_file(request.FILES['image'])
                 Phone.objects.create(name=request.POST['name'],
                                      manufacturer=request.POST['manufacturer'],
                                      price=request.POST['price'],
                                      rate=request.POST['rate'],
                                      date=request.POST['date'],
                                      image=request.FILES['image'])
                 return render( request , "phones.html", {'result': result , 'username':request.user.username})''''''
                 else:

                     print('Form is invalid')
         else:
             return render('/auth/login')


     elif request.method == "GET":
         if not Phone.objects :
             print("empty")
             return render_to_response("phones.html" , {'username' : request.user.username})
         else:
             print("OK")
             return render_to_response("phones.html", {'phone': Phone.objects.all() ,  'username' : request.user.username})
'''



          # phone=Phone.objects.get(id=int(path)))


def search(request):
    if request.user.is_authenticated():
        username = request.user
    else:
        username = None
    phones = Phone.objects.none()
    flag = True
    print(phones)
    if 'search' in request.GET:
        search = request.GET['search'].split()
        print(search)
        for val in search:
            if flag:
                newphones = Phone.objects.filter(name_icontains=val)
                print(newphones)
                if newphones:
                    phones = newphones
                else:
                    continue
                flag = False
            else:
                newphones = phones & Phone.objects.filter(name__icontains=val)
                if newphones:
                    phones = newphones

    return HttpResponse(json.dumps([i.dic() for i in phones]), content_type="application/javascript")


#def phone_del(request, id):
#     # if request.method == "DELETE":
#     #     try:
#     #         # user = User.phones.get(id = int(request.GET['phone']))
#     #         User.phones.through.objects.get(phone_id=int(request.GET['phone']), user_id=request.user.id).delete()
#     #     except:
#     #         print(sys.exc_info())
#     #         return HttpResponse(json.dumps({"status": "error"}), content_type="application/json")
#     # return HttpResponse(json.dumps({"status": "ok"}), content_type="application/json")
#
#
# return render(request, 'zakaz.html', args)



        #return HttpResponse("You're looking at question %s." % id)



def phone_view(request, path):
    if request.method == "GET":
        return render_to_response("phone.html" , {'phone': Phone.objects.get(id = int(path)) , 'username' : request.user.username})



def interesting(request):
    if request.method =="GET" and request.user.is_authenticated():

        return render( request , "interesting.html" , {'username' : request.user.username})
    else:
        return redirect('/auth/login/')


def view_users(request):

    if request.method == "GET" and request.user.is_superuser:
        return render(request, 'users.html', {'users':User.objects.all(), 'username' : request.user.username})


















'''    elif request.method == 'POST' and request.POST['text'] and request.user.is_authenticated():
        error = False
        if request.session.get('has_commented_already', False):
            error = "You have already commented this post!"
        else:
            Comments.objects.create(comments = request.POST['text'] , creator = request.user , phone = Phone.objects.get(id = int(path)))
            request.session['has_commented_already'] = True

        return render_to_response("phone.html", {'error': error , 'phone': Phone.objects.get(id=int(path)) , 'username' : request.user.username, 'comments':Phone.objects.get(id = int(path)).comments.all()})
    elif  request.method == 'POST' and request.POST['text'] and not request.user.is_authenticated():
        return redirect('/auth/login/')
    else:
        return render_to_response("phone.html" , {'phone' : Phone.objects.get(id = int(path))})
'''