from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from snippets import views

# 라우터 생성
router = DefaultRouter()
# 라우터에 뷰셋 등록
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API url을 라우터가 자동으로 인식한다.
# 추가로 탐색가능한 API를 구현하기 위해 로그인에 사용할 url은 따로 직접 설정.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth', include(
        'rest_framework.urls',
        namespace='rest_framework'))
]
