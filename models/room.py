from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Room(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'schematic_configurator.room'
    _description = 'Schematic Configurator Room'
    _order = 'sequence'

    # fields
    name = fields.Char()
    sequence = fields.Integer()
    level_id = fields.Many2one('schematic_configurator.level', required=True)
    building_id = fields.Many2one(related='level_id.building_id')

    def action_show_details(self):
        self.ensure_one()
        view = self.env.ref('schematic_configurator.room_form')
        return {
            'name': _('%s') % self.name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_model': 'form',
            'res_model': 'schematic_configurator.room',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
            'context': dict(self.env.context),
        }