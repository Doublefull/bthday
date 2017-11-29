"""Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, current_datetime,current_datetime_2, ua_display_good2,ua_display_good1, hours_ahead
#from books import views
from birthdays import  views

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/', admin.site.urls),
    url(r'^time2/$', current_datetime_2),
    url(r'^good1/$', ua_display_good1),
    url(r'^good2/$', ua_display_good2),
#    url(r'^search/$',views.search),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.thanks),
    url(r'^birthday/$', views.birthday),
]
