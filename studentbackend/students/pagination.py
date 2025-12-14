from rest_framework.pagination import PageNumberPagination

class StudentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'   # user can override page size
    max_page_size = 50
