from django.urls import path
from . import views
urlpatterns = [
    path("form/", views.FormCreate.as_view(), name = "form-create"),
    path("form/<int:pk>/", views.FormRetrieveUpdateDestroy.as_view(),
         name = "update"),
    
]
