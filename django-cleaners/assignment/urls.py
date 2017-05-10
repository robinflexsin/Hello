from django.conf.urls import include, url
from django.contrib import admin
from main import views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cleaners/', include('cleaners.urls', namespace='cleaners')),
    url(r'^customers/', include('customers.urls', namespace='customers')),
    url(r'^$', main_views.home),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^login/', include('bookings.urls', namespace='main')),
]
