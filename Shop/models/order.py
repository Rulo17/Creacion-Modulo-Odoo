from odoo import api, models, fields
class ShopOrder(models.Model):
    _name = 'shop.order'
    code = fields.Char(string="Order code", required=True)
    date = fields.Date(string="Order date", required=True)