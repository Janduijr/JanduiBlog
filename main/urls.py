from django.contrib import admin
from django.urls import path
from blog.views import index, jogador, time
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('jogador/<int:jogadores_id>/', jogador, name='jogador'),
    path('time/<int:time_id>/', time, name='time'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

