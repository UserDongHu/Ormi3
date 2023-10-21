from django.urls import path, include
from rest_framework.routers import DefaultRouter # default router는 기능 많고요. simple router는 기능 적어요.
from .views import BookViewSet

router = DefaultRouter() # 어떤 라우터를 사용할건지 
router.register('', BookViewSet) # ''주소로 가면 BookViewset으로 연결하겠다.

urlpatterns = [
    path('', include(router.urls)),
] 