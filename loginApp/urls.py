"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from loginApp import views
from loginApp.views import LoginView, RegisterView, ProfileView, EditProfileView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name = 'login'),
    path('accounts/register/', RegisterView.as_view(), name = 'Register'),
    path('accounts/logout/', LogoutView.as_view(template_name='home/registration/logged_out.html'), name='logout'),
    path('accounts/profile/', ProfileView.as_view(), name='Profile'),
    path('accounts/edit_profile/', EditProfileView.as_view(), name = 'Edit_Profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
