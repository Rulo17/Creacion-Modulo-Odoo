from odoo import api, models, fields
class ShopProduct(models.Model):
    _name = 'shop.product'
    name = fields.Char(string="Name", required=True)
    price = fields.Float(string="Price", digits=(10, 2))
    orderclient_id = fields.Many2one('shop.orderclient', string="Order")