from rest_framework import serializers

from ampi.ampi.reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id_file', 'count_down']
