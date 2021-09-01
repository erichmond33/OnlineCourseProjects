from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("about", views.about, name="about"),
    path("join", views.join, name="join"),
    path("variations", views.variations, name='variations'),
    path("memes", views.memes, name="memes"),
    path("cycle", views.cycle, name="cycle"),
    path("atm", views.atm, name="atm"),
    path('submissions', views.submissions, name="submissions"),
    path('atm_memes', views.atm_memes, name="atm_memes"),



    # This is the ABI route
    path("abi/<int:abi_id>", views.abi, name="abi"),
    
]
