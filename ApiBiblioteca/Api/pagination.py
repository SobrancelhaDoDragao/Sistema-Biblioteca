from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from math import ceil

class PaginationToFrontEnd(PageNumberPagination):
    """
    Paginacao criada para facilitar a implementacao do front-end com algumas novas variaveis retornadas
    """

    page_size = 15

    def get_paginated_response(self, data):
        
        nextPageNumber = self.get_next_link()
        previousPageNumber = self.get_previous_link()
        PageActive = 1
        TotalPages = ceil(self.page.paginator.count/self.page_size) # Sempre será um numero inteiro arredondado para cima
        
        if(data):
            try:
                nextPageNumber = nextPageNumber.split('?')[1]
                nextPageNumber = nextPageNumber.split('=')[1]
            except:
                nextPageNumber = None
            
            try:
                previousPageNumber = previousPageNumber.split('?')[1]
                previousPageNumber = previousPageNumber.split('=')[1]
            except:
                if (previousPageNumber == None):
                    previousPageNumber = None
                else:
                    previousPageNumber = "1"

            
            if(nextPageNumber != None):
                PageActive = int(nextPageNumber) - 1
            elif(previousPageNumber != None):
                PageActive = int(previousPageNumber) + 1
            else:
                PageActive = 1

       
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'nextPageNumber':nextPageNumber,
                'previousPageNumber':previousPageNumber,
                'PageActive':str(PageActive),
                'TotalPages':TotalPages
            },
            'count': self.page.paginator.count,
            'results': data
       })


class PaginationToEmprestimo(PaginationToFrontEnd):
    """
    Paginacao customizada criada apenas para alterar o page size
    """

    page_size = 5