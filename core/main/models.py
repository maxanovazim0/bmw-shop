from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


#<=============================================================================>

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/',null=True,blank=True)
    

class biz_haqmizda_ga(models.Model):
    img = models.ImageField(upload_to='rasim/')
    name = models.CharField(max_length=20)
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class bizning_asosiy_qoydlar(models.Model):
    img_orqa = models.ImageField(upload_to='img_orqa/')
    img_oldi = models.ImageField(upload_to='img_oldi/')
    name = models.CharField(max_length=50)
    sarlavha =models.CharField(max_length=100)
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.name
   

class mashin_shop(models.Model):
    img  = models.ImageField(upload_to='shop_img/')
    name = models.CharField(max_length=100)
    Seats = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    Suitcase = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.name 
    
    @property
    def hamma_car(self):
        return self.cars.all()
    
class car(models.Model):
    img = models.ImageField(upload_to='img_cars/')
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=1, max_digits=10, default=0.0)
    discount = models.DecimalField(decimal_places=1, max_digits=10, default=0.0)
    car_sh = models.ForeignKey(mashin_shop, on_delete=models.CASCADE, related_name="cars")
    km = models.IntegerField()
    cc = models.IntegerField()

    def __str__(self):
        return self.name


class VehicleImage(models.Model):
    image = models.ImageField(upload_to='vehicles/')
    car_a = models.ForeignKey('car_details',on_delete=models.CASCADE,related_name='car_a')

    def __str__(self):
        return f"Imge {self.id}"

class car_details(models.Model):
    TYPE_CHOICES = [
        ('new', 'New'),
        ('used', 'Used vehicle'),
    ]
    FUEL_CHOICES = [
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
    ]
    GEARBOX_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='used')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    first_registration = models.DateField()
    mileage = models.PositiveIntegerField()
    fuel = models.CharField(max_length=10, choices=FUEL_CHOICES, default='diesel')
    engine_size = models.PositiveIntegerField()
    power = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=10, choices=GEARBOX_CHOICES, default='manual')
    number_of_seats = models.PositiveIntegerField()
    doors = models.CharField(max_length=5)
    color = models.CharField(max_length=50)
    main_image = models.ImageField(upload_to='vehicles/')
    car = models.ForeignKey(car, on_delete=models.CASCADE, related_name="car_d")

    def __str__(self):
        return self.model 
    
    def car_hamma(self):
        return self.car_d.all()
    
    @property
    def all_images(self):
        if self.car_a.all():
            return self.car_a.all()

class modeli(models.Model):
    img = models.ImageField(upload_to='model/')
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class model_a(models.Model):
    img = models.ImageField(upload_to='model_a/')

    def __str__(self):
        return f"Img {self.id}"

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    comment_sarlavha = models.CharField(max_length=25)
    comment = models.CharField(max_length=400)

    def __str__(self):
        return f'comment shu user niki:|{self.user.username}'
    


class mashin_yuish_uchun(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Address(models.Model):
  
    country_choices = [
        ("RU", "Rossiya"),
        ("UZ", "O'ZBEKISTON"),
    ]

    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=200, choices=country_choices, default="UZ")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    car_det = models.ForeignKey(car_details,on_delete=models.CASCADE,related_name='car_det')


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.address_line1}"
    

class CreditCard(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    number = models.CharField(max_length=16)
    holder = models.CharField(max_length=20)
    expiration_month = models.CharField(max_length=2)
    expiration_year = models.CharField(max_length=4)
    ccv = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.holder} - **** **** **** {self.number[-4:]}"
    