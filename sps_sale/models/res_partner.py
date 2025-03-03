# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'


    is_customer = fields.Boolean(string='Is Customer', compute='_compute_is_customer', store=True, inverse='_inverse_is_customer', copy=False)
    
    @api.depends('customer_rank')
    def _compute_is_customer(self):
        for record in self:
            record.is_customer = record.customer_rank > 0

    @api.depends('is_customer')
    def _inverse_is_customer(self):
        for record in self:
            record.customer_rank = 1 if record.is_customer else 0
    