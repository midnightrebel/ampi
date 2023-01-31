from rest_framework import routers
from rest_framework.routers import SimpleRouter

from ampi.ampi.files.views import FileViewSet


router = SimpleRouter()
router.register('', FileViewSet, basename='')

app_name = 'files'

urlpatterns = [
    # path('/download', GetFilesView.as_view()),

]
urlpatterns += router.urls
