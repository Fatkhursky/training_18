# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    tolerance_limit = fields.Float('Tolerance Limit', related='partner_id.tolerance_limit', readonly=False)
    