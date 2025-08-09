from odoo import models, fields

class PickingType(models.Model):
    _inherit = 'stock.picking.type'

    code = fields.Selection(
        selection_add=[
            ('manufacturing', 'Manufacturing'),
            ('returns', 'Returns')
        ],
        ondelete={
            'manufacturing': 'cascade',
            'returns': 'cascade'
        }
    )

    return_type = fields.Selection(
        [
            ('none', 'None'),
            ('return', 'Return'),
            ('refund', 'Refund'),
        ],
        string='Return Type',
        default='none',
        ondelete={
            'none': 'set default',
            'return': 'cascade',
            'refund': 'cascade'
        }
    )

    show_reserved_qty = fields.Boolean(
        string='Show Reserved Quantity',
        default=False
    )