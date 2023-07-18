from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'create new field in existing model by inheritance'

    test = fields.Char(string="Test")
    staff_id = fields.Many2one('rest.staff', string="Staff_Id")
