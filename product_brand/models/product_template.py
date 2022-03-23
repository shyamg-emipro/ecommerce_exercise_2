from odoo import models, fields


class ProductTemplateExtended(models.Model):
    _name = "product.template"
    _inherit = "product.template"

    # used to specify brand of the current product
    product_brand_ept_id = fields.Many2one(comodel_name="product.brand.ept", string="Product Brand", help="Brand of the current product.")
