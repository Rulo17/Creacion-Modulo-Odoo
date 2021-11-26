from odoo import api, models, fields
class ShopOrderProvider(models.Model):
    _inherit = 'shop.order'
    _name = 'shop.orderprovider'
    _rec_name = 'code'
    component_ids = fields.Many2many('shop.component', 'shop_orderprovider_component_rel', 'orderprovider_id', 'component_id', string="Component")
