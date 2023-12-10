import requests
from config.enums import PageSize, SortOrder, AuctionCategory, ProductCategory

BASE_URL = "https://kotnauction.com"

def get_products_page_url(
    auctionCategory: AuctionCategory = AuctionCategory.All,
    pageSize: PageSize = PageSize.TwentyFive,
    sortOrder: SortOrder = SortOrder.EndingSoon,
    searchQuery: str = "",
    productCategory: ProductCategory = ProductCategory.All,
    pageNumber: int = 1
):
    return f"""
        {BASE_URL}
        /auctions
        /{auctionCategory}
        ?category={productCategory}
        &order_by={sortOrder}
        &per_page={pageSize}
        &page={pageNumber}
        &find={searchQuery}
    """

def get_home_page():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.content
    
def get_products_page(page_url):
    response = requests.get(page_url)
    if response.content:
        return response.content