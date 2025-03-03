# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResTolerance(models.Model):
    _name = 'res.tolerance'
    # _order = 'partner_id'

    name = fields.Char('Name', compute='_compute_name', store=True)
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True)
    tolerance_limit = fields.Float('Tolerance Limit', required=True)

    @api.depends('tolerance_limit')
    def _compute_name(self):
        for record in self:
            record.name = str(record.tolerance_limit * 100) + '%' if record.tolerance_limit else False



