from odoo import api, fields, models, _

class CreateAttendeeWizard(models.TransientModel):
    _name = 'academic.create.attendee.wizard'

    session_id = fields.Many2one(
        comodel_name="academic.session",
        string="Session",
    )

    session_ids = fields.Many2many(
        comodel_name='academic.session',
        string="Sessions",
    )

    partner_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Partners to add to session",
        required=True
    )

    def action_add_attendee(self):
        self.ensure_one()
        session = self.session_id
        att_data = [{'partner_id': att.id}
                                for att in self.partner_ids]
        #session.attendee_ids = [(0, 0, data) for data in att_data]
        for session in self.session_ids:
            session.attendee_ids = [(0, 0, data) for data in att_data]

        return {'type': 'ir.actions.act_window_close'}


        # self.partner_ids = res.partner(1,2,3)
        # [(0,0,{'partner_id':1}),(0,0,{'partner_id':2}),(0,0,{'partner_id':3})]
        # [(0,0,{'partner_id':1})]
        # [(0,0,{'partner_id':1}),          (0,0,{'partner_id':2})]
        # [(0,0,{'partner_id':1}),          (0,0,{'partner_id':2}),         (0,0,{'partner_id':3})]
