from django.conf.urls import url

from . import views

# Specifying a namespace in include() without providing an app_name
app_name = 'learning_logs'

urlpatterns = [
    url(r'^$', views.index, name='index')
]
