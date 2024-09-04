from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .product import Product
from .category import Category
#To hide the password
from django.contrib.auth.hashers import make_password,check_password
from .customer import Customer

# Create your views here.
def home(request):
    products=Product.objects.all()
    categorys=Category.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.get_category_id(categoryID)
    else:
        products=Product.objects.all()
        data={'products':products,'categorys':categorys}
        return render(request,'index.html',data)

#signupform
def signup(request):
    if request.method== 'GET':
        return render(request,'signup.html')
    else:
        nn=request.POST['nn']
        ln=request.POST['ln']
        email=request.POST['email']
        mobile_number=request.POST['mobile_number']
        password=request.POST['password']
        # password=make_password(password)
        userdata=[nn,ln,email,mobile_number,password]   
        print(userdata)
        uservalues={
            'nn':nn,
            'ln':ln,
            'email':email,
            'mobile_number':mobile_number,

        }

        #stroing object
        customerdata=Customer(first_name=nn,last_name=ln,email=email,password=password,mobile_number=mobile_number)
        #validation
        error_msg=None
        success_msg=None
        if (not nn):
            error_msg="First Name should not be empty"
        elif (not ln):
            error_msg="Middle Name should not be empty"
        elif (not email):
            error_msg="Email1 should not be empty"
        elif (not mobile_number):
            error_msg="Mobile should not be empty"
        elif (not password):
            error_msg="Password should not be empty"
        elif (customerdata.isexit()):
            error_msg="Email Already Exists"
        if not error_msg:
            customerdata.password=make_password(customerdata.password)
            success_msg="Account Created successfully"
            customerdata.save()
            msg={"success":success_msg}
            return render(request,'signup.html',msg)
        else:
            msg={'error':error_msg,'value':uservalues}
            return render(request,'signup.html',msg)    
#login page
def  login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']   
        # To check email found or not
        users=Customer.getemail(email)
        error_msg=None
        if users:
            #if email found check password
            check=check_password(password,users.password) 
            #if password found
            if check:
                return redirect('/')
            else:
                error_msg="Password is incorrect"
                msg={'error':error_msg}
                return render(request,'login.html',msg)
        else:
            error_msg="Email is incorrect"
            msg={'error':error_msg}
            return render(request,'login.html',msg)
        
#contact
def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    else:
        # Extracting data from POST request
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Message = request.POST.get('Message')

        # Basic validation
        if not Email or not Message:
            return render(request, 'contact.html', {
                'error': 'Please fill out all fields.'
            })

        # Sending an email (you'll need to configure email backend settings in settings.py)
        try:
            send_mail(
                'New Contact Form Submission',
                Message,
                Email,  # From email
                ['your_email@example.com'],  # To email
                fail_silently=False,
            )
            return render(request, 'contact.html', {
                'success': 'Thank you for your message. We will get back to you shortly.'
            })
        except Exception as e:
            return render(request, 'contact.html', {
                'error': f'Something went wrong: {e}'
            })


                
                