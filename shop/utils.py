from shop.models import Products
# from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector('product_name', 'description')
    query = SearchQuery(query)
    
    result = Products.objects.annotate(
        rank=SearchRank(vector, query)
    ).filter(rank__gt=0).order_by('-rank')
    
    result = result.annotate(
        headline=SearchHeadline(
            'product_name',
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    
    result = result.annotate(
        headline_d=SearchHeadline(
            'description',
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    
    return result
    
    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(product_name__icontains=token)
    # return Products.objects.filter(q_objects)
