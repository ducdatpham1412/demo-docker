from django.urls.conf import path
from . import views


urlpatterns = [
    path('', views.Ducdat.as_view())
]
