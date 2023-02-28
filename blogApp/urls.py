"""Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import include, path
from django.conf.urls import url
from blogApp import views
from .views import HomeView
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name = 'Home'),
    path('blog/', views.blog, name = 'Blog'),
    path('blogpost/', views.blogpost, name = 'Blogpost'),
    path('portfolio/', views.portfolio, name = 'Portfolio'),
]