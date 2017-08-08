from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetList, SnippetDetail

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view(), name="snippet-list"),
    url(r'^snippets/(?P<pk>\d+)/$', SnippetDetail.as_view(), name="snippet-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
