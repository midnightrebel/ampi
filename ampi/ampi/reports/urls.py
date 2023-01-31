from rest_framework import routers

from ampi.ampi.reports.views import ReportViewSet


app_name = ''

router = routers.DefaultRouter()
router.register(r'', ReportViewSet)

urlpatterns = []
urlpatterns += router.urls
