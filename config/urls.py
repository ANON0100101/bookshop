from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('applications.account.urls')),
    path('api/book/', include('applications.book.urls')),

]
