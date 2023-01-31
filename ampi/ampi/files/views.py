from django.db.models import F
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ampi.ampi.files.models import File
from ampi.ampi.files.serializers import FileSerializer
from ampi.ampi.reports.models import Report

filter_query_params = [
    openapi.Parameter(
        name="file",
        in_=openapi.IN_FORM,
        type=openapi.TYPE_FILE,
        required=True,
    ),
    openapi.Parameter('name', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Название', required=True, ),

]


class FileViewSet(generics.RetrieveUpdateDestroyAPIView,generics.ListAPIView, GenericViewSet):
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]
    queryset = File.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=filter_query_params,
    )
    @action(detail=False, methods=['POST'],
            url_path='upload-file')
    def upload_file(self, request, *args, **kwargs):
        f = File.objects.create(
            name=self.request.query_params.get('name'),
            file=request.FILES.get('file'),
            owner=self.request.user.id,
        )

        Report.objects.create(
            id_file=f.id,
            count_down=0
        )
        return Response(status=201)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='ID', required=True)
        ]
    )
    @action(detail=False, methods=['POST'],
            url_path='download-file')
    def download_file(self, request):
        idf = self.request.query_params.get('id')
        Report.objects.filter(id_file=idf).update(count_down=F('count_down') + 1)
        qs = File.objects.filter(id=idf)
        if qs:
            res = 'http://127.0.0.1:8000/temp/' + str(qs[0]['file'])
            return Response(res)
        else:
            return Response(status=404)
