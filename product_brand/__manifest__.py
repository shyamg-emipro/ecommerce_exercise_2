{
    'name': 'Product Brand',
    'summary': 'Product Brand',
    'description': """
        Odoo Ecommerce Exercise 2
    """,
    'depends': ['base', 'mail', 'product', 'website_sale'],
    'data': ['security/ir.model.access.csv',
             'views/product_brand_ept.xml',
             'views/product_template.xml',
             'views/product_filter_template.xml'],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False
}
