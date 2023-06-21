from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

api_info = openapi.Info(
      title="Sistema biblioteca API",
      default_version='v1',
      description="Api para gerenciar acervo e emprestimo de livro em uma biblioteca",
      contact=openapi.Contact(email="eudson.duraes@gmail.com"),
      license=openapi.License(name="MIT"),
)

schema_view = get_schema_view(
  public=True,
  permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'user', views.UserNormal,basename="user")
router.register(r'all_users', views.UsersAdmin, basename="users_admin")
router.register(r'livros', views.Livros,basename="livros")
router.register(r'emprestimos', views.EmprestimoCRUD,basename="emprestimo")

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('',views.getRoutes.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('VerifyAuthenticated/', views.VerifyAuthenticated.as_view(), name='VerifyAuthenticated'),

    path('', include(router.urls)),
    path('cadastro/', views.CadastroUser.as_view(),name='cadastro'),
    path('usuarios/<int:pk>/emprestimos/', views.EmprestimoCRUD.as_view({'get':'ListarEmprestimosUsuario'}),name='all_emprestimos_users'),
    path('recomendacao/', views.Livros.as_view({'get':'Recomedacao'})),
    path('novoslivros/', views.Livros.as_view({'get':'NovosLivros'}))
]

# Desativar na produção, o ngix vai servir os arquivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


