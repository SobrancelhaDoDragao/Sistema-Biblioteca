from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'user', views.UserNormal,basename="user")
router.register(r'all_users', views.UsersAdmin,basename="users_admin")
router.register(r'livros', views.Livros,basename="livros")
router.register(r'emprestimos', views.EmprestimoCRUD,basename="emprestimo")

urlpatterns = [
    path('',views.getRoutes.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('VerifyAuthenticated/', views.VerifyAuthenticated.as_view()),

    path('', include(router.urls)),
    path('cadastro/', views.CadastroUser.as_view(),name='cadastro'),
    path('usuarios/<int:pk>/emprestimos/', views.EmprestimoCRUD.as_view({'get':'ListarEmprestimosUsuario'})),
    path('recomendacao/', views.Livros.as_view({'get':'Recomedacao'})),
    path('novoslivros/', views.Livros.as_view({'get':'NovosLivros'}))
]

# Desativar na produção, o ngix vai servir os arquivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


