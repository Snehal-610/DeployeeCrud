from django.shortcuts import redirect,render
from .models import *
# Create your views here.
def IndexPage(request):
    if 'id' in request.session:
        data = RegisterData.objects.all()
        return render(request,"crud/index.html",{'data':data})
    else:
        return redirect("loginpage")

def RegisterPage(request):
    return render(request,'crud/Register.html')

def UpdatePage(request,pk):
    if 'id' in request.session:
        data=RegisterData.objects.get(id=pk)
        return render(request,"crud/Update.html",{'data':data})
    else:
        return redirect("loginpage")
    
def Register(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pswd']
        propic=request.FILES['profilepic']
        adata = AllData.objects.filter(AllEmail=email)
        if len(adata)>0:
            return render(request,'crud/Register.html',{'msg':'User Already Exists'})
        adata = AllData.objects.create(AllEmail=email,AllPassword=password)
        data = RegisterData.objects.create(alldata=adata,Fname=fname,Lname=lname,Email=email,Password=password,ProfilePic=propic)
        return redirect("homepage")

def Update(request,pk):
    if 'id' in request.session:
        data=RegisterData.objects.get(id=pk)
        adata=AllData.objects.get(id=data.alldata_id)
        if request.method == "POST":
            data.Fname=request.POST['fname'] if request.POST['fname'] else data.Fname
            data.Lname=request.POST['lname'] if request.POST['lname'] else data.Lname
            data.Email=request.POST['email'] if request.POST['email'] else data.Email
            data.Password=request.POST['pswd'] if request.POST['pswd'] else data.Password
            # data.ProfilePic=request.FILES['propic'] if request.FILES['propic'] else data.ProfilePic
    
            adata.AllEmail=request.POST['email'] if request.POST['email'] else adata.AllEmail
            adata.AllPassword=request.POST['pswd'] if request.POST['pswd'] else adata.AllPassword

            newpswd = request.POST['npswd']
            currentpswd = request.POST['pswd'] 
            confirmpswd = request.POST['cpswd']
            if (adata.AllPassword == currentpswd) and (data.Password == currentpswd):
                if newpswd == confirmpswd:
                    data.Password = request.POST['npswd']
                    adata.AllPassword = request.POST['npswd']
                else:
                    return render(request,"crud/Update.html",{'data':data,'msg':'Password not matched'})
            else:
                return render(request,"crud/Update.html",{'data':data,'err':'Password was wrong'})
            data.save()
            adata.save()
            return redirect("homepage")
    else:
        return redirect("loginpage")

def Delete(request,pk):
    if 'id' in request.session:
        data=RegisterData.objects.get(id=pk)
        adata=AllData.objects.get(id=data.alldata_id)
        data.delete()
        adata.delete()
        return redirect("homepage")
    else:
        return redirect("loginpage")


def LoginPage(request):
    return render(request,'crud/login.html')

def LoginUser(request):
    email=request.POST['email']
    password=request.POST['pswd']
    adata = AllData.objects.filter(AllEmail=email)
    if len(adata)>0:
        if adata[0].AllPassword == password:
            request.session['id'] = adata[0].id
            request.session['emailid'] = adata[0].AllEmail
            return redirect("homepage")
        else:
            err="Password is Incorrect !"
            return render(request,"crud/login.html",{'msg':err})
    else:
        err="User Doesn't Exist !"
        return render(request,"crud/login.html",{'msg':err})           

def LogOut(request):
    if 'id' in request.session:
        del request.session['id']
        del request.session['emailid']
        return redirect("loginpage")
    else:
        return redirect("loginpage")