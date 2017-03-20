'''
Created on 2017-03-20

@author: lishiwei
'''
from math import ceil


def paginate(data, per_page):
    """Paginate one list, return one iterator

    params:
      data    : paginated data
      per_page: page size of per page

    returns: one iterator
    """
    if type(data) != list:
        return ValueError("bad value: not list")

    total = len(data)
    page_count = ceil(total/per_page)
    for page in range(1, page_count + 1):
        yield {
            "page": page,
            "per_page": per_page,
            "total_page": page_count,
            "data": data[(page - 1) * per_page: page * per_page]
        }
