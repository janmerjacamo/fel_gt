from odoo import api, models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    fel_tipo_registro = fields.Selection([('No', 'No'), ('Si', 'Si')], default='No', string='Emite FEL')
    fel_tipo_fel = fields.Char(string='Documento SAT')
    fel_retencion_isr = fields.Float(string='Retencion ISR (%)', default=0.00)
    fel_frases = fields.One2many(comodel_name='fel.account.journal.frases', inverse_name='fel_account_journal_id')



class ResAccountJournalFrases(models.Model):
    _name = 'fel.account.journal.frases'

    fel_account_journal_id = fields.Many2one(comodel_name='account.journal')
    fel_frases_codigo_escenario = fields.Char(string="Codigo Escenario", required=True)
    fel_frases_tipo_frase = fields.Char(string="Tipo Frase", required=True)