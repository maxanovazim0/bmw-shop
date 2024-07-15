from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from .forms import LoginForm,SignupForm,CommentForm,mashin_yuvishForm,AddressForm,CreditCardForm
from django.contrib.auth import login, authenticate, logout
from .models import (biz_haqmizda_ga,bizning_asosiy_qoydlar,mashin_shop,modeli,
                     model_a,Comment,car,car_details,mashin_yuish_uchun,Address,CreditCard)
from django.http import Http404
from django.contrib import messages
from django.conf.urls import handler404
# Create your views here.


def car_shop(request):
    context = {
        'css':'css/car-shop.css',
        'car_shop':mashin_shop.objects.all()
    }
    return render(request,'car-shop.html',context=context)


def Home(request):
    context = {
        'css':'css/Home.css'
    }
    return render(request,'Home.html',context=context)


def mashin_yuish(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    try:
        contact_message = mashin_yuish_uchun.objects.get(user=request.user)
    except mashin_yuish_uchun.DoesNotExist:
        contact_message = None

    if request.method == 'POST':
        form = mashin_yuvishForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.user = request.user
            contact_message.save()
            text = 'sizning malmuotlaringiz saqladi'
        text = "uzur sizning malmuotlaringiz saqlmadi"

    
    else:
        form = mashin_yuvishForm()
        text = ""
    
    context = {
        'css':'css/mashin-yuvish.css',
        'form':form,
        'text':text
    }
    return render(request,'mashin-yuvish.html',context=context)


def model10(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {
        'css':'css/model10.css',
        'comment':Comment.objects.all(),
    }
    return render(request,'model10.html',context=context)


def error_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = error_404

def yetgazib_berish(request,car_detail_id):
    
    form = AddressForm
    if request.method == "POST" and car_detail_id:
        
        if not request.user.is_authenticated:
            return redirect("login")
        form = AddressForm(request.POST)
        
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.car_det = car_details.objects.get(pk=car_detail_id)
            car.save()

            return redirect("cart")

    context = {
        'css':'css/yetgazib-berish.css',
        'billing_form': form,
    }
    return render(request,'yetgazib-berish.html',context=context)

def Login(request):
    form = LoginForm()
    error = ""
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            
            data = form.cleaned_data
            
            user = authenticate(username=data["username"], password=data["password"])
            if user:
                login(request, user)

                return redirect("profile")
            
            error = "Login noto'g'ri"
    context = {
        'css':'css/login.css',
        'error':error,
        'form':form
    }
    return render(request,'login.html',context=context)

def signup(request):
    form = SignupForm()
    
    if request.method == "POST":
        password = request.POST.get("password")
        
        form = SignupForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save(commit=False)
            
            user.set_password(password)
            
            user.save()
            
            return redirect("login")
    
    context = {
        'css':'css/singnup.css',
        'form':form   
    }
    return render(request,'signup.html',context=context)

def profile(request,username=None):

    if username is not None and get_user_model().objects.filter(username=username).exists():
        user = get_user_model().objects.get(username=username)
    elif request.user.is_authenticated:
        user = request.user
    else: 
        user = None

    context = {
        'css':'css/profile.css',
        'user':user
    }
    return render(request,'profile.html',context=context)

def Logout(request):
    logout(request)
    
    return redirect("login")

def cars(request,car_model_id=None):

    context = {
        'css':'assets/css/style.css',
        'car':car.objects.all()
    }
    if car_model_id:
       context["car"] = car.objects.filter(car_sh=car_model_id)
       
    return render(request,'cars.html',context=context)

def car_detail(request,car_id):
    context = ''
    if car_id:
        context = {
        'css':'assets/css/style.css',
        'cars':car_details.objects.filter(car=car_id),
    }
    return render(request,'car-details.html',context=context)

def comment_qoshish(request):
    form = CommentForm()
    
    if request.method == "POST":
        
        if not request.user.is_authenticated:

            return redirect("login")
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            form = CommentForm()
            return redirect('model10')

    context = {
        'css':'css/singnup.css',
        'form':form
    }
    return render(request,'comment_qoshish.html',context=context)

def delete(request,comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
        if request.user == comment.user:
            comment.delete()
            return redirect('model10') 
        else:
            return HttpResponse("Siz bu kommentni o'chira olmaysiz", status=403) 
    except Comment.DoesNotExist:
        return HttpResponse("Komment topilmadi", status=404)  


def cart(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    
    if not CreditCard.objects.filter(user=request.user).exists():
        if request.method == 'POST':
            form = CreditCardForm(request.POST)
            if form.is_valid():
                card = form.save(commit=False)
                card.user = request.user
                card.save()
                text = 'Sizning kartangiz saqlandi.'
            else:
                text = 'Uzur kartani saqlashda xatolik yuz berdi.'
        else:
            form = CreditCardForm()
            text = ""
    else:
        form = CreditCardForm()
        text = "sizda karta bor"

    matn=["sizda karta bor",'Sizning kartangiz saqlandi.','Uzur kartani saqlashda xatolik yuz berdi.']
    return render(request, 'cart.html', context={'form': form, 'text': text,'matn':matn})

def cart_yangilash(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    text = ""
    form = CreditCardForm()
    if CreditCard.objects.filter(user=request.user).exists():
        card = CreditCard.objects.get(user=request.user)
        if request.method == 'POST':
            form = CreditCardForm(request.POST, instance=card)
            if form.is_valid():
                form.save()
                text = 'Sizning kartangiz yangilandi.'
            else:
                text = 'Uzur kartani yangilashda xatolik yuz berdi.'
        else:
            form = CreditCardForm(instance=card)
    else:
        return redirect('cart')
    
    matn=['Sizning kartangiz yangilandi.','Uzur kartani yangilashda xatolik yuz berdi.']
    return render(request, 'cart.html', context={'form': form, 'text': text,'matn':matn})

def hamma_model(request, m_model):

    model_map = {
        'biz_haqmizda': {
            'css':'css/Biz-haqmizda.css',
            'biz_haqmizda':biz_haqmizda_ga.objects.all(),
            'template':'Biz-haqmizda.html'
        },
        'bizning_asosiy_qoydlarmiz': {
            'css':'css/bizning-asosiy-qoydlarmiz.css',
            'bizning_asosiy_qoydlarmiz':bizning_asosiy_qoydlar.objects.all(),
            'template':'bizning-asosiy-qoydlarmiz.html'
        },
        'Galereya': {
            'css':'css/Galereya.css',
            'template':'Galereya.html'
        },
        'Komanda': {
            'css':'css/Komanda.css',
            'template':'Komanda.html'
        },
        'kontakt': {
            'css':'css/kontakt.css',
            'template':'kontakt.html'
        },
        'model': {
            'css': 'css/model.css',
            'model': modeli.objects.all(),
            'model_a': model_a.objects.all(),
            'template': 'model.html'
        },
        'model1': {
            'css': 'css/model1.css',
            'template': 'model1.html'
        },
        'model2': {
            'css': 'css/model2.css',
            'template': 'model2.html'
        },
        'model3': {
            'css': 'css/model3.css',
            'template': 'model3.html'
        },
        'model4': {
            'css': 'css/model4.css',
            'template': 'model4.html'
        },
        'model5': {
            'css': 'css/model5.css',
            'template': 'model5.html'
        },
        'model6': {
            'css': 'css/model6.css',
            'template': 'model6.html'
        },
        'model7': {
            'css': 'css/model7.css',
            'template': 'model7.html'
        },
        'model8': {
            'css': 'css/model8.css',
            'template': 'model8.html'
        },
        'model9': {
            'css': 'css/model9.css',
            'template': 'model9.html'
        },
        'model11': {
            'css': 'css/model11.css',
            'template': 'model11.html'
        },
        'Portfoliya': {
            'css':'css/Portfoliya.css',
            'template': 'Portfoliya.html'
        }
    }

    if m_model in model_map:
        context = {key: value for key, value in model_map[m_model].items() if key != 'template'}
        return render(request, model_map[m_model]['template'], context=context)
    else:
        return render(request, '404.html', status=404)

