
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status as drf_status
from decimal import Decimal
import json
from datetime import date, datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def paginate_queryset(self, queryset, request, view=None, context=None):
        self.context = context or {}
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        """
        DRF talabi bo‘yicha Response qaytaradi,
        lekin CustomResponse.ok() uchun dict ichki formatini saqlaydi.
        """
        payload = {
            'total': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        }
        return Response(payload)  # ✅ DRF bilan mos


class CustomResponse:
    @staticmethod
    def ok(message='', data=None, status_code=drf_status.HTTP_200_OK):
        if isinstance(data, Response):
            data = data.data

        response = {
            'status': True,
            'message': message
        }

        if isinstance(data, dict) and 'total' in data and 'data' in data:
            response.update({
                'total': data.get('total'),
                'total_pages': data.get('total_pages'),
                'current_page': data.get('current_page'),
                'next': data.get('next'),
                'previous': data.get('previous'),
                'data': data.get('data')
            })
        else:
            response['data'] = data or {}

        return Response(response, status=status_code)

    @staticmethod
    def fail(message='', data=None, status_code=drf_status.HTTP_400_BAD_REQUEST):
        response_data = {
            "status": False,
            "message": message,

        }
        if data:
            response_data['data'] = data
        return Response(response_data, status=status_code)


def decimal_to_float(obj):
    if isinstance(obj, list):
        return [decimal_to_float(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: decimal_to_float(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return float(obj)
    return obj


class CleanJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, models.Model):
            return o.pk
        if isinstance(o, Decimal):
            return float(o)  # yoki str(o)
        if isinstance(o, (date, datetime)):
            return o.isoformat()
        return super().default(o)


def safe_jsonify(data):
    return json.loads(json.dumps(data, cls=CleanJSONEncoder))