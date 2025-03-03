# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    tolerance_limit = fields.Float('Tolerance Limit', required=True)
    
    # tolerance_id = fields.Many2one('res.tolerance', string='Tolerance')

    # def action_open_tolerances(self):
    #     return {
    #         "type": "ir.actions.act_window",
    #         "name": _("Tolerance"),
    #         "res_model": "res.tolerance",
    #         "view_mode": "list,form",
    #         # "domain": [("member_id", "=", self.id)],
    #         "target": "current",
    #     }
