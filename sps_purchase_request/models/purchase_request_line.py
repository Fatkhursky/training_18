# Copyright 2018-2019 ForgeFlow, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import _, api, fields, models
from odoo.exceptions import UserError

class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"

    # unit_price = fields.Float('Unit Price')

    @api.model
    def _prepare_purchase_order_line(self, name, product_id, product_qty, price_unit, po):
        return {
            'name': name,
            'product_id': product_id.id,
            'product_uom': product_id.uom_po_id.id,
            'product_qty': product_qty,
            'price_unit': price_unit,
            # 'date_planned': fields.Datetime.now(),
            # 'taxes_id': [(6, 0, taxes.ids)],
            # 'order_id': po.id,
            # 'discount': discount,
        }
    