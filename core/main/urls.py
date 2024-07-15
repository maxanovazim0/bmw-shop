from django.urls import path
from .views import (Home,car_shop,mashin_yuish,model10,yetgazib_berish,
                    Login,signup,profile,cars,car_detail,Logout,comment_qoshish,delete,
                    cart,cart_yangilash,hamma_model,error_404)

urlpatterns = [
    path('',Home,name='Home'),
    path('car_shop/',car_shop,name='car_shop'),
    path('mashin_yuish/',mashin_yuish,name='mashin_yuish'),
    path('comment/',model10,name='model10'),
    path("delete/comment/<int:comment_id>/", delete, name="delete_comment"),
    path('yetgazib_berish/<int:car_detail_id>/',yetgazib_berish,name='yetgazib_berish'),
    path('login/',Login,name='login'),
    path('Logout/',Logout,name='Logout'),
    path('signup/',signup,name='signup'),
    path("profile/", profile, name="profile"),
    path("profile/<str:username>/", profile, name="profile"),
    path('cars/',cars,name='cars'),
    path('cars/<int:car_model_id>/',cars,name='car_model'),
    path('car_detail/<int:car_id>/',car_detail,name='car_detail'),
    path('comment_qoshish/',comment_qoshish,name='comment_qoshish'),
    path('cart/',cart,name='cart'),
    path('cart_yangilash/',cart_yangilash,name='cart_yangilash'),
    path('hamma_model/<str:m_model>/',hamma_model,name='hamma_model'),
    path('error_404/',error_404,name='error_404')

]
