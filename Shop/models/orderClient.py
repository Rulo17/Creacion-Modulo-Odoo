from odoo import api, models, fields
class ShopOrderClient(models.Model):
    _inherit = 'shop.order'
    _name = 'shop.orderclient'
    _rec_name = 'code'
    product_ids = fields.One2many('shop.product', 'orderclient_id', string="Products")
