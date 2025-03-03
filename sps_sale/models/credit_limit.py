# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CreditLimit(models.Model):
    _name = 'credit.limit'
    # _order = 'partner_id'

    name = fields.Char('Name')
    partner_id = fields.Many2one('res.partner', string='Partner')
    type = fields.Selection([
        ('asuransi', 'Asuransi'),
        ('jaminan', 'Jaminan')
    ], string='Type', default='asuransi')
    start_date = fields.Datetime('Start Date')
    end_date = fields.Datetime('End Date')
    amount = fields.Float('Amount')

    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', compute='_compute_state')

    @api.depends('start_date', 'end_date')
    def _compute_state(self):
        for rec in self:
            state = 'active'
            if rec.end_date and rec.end_date < fields.Datetime.now():
                state= 'inactive'
            rec.state = state


