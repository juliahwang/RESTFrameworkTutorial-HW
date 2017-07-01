from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from snippets import views

urlpatterns = [
    # SnippetHighlight 뷰와 연결
    url(r'^$', views.api_root),
    # 코드조각 리스트
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list',
        ),
    # 코드조각 디테일 페이지
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail',
        ),
    # 하이라이트된 코드조각을 볼 수 있는 페이지
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight',
        ),
    # 유저 리스트
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list',
        ),
    # 유저별 디테일 페이지
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail',
        ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# 탐색 가능한 API를 위한 로그인/로그아웃 뷰
urlpatterns += [url(r'^api-auth/', include('rest_framework.urls',
                                           namespace='rest_framework')),
]
