from django.shortcuts import render,HttpResponse
from homeapp.models import homedata
from aboutapp.models import aboutdata
from otherapp.models import services01data
from otherapp.models import services02data
from portfolioapp.models import  part01data,part02data,part03data,part04data
from blogsapp.models import  blog01data,blog02data,skilldata,footerdata,Contact
from django.shortcuts import redirect


def home(request):
    data = homedata.objects.all()[0:1]
    data01 = aboutdata.objects.all()[0:1]
    data02 = services01data.objects.all()
    data03 = services02data.objects.all()[0:1]
    data03_1 = services02data.objects.all()[1:2]
    data03_2 = services02data.objects.all()[2:3]
    data03_3 = services02data.objects.all()[3:4]
    part01 = part01data.objects.all()[0:1]
    part02 = part02data.objects.all()
    part03 = part03data.objects.all()
    part04 = part04data.objects.all()
    blog01 = blog01data.objects.all()[0:1]
    blog02 = blog02data.objects.all()
    skills = skilldata.objects.all()
    foot = footerdata.objects.all()[0:1]
    
    
    info = {
        'records1' : data,
        'records2' : data01,
        'records3' : data02,
        'records4' : data03,
        'records5' : data03_1,
        'records6' : data03_2,        
        'records7' : data03_3,
        
        'p1' : part01,
        'p2' : part02,
        'p3' : part03,
        'p4' : part04,
        
        'b01' : blog01,
        'b02' : blog02,
        'skill' : skills,
        'foot'  : foot
        
    }
    
    if request.method == "POST":
        n = request.POST.get('Name')
        last_n = request.POST.get('last_name')
        e = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        print(n,last_n,e,sub,msg)
        Contact.objects.create(name=n,
                               last_name=last_n, 
                               email=e,
                               subject=sub,
                               message=msg)
        return HttpResponse("save successfully")  
    
    
    return render(request,'home.html',info)