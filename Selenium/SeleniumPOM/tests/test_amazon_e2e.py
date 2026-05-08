
import pytest

from pages.home_page import Homepage
from pages.product_listing_page import ProductListingPage


@pytest.mark.parametrize(("searchproduct","brandname","mensize"),
[
     ("shoes",'Nike','9')
])

def test_product_ordering(driver, searchproduct,brandname,mensize):
    homepage = Homepage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Search Product - {searchproduct}")
    homepage.click_search_button()


    assert homepage.is_amazon_page_loaded(), 'Search results page did not load.'
    print(f"\nSearch results page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)

    print(f"Applying Brand Filter-{brandname}")
    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand filter did not apply '

    print(f"Apllying size Filter for men shoes - {mensize}")
    productlistingpage.select_brand_filter(mensize)

    assert productlistingpage.check_size_in_title(mensize), 'Mensize filter did not apply'

