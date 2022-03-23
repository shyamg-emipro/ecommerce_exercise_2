from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale, TableCompute


class WebsiteSaleAddNewFilter(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(WebsiteSaleAddNewFilter, self).shop(page, category, search, min_price, max_price, ppg, **post)
        brand_filter = http.request.httprequest.args.getlist('brand')
        brands_list = [int(x) for x in brand_filter]
        brands = http.request.env['product.brand.ept'].search([])
        res.qcontext.update({'brands': brands, 'brands_list': brands_list})
        if brands_list:
            products = http.request.env['product.template'].search([('product_brand_ept_id', 'in', brands_list)])
            ppr = http.request.env['website'].get_current_website().shop_ppr or 4
            ppg = http.request.env['website'].get_current_website().shop_ppg or 20

            if res.qcontext.get('attrib_set', False):
                for product in res.qcontext.get('products', False):
                    if product not in products:
                        products += product
            bins = TableCompute().process(products, ppg, ppr)
            pager = http.request.website.pager(url="/shop", total=len(products), page=page, step=ppg, scope=7, url_args=post)

            res.qcontext.update({'products': products, 'bins': bins, 'pager': pager})
        return res
