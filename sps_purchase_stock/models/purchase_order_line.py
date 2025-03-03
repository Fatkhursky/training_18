# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'


    tolerance_receipt_qty = fields.Float(string='Tolerance QTY', compute='_compute_tolerence_qty')

    @api.depends('order_id.tolerance_limit','product_qty')
    def _compute_tolerence_qty(self):
        for rec in self:
            qty = 0
            # rec.tolerance_receipt_qty = rec.order_id.tolerance_limit * 100 > 0 if rec.product_qty + rec.product_qty * rec.order_id.tolerance_limit else 0
            if rec.order_id.tolerance_limit * 100 > 0:
                qty = rec.product_qty + rec.product_qty * rec.order_id.tolerance_limit
            rec.tolerance_receipt_qty = qty