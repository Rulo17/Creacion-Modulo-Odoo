from odoo import api, models, fields
class ShopProvider(models.Model):
    _name = 'shop.provider'
    name = fields.Char(string="Name", required=True)
    component_ids = fields.One2many('shop.component', 'provider_id', string="Components")
    _sql_constraints = [('name', 'UNIQUE (name)', "There is already a provider with that name")]