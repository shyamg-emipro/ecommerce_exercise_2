from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute
from functools import reduce


class WebsiteSaleAddNewFilter(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        """
            I have overridden the shop() method to add a filter which filters the product by their brand.
        """
        res = super(WebsiteSaleAddNewFilter, self).shop(page, category, search, min_price, max_price, ppg, **post)  # Here it is calling parent method
        brand_filter = http.request.httprequest.args.getlist('brand')   # Getting the of brand attribute form every input element in the request
        brands_list = [int(x) for x in brand_filter]    # converting list of string into list of integer
        brands = http.request.env['product.brand.ept'].search([])   # gets the all the record from product.brand.ept
        res.qcontext.update({'brands': brands, 'brands_list': brands_list})     # update the qcontext of the response so that brand record can become visible
        if brands_list:     # if found that user has checked one or more brand form the list of brands
            products = http.request.env['product.template'].search([('product_brand_ept_id', 'in', brands_list)])   # find products whose brand id is in brand list
            ppr = http.request.env['website'].get_current_website().shop_ppr or 4   # added because it is required to pass value of this variable in process() method below
            ppg = http.request.env['website'].get_current_website().shop_ppg or 20  # added because it is required to pass the value of this variable into process() method and pager() method

            if res.qcontext.get('attrib_set', False):   # if found that one or more than one attribute filter is checked
                products = http.request.env['product.template'].search([('product_brand_ept_id', 'in', brands_list),
                                                                        ('id', 'in', res.qcontext.get('products').ids)])    # Get the product whose brand is from brand list and whose id is from products id which is already filtered by the parent shop() method.
            bins = TableCompute().process(products, ppg, ppr)   # get the value of bins from the product which is then used to show products in the shop page
            pager = http.request.website.pager(url="/shop", total=len(products), page=page, step=ppg, scope=7, url_args=post)   # update the pager's value according to the number of products which is then used in pagination.

            res.qcontext.update({'products': products, 'bins': bins, 'pager': pager})   # update the 'products', 'bins', 'pager' value in the qcontext dictionary
        return res
