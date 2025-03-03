# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_to_approve(self):
        for order in self:
            order.write({'state': 'to approve'})

