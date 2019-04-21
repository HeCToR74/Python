from rest_framework.pagination import PageNumberPagination


class InterviewsPagination(PageNumberPagination):
    """Pagination with 5 items from Interviews"""

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000
