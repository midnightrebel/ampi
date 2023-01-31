from drf_yasg import openapi
from rest_framework import viewsets

from ampi.ampi.reports.models import Report
from ampi.ampi.reports.serializers import ReportSerializer

filter_query_params = [
    openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='ID отчета'),
]


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    permission_classes = []