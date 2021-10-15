from django.urls import path
from django.contrib.auth.models import User
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name= "mycard"

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('register', views.register, name='register'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('base/<int:id>', views.base, name='base'),
    path('showmycard/<int:id>', views.showmycard, name='showmycard'),
    path('setting/<int:id>', views.setting, name='setting'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('setting/changepro', views.changepro, name='changepro'),
    path('setting/changeprofile', views.changeprofile, name='changeprofile'),
    path('setting/changepass', views.changepass, name='changepass'),
    path('setting/changepa', views.changepa, name='changepa'),
    path('setting/addphone', views.addphone, name='addphone'),
    path('setting/adddetails', views.adddetails, name='adddetails'),
    path('setting/image_upload_view', views.image_upload_view, name='image_upload_view'),
    path('setting/IMG', views.IMG, name='IMG'),
    path('add_cat', views.add_cat, name='add_cat'),
    path('addcategory', views.addcategory, name='addcategory'),
    path('addcard', views.addcard, name='addcard'),
    path('add_card', views.add_card, name='add_card'),
    path('showlist/<int:id>', views.showlist, name='showlist'),
    path('showcard/<int:id>', views.showcard, name='showcard'),
    path('editcard/<int:id>', views.editcard, name='editcard'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('removecard/<int:id>', views.removecard, name='removecard'),
    path('removecat/<int:id>', views.removecat, name='removecat'),
]


urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)