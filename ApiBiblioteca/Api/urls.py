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
router.register(r'users', views.UserCRUD,basename="user")
router.register(r'livros', views.LivroCRUD,basename="livro")
router.register(r'emprestimos', views.EmprestimoCRUD,basename="emprestimo")



urlpatterns = [
    path('',views.getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('VerifyAuthenticated/', views.VerifyAuthenticated.as_view()),

    path('', include(router.urls)),
    path('UserLogado/', views.UserCRUD.as_view({'get': 'UserLogadoData'})),
    path('cadastro/', views.CadastroUser.as_view(),name='cadastro'),
    path('emprestimos/', views.CadastroUser.as_view()),
    path('usuarios/<int:pk>/emprestimos/', views.ListarEmprestimosUsuario.as_view()),
    path('recomendacao/', views.Recomedacao.as_view()),
    path('novoslivros/', views.NovosLivros.as_view())
]

# Desativar na produção, o ngix vai servir os arquivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


