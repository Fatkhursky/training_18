# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    panjang = fields.Float("Panjang(M)")
    density = fields.Float("Density")
    ketebalan = fields.Float("Ketebalan (Micron)")