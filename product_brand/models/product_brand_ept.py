from odoo import models, fields


class ProductBrandEpt(models.Model):
    _name = "product.brand.ept"
    _description = "Product Brand Ept"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", help="Name of the Brand")
    website_id = fields.Many2one(comodel_name="website", string="Website", help="Website on which you want to add this brand.")
    product_tmpl_ids = fields.One2many(comodel_name="product.template", inverse_name="product_brand_ept_id", string="Products", help="Products of the current Brand.")
    logo = fields.Image(string="Logo", help="Please, Select the logo for the brand")
