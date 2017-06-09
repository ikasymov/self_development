from django.conf.urls import url

from practice import views

urlpatterns = [
	url(r'^$', views.base_page, name='base_page')
]

