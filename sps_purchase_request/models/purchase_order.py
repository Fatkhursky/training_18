# Copyright 2018-2019 ForgeFlow, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import _, api, fields, models
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    request_id = fields.Many2one('purchase.request', string='Request Reference', copy=False)

    @api.onchange('request_id')
    def _onchange_request_id(self):
        if not self.request_id:
            return

        self = self.with_company(self.company_id)
        request = self.request_id
        if self.partner_id:
            partner = self.partner_id
    
        if not self.origin or request.name not in self.origin.split(', '):
            if self.origin:
                if request.name:
                    self.origin = self.origin + ', ' + request.name
            else:
                self.origin = request.name
       
        order_lines = []
        for line in request.line_ids:
            # Compute name
            product_lang = line.product_id.with_context(
                lang=partner.lang or self.env.user.lang,
                partner_id=partner.id
            )
            name = product_lang.display_name
            if product_lang.description_purchase:
                name += '\n' + product_lang.description_purchase

           
            product_qty = line.product_qty
            price_unit = line.estimated_cost

            # Create PO line
            order_line_values = line._prepare_purchase_order_line(
                name=name, product_id=line.product_id, product_qty=product_qty, price_unit=price_unit, po=self)
            order_lines.append((0, 0, order_line_values))
        self.order_line = order_lines
       