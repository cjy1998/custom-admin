from collections import namedtuple

from django.core.paginator import InvalidPage
from rest_framework import pagination
from rest_framework.response import Response

FakePage = namedtuple('FakePage', ['object_list', 'paginator', 'number'])
class MyPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page_number'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        self.request = request
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            fake = FakePage(object_list=[], paginator=paginator, number=page_number)
            self.page = fake
            return []

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        return list(self.page)
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'page_number': self.page.number,
            'page_size': self.page_size,
            'rows': data,
        })