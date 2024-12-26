from django.urls import path
from . import views

urlpatterns = [

    path("did/it/",views.home),
    path("get/data/",views.get_data),
    path("get/<int:obj>/pics/",views.get_pics)
    # path("get/img/",views.get_pics),
    # path("get/full/data/",views.get_full_data),

]
              # + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
