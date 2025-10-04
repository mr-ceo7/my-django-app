from django.shortcuts import render,HttpResponse,redirect
from . models import Student
from django.contrib import messages

def show(request):
    return render(request,"home.html")

def all_stu(request):
    stud = Student.objects.all()
    context = {
        'studs': stud

    }
    print(context)
    return render(request,'customefab.html',context)

def register(request):
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_fathername = request.POST['s_fathername']
        s_mothername = request.POST['s_mothername']
        s_addr = request.POST['s_addr']
        s_school = request.POST['s_school']
        s_email = request.POST['s_email']
        s_gender = request.POST['s_gender']
        s_class = request.POST['s_class']
        new_stu = Student(s_name=s_name, s_fathername=s_fathername, s_mothername=s_mothername, s_addr=s_addr, s_school=s_school, s_email=s_email, s_gender=s_gender,s_class=s_class)
        new_stu.save()
        messages.success(request,"Student has been added succeffuly")
        return redirect('reg')
        
    elif request.method =='GET':
        return render(request,'services.html')        
    else:
        return HttpResponse("Exception Occured")
    

def search_stu(request):
    if request.method == 'POST':
       s_name = request.POST['s_name']
       s_fathername = request.POST['s_fathername']
       s_mothername = request.POST['s_mothername']
       stud = Student.objects.all()
       if s_name:
            studs = stud.filter (s_name__icontains = s_name)
       if s_fathername:
            studs = stud.filter(s_fathername__icontains = s_fathername)     


       if s_mothername:
            studs = stud.filter(s_mothername__icontains = s_mothername)
       context = {
                'studs': studs
                
           
        }
            
       return render(request, 'viewstudent.html', context)
       
    elif request.method == 'GET':            

          return render(request,'contact.html')
    else:
            return HttpResponse('An eception Occured')
    

def delete_stud(request, stud_id = 0):
    
    return render(request,'restoration.html')




def update_student(request):
    
    return render(request,'Performance Upgrades.html')

def STUDENT_UPDATE(request):
       
    
    return render(request, 'portfolio.html')


def review(request):
       
    
    return render(request, 'testimoniols.html')
    
        
        
        