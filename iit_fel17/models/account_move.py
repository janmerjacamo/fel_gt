from odoo import api, models, fields
from ..controllers.fel import controllerfel as confel
import logging

_logger = logging.getLogger(__name__)


class account_move(models.Model):
    _inherit = "account.move"

    fel_uuid = fields.Char(string='Autorizacion FEL Infile')  # registro electronico infile
    fel_serie = fields.Char(string='Serie FEL')  # Serie FEL
    fel_numero = fields.Char(string='Numero FEL')  # Numero Fel
    fel_certificado = fields.Char(string='Estatus FEL', default='No certificado', readonly=True) # Si esta certificado
    fel_fecha = fields.Date(string='Fecha de factura firmada') # Para registro
    fel_tipo_registro = fields.Selection(string="fel_tipo_registro", related="journal_id.fel_tipo_registro")
    fel_url = fields.Char(string="Infile", readonly=True, compute="_fel_")

    @api.model
    def create(self,vals):
        res = super(account_move, self).create(vals)

        if (res.move_type == "out_refund") and (res.state == "draft"):
            res.fel_certificado = 'No certificado'

        return res

    # def action_post(self):
    #     res = super(account_move, self).action_post()
    #     if self.journal_id.fel_tipo_registro == 'Si':
    #         confel.generaFel(self)
    #
    #
    #     return res

    def write(self, vals):
        res = super(account_move, self).write(vals)

        if self.journal_id.fel_tipo_registro == 'Si':
            if vals.get('state') == 'posted':
                confel.generaFel(self)

        return res



    def button_cancel(self):
        res = super(account_move, self).button_cancel()
        if self.journal_id.fel_tipo_registro == 'Si':
            confel.anulafel(self)

        return res

    def action_firma_fel(self):
        _logger.info("dieron click")
        if self.journal_id.fel_tipo_registro == 'Si':
            confel.generaFel(self)

    def _fel_(self):
        company = self.env['res.company'].search([('id', '=', self.env.company.id)])
        if self.fel_uuid:
            self.fel_url = company.fel_url + self.fel_uuid
        else:
            self.fel_url = 'N/A'