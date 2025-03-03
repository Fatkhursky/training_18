# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'


    is_vendor = fields.Boolean(string='Is Vendor', compute='_compute_is_vendor', store=True, inverse='_inverse_is_vendor', copy=False)
    
    @api.depends('supplier_rank')
    def _compute_is_vendor(self):
        for record in self:
            record.is_vendor = record.supplier_rank > 0

    @api.depends('is_vendor')
    def _inverse_is_vendor(self):
        for record in self:
            record.supplier_rank = 1 if record.is_vendor else 0
    