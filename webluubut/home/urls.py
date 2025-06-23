from django.urls import path
from home import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home, name = "home"),
    path('new', views.newhome, name = "new"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('send', views.subhome, name='send'),
    path('list/<int:id>', views.listhome, name='list'),
]