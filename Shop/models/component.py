from odoo import api, models, fields
class ShopComponent(models.Model):
    _name = 'shop.component'
    name = fields.Char(string="Name", required=True)
    price = fields.Float(string="Price", digits=(10, 2))
    units = fields.Integer(string="Units")
    priceperunit = fields.Float(string="Price/Unit")
    provider_id = fields.Many2one('shop.provider', string="Provider")
    orderProvider_ids = fields.Many2many('shop.orderprovider', 'shop_orderprovider_component_rel', 'component_id', 'orderprovider_id', string="Order")

    @api.onchange('priceperunit', 'units')
    def _onchange_price(self):
        # set auto-changing field
        self.price = self.priceperunit * self.units
        # Can optionally return a warning and domains
        if self.price <= 0:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "It was very bad indeed",
                }
            }