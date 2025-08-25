from rest_framework.pagination import PageNumberPagination

class BlogPagination(PageNumberPagination):
    page_size =15
    page_query_param = "p_size"
    max_page_size = 100


