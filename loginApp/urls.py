"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from loginApp import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/', views.login_request, name = 'login'),
    path('accounts/register/', views.register, name = 'Register'),
    path('accounts/logout/', LogoutView.as_view(template_name='home/registration/logged_out.html'), name='logout'),
    path('accounts/my_profile/', views.myProfile, name="My_Profile"),
    path('accounts/edit_profile/', views.editProfile, name = 'Edit_Profile'),
    path('accounts/edit_bw/', views.editBW, name="Edit_BW"),
    path('accounts/add_avatar/', views.addAvatar, name= "Add_Avatar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# [
#     path('cuentas/password_change/done/', views.password_change_done, name = 'password_done'),
#     path('cuentas/', views.contacto, name = "Formulario_Contacto"),
#     path('contactook/', views.contacto_enviado, name = "Contacto_Enviado"),

# ]