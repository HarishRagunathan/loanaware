from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('business',views.Business,name="business"),
    path('education',views.edu,name="education"),
    path('other',views.other,name="other"),
    path('search', views.loan_search, name='business_search'),
    path('profile',views.profile,name="profile")
    # path('profile',views.profile,name='profiles'),
    # path('favviewpage',views.favviewpage,name="favviewpage"),
    # path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    # path('esearch', views.Education_search, name='education_search'),
    # path('osearch', views.others_search, name='others_search'),
   
]