from rest_framework import routers
from ampi.ampi.users.views import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='')

urlpatterns = []
urlpatterns += router.urls
