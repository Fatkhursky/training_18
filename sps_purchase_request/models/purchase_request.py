# Copyright 2018-2019 ForgeFlow, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import _, api, fields, models
from odoo.exceptions import UserError
# _STATES = [
#     ("draft", "Draft"),
#     ("to_approve", "To be approved"),
#     ("approved", "Approved"),
#     ("rejected", "Rejected"),
#     ("done", "Done"),
# ]

class PurchaseRequest(models.Model):
    _inherit = "purchase.request"

    def read(self, fields=None, load='_classic_read'):
        """Memastikan fungsi dipanggil setiap kali record dibaca (misalnya, saat refresh)."""
        res = super().read(fields, load)
        self._compute_purchase_request_status()
        return res
    
    # @api.depends('line_ids.purchase_lines.order_id.state', 'line_ids.product_qty', 'line_ids.purchased_qty')
    # def _compute_purchase_request_status(self):
    #     for pr in self:
    #         line_ids = pr.line_ids
    #         if pr.state == 'approved':
    #             if line_ids and line_ids.mapped('product_qty') == line_ids.mapped('purchased_qty'):
    #                 purchases = line_ids.purchase_lines.filtered(lambda x: x.order_id.state != 'cancel')
    #                 if all(state in ['purchase', 'done'] for state in purchases.mapped('state')):
    #                     pr.state = 'done'
    #         if pr.state == 'done':
    #             if line_ids and line_ids.mapped('product_qty') == line_ids.mapped('purchased_qty'):
    #                 purchases = line_ids.purchase_lines.filtered(lambda x: x.order_id.state != 'cancel')
    #                 if not all(state in ['purchase', 'done'] for state in purchases.mapped('state')):
    #                     pr.state = 'approved'

    @api.depends('line_ids.purchase_lines.order_id.state', 'line_ids.product_qty', 'line_ids.purchased_qty')
    def _compute_purchase_request_status(self):
        for pr in self:
            if not pr.line_ids:
                continue

            product_qty_list = pr.line_ids.mapped('product_qty')
            purchased_qty_list = pr.line_ids.mapped('purchased_qty')
            purchases = pr.line_ids.purchase_lines.filtered(lambda x: x.order_id.state != 'cancel')
            purchase_states = purchases.mapped('state')

            if product_qty_list == purchased_qty_list:
                if pr.state == 'approved' and all(state in ['purchase', 'done'] for state in purchase_states):
                    pr.state = 'done'
                elif pr.state == 'done' and not all(state in ['purchase', 'done'] for state in purchase_states):
                    pr.state = 'approved'