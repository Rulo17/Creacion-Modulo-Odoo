# -*- coding: utf-8 -*-
{
    'name': "ShopModule",
    'summary': """Shop management""",
    'description': """A shop that is more like a business.""",
    'author': "Raul Rodriguez",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Practice',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/component.xml',
        'views/provider.xml',
        'views/product.xml',
        'views/client.xml',
        'views/orderClient.xml',
        'views/orderProvider.xml'
        ],
}