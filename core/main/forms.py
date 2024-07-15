from django import forms
from django.contrib.auth import get_user_model
from .models import Comment,mashin_yuish_uchun,Address,CreditCard


class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password','image')

        widget = {
            "username":forms.TextInput(attrs={'class':'form-group',"type":"name"}),
            "email":forms.TextInput(attrs={'class':'form-group',"type":"email"}),
            "password":forms.TextInput(attrs={'class':'form-group',"type":"password"}),
        }

        labels = {
            "username": "Name",
            "email": "Email",
            "password": "Password",
            "image":'Img'
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-group", "type": "text"}), label="Ism", max_length=150)
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-group", "type": "password"}), label="Parol", max_length=200)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ("comment_sarlavha",'comment')

        widget = {
            'comment_sarlavha': forms.TextInput(attrs = {'class':'form-group','required placeholder':"name",'type':'name','id':'name'}),
            'comment':forms.Textarea(attrs={'class':'form-group','rows':"4",'cols':"50",'required placeholder':"massage",'type':'message'})
        }
        
        
        labels={
            "comment_sarlavha":'name',
            "comment":"message"
            }


class mashin_yuvishForm(forms.ModelForm):
    class Meta:
        model = mashin_yuish_uchun
        fields = ('email','name','mobile_no','date','message')
        widgets = {
            'email':forms.EmailInput(attrs={'class':"u-border-2 u-border-palette-5-dark-2 u-input u-input-rectangle", 'placeholder':"Enter a valid email address",'type':'email','id':"email-8268",'name':'email'}),
            'name':forms.TextInput(attrs={'class':"u-border-2 u-border-palette-5-dark-2 u-input u-input-rectangle",'placeholder':"Enter your Name",'type':'text','id':'name-8268','name':'name'}),
            'mobile_no':forms.TextInput(attrs={'class':"u-border-2 u-border-palette-5-dark-2 u-input u-input-rectangle",'placeholder':"+998-93-999-99-99",'type':'text','id':'name-8268','name':'Number','max_length':20}),
            'date': forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY','type':'text','id':'date-be9f','name':'date','class':"u-border-2 u-border-palette-5-dark-2 u-input u-input-rectangle",'data-date-format':"mm/dd/yyyy"}),
            'message':forms.Textarea(attrs={'placeholder':"Enter your message",'rows':"4",'cols':"50",'id':"message-8268",'name':"message",'class':"u-border-2 u-border-palette-5-dark-2 u-input u-input-rectangle"})
        }




class AddressForm(forms.ModelForm):

    class Meta:
        model = Address

        fields = [
            'first_name', 'last_name', 'email', 'mobile_no', 
            'address_line1', 'address_line2', 'country', 
            'city', 'state', 'zip_code'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class':"form-control",'type':"text",'placeholder':"John"}),
            'last_name' : forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"Doe"}),
            'email': forms.EmailInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"example@email.com"}),
            'mobile_no' : forms.TimeInput(attrs={'class':"form-control", 'type':"text",'placeholder':"+123 456 789"}),
            'address_line1' : forms.TimeInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"123 Street"}),
            'address_line2' : forms.TimeInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"123 Street"}),
            'country' : forms.TextInput(attrs={'class':"custom-select"}),
            'city' : forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"New York"}),
            'state' : forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"New York"}),
            'zip_code' : forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"123"})
        }



class CreditCardForm(forms.ModelForm):
    card_number_1 = forms.CharField(
        max_length=4, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-cart-number','id':"card-number"})
    )
    card_number_2 = forms.CharField(
        max_length=4, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-cart-number','id':"card-number-1"})
    )
    card_number_3 = forms.CharField(
        max_length=4, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-cart-number','id':"card-number-2"})
    )
    card_number_4 = forms.CharField(
        max_length=4, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-cart-number','id':"card-number-3"})
    )

    
    class Meta:
        model = CreditCard

        fields = ('holder', 'expiration_month', 'expiration_year', 'ccv')

        widgets = {
            # 'number': forms.TextInput(attrs={'maxlength': 16,'class':"input-cart-number" ,'id':"card-number"}),
            'holder': forms.TextInput(attrs={'id': 'card-holder'}),
            'expiration_month': forms.Select(attrs={'id': 'card-expiration-month'},choices=[(str(i).zfill(2), str(i).zfill(2)) for i in range(1, 13)]),
            'expiration_year': forms.Select(attrs={'id': 'card-expiration-year'},choices=[(str(i), str(i)) for i in range(2024, 2033)]),
            'ccv': forms.TextInput(attrs={'maxlength': 3, 'id': 'card-ccv'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        card_number_1 = cleaned_data.get("card_number_1")
        card_number_2 = cleaned_data.get("card_number_2")
        card_number_3 = cleaned_data.get("card_number_3")
        card_number_4 = cleaned_data.get("card_number_4")

        if card_number_1 and card_number_2 and card_number_3 and card_number_4:
            cleaned_data['number'] = f"{card_number_1}{card_number_2}{card_number_3}{card_number_4}"
        else:
            raise forms.ValidationError("All card number fields are required.")
        
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.number = self.cleaned_data['number']
        if commit:
            instance.save()
        return instance
    

