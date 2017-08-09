from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    SnippetList, SnippetDetail,
    SnippetHighlight, api_root,
    UserList, UserDetail
    )

urlpatterns = [
    url(r'^$', api_root),
    url(r'^snippets/$', SnippetList.as_view(), name="snippet-list"),
    url(r'^snippets/(?P<pk>\d+)/$', SnippetDetail.as_view(), name="snippet-detail"),
    url(r'^snippets/(?P<pk>\d+)/highlight/$', SnippetHighlight.as_view(), name="snippet-highlight"),
    url(r'^users/$', UserList.as_view(), name="user-list"),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
