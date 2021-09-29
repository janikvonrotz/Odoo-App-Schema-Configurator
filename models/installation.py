from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Installation(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.installation'
    _description = 'Schematic Configurator Installation'

    # fields
    name = fields.Char()
