"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from school.views import EUserViewSet, ScoreViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="softmediaLab example api",
        default_version='v1',
        description="Обновленный схемогенератор drf_yasg. Доступен генератор на Swagger и на Redoc (/api/docs/redoc/)",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ivanvalenkov@gmail.com"),
        # license=openapi.License(name=""),

    ),
    # public=False,
    url=f'http://exapmle.url',
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'users', EUserViewSet)

router.register(r'scores', ScoreViewSet)

urlpatterns = [

                  re_path('^api/docs/swagger(?P<format>\\.json|\\.yaml)$', schema_view.without_ui(cache_timeout=60), name='schema-json'),
                  path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=60), name='schema-redoc'),
                  path('docs/', schema_view.with_ui('swagger', cache_timeout=60), name='schema-swagger-ui'),

                  url(r'^api-auth', include("rest_framework.urls")),
                  url(r'^', include(router.urls)),

                  # provide the most basic login/logout functionality
                  url(r'^login/$', auth_views.LoginView.as_view(template_name='core/login.html'),
                      name='core_login'),
                  url(r'^logout/$', auth_views.LogoutView.as_view(), name='core_logout'),

                  # enable the admin interface
                  url(r'^admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
