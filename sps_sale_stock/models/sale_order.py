# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    allow_delivery = fields.Boolean('Allow Delivery', copy=False, readonly=True, compute='_compute_allow_delivery')


    @api.depends('order_line', 'invoice_ids.payment_state', 'invoice_ids.invoice_payment_term_id')
    def _compute_allow_delivery(self):
        for order in self:
            # order.allow_delivery = True 
            allow = True
            
            order_line = order.order_line.filtered(lambda l: l.is_downpayment and l.display_type != 'line_section')
            if order_line:
                for line in order_line:
                    match = re.search(r'(?<=ref: )(.*?)(?= on)', line.name)
                    if match:
                        inv_ref = match.group()
                        invoice = order.invoice_ids.filtered(lambda i: i.name == inv_ref)
                        if invoice and invoice.payment_state != 'paid':
                            allow = False
            # for inv in order.invoice_ids:
            #     if inv.invoice_payment_term_id and not inv.invoice_payment_term_id.cod:
            #         allow = False
            if not order.payment_term_id.cod:
                allow = False

            order.allow_delivery = allow
