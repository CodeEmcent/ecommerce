from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView

#Static Url Configuration
from django.conf import settings
from django.conf.urls.static import static

def welcome(request):
    return JsonResponse(
        {
            "name": "Emcent E-Commerce API Documentation",
            "message": "Welcome. To View Emcent E-Commerce API Documentation, Click the Link Below.",
            "url": " ",
            "status": 200,
        }
    )


schema_view = get_schema_view(
    openapi.Info(
        title="Emcent E-Commerce API Documentation",
        default_version='v1',
        description="This is the documentation to my Emcent E-Commerce API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mcinnobezzy@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path("admin/", admin.site.urls),
    path('product/', include('product.urls')),
    path('account/', include('account.urls')),
    path('order/', include('order.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
]

handler404 = 'utils.error_views.handler404'
handler500 = 'utils.error_views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)