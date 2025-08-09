from odoo import models, fields

class PickingType(models.Model):
    _inherit = 'stock.picking.type'

    code = fields.Selection(selection_add=[
        ('manufacturing', 'Manufacturing'),
        ('returns', 'Returns')
    ], ondelete='set default')

    return_type = fields.Selection([
        ('none', 'None'),
        ('return', 'Return'),
        ('refund', 'Refund'),
    ], string='Return Type', default='none', ondelete='set default')

    show_reserved_qty = fields.Boolean(string='Show Reserved Quantity', default=False, ondelete='set default')
