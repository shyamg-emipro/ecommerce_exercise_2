from odoo import models, fields


class ProductBrandEpt(models.Model):
    _name = "product.brand.ept"
    _description = "Product Brand Ept"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    """
        Specifies the brand of products
    """

    name = fields.Char(string="Name", help="Name of the Brand")     # name of the brand
    website_id = fields.Many2one(comodel_name="website", string="Website", help="Website on which you want to add this brand.")     # Website in which this brand is visible
    product_tmpl_ids = fields.One2many(comodel_name="product.template", inverse_name="product_brand_ept_id", string="Products", help="Products of the current Brand.")      # Products of the current brand
    logo = fields.Image(string="Logo", help="Please, Select the logo for the brand")    # logo of the brand
