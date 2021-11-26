from odoo import api, models, fields
class ShopClient(models.Model):
    _name = 'shop.client'
    name = fields.Char(string="Name", required=True)