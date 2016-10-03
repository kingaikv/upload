from django.conf.urls import include, url
from django.contrib import admin
from image import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    # Examples:
    # url(r'^$', 'upload.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^$', RedirectView.as_view(url='/upload/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload', 'image.views.uploadImg'),
    url(r'^show', 'image.views.showImg'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
