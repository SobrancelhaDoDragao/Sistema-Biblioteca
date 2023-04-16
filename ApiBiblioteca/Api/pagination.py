from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from math import ceil

class PaginationToFrontEnd(PageNumberPagination):
    
    def get_paginated_response(self, data):
        
        nextPageNumber = self.get_next_link()
        previousPageNumber = self.get_previous_link()
        PageActive = 0
        TotalPages = ceil(self.page.paginator.count/10) # Sempre será um numero inteiro arredondado para cima
        
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