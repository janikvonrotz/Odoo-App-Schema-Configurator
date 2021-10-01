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
    installation_ids = fields.One2many('schematic_configurator.installation', 'room_id')
    panel_ids = fields.One2many('schematic_configurator.panel', 'room_id')
    panel_count = fields.Integer(compute='_compute_panel_count')
    installation_count = fields.Integer(compute='_compute_installation_count')

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, f'{rec.name} ({rec.level_id.name}, {rec.building_id.name})'))
        return res

    def _compute_panel_count(self):
        for rec in self:
            rec.panel_count = len(rec.panel_ids)

    def _compute_installation_count(self):
        for rec in self:
            rec.installation_count = len(rec.installation_ids)

    def action_show_details(self):
        self.ensure_one()
        view = self.env.ref('schematic_configurator.room_form')
        return {
            'name': _('%s') % self.name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'res_model': 'schematic_configurator.room',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
            'context': dict(self.env.context),
        }

    def view_installation_ids(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Installations',
            'view_mode': 'tree,form',
            'res_model': 'schematic_configurator.installation',
            'domain': [('id', 'in', [t.id for t in self.installation_ids])],
        }

    def view_panel_ids(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Panels',
            'view_mode': 'tree,form',
            'res_model': 'schematic_configurator.panel',
            'domain': [('id', 'in', [t.id for t in self.panel_ids])],
        }