from odoo import models, fields, api

class WizardMessage(models.TransientModel):
    _name = 'wizard.message'
    _description = 'Notification Message'

    message = fields.Text(string="Message", readonly=True)

    def action_close(self):
        return {'type': 'ir.actions.act_window_close'}
