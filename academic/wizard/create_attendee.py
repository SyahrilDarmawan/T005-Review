from odoo import api, fields, models, _
import string # Menyalakan Nama Acak
import random # Menyalakan Fungsi Random / Acak

# Menyalakan Fungsi Nama Acak atau Random Name
def generate_random_name():
        """Generate nama acak pakai huruf dan angka."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class CreateAttendeeWizard(models.TransientModel):
    _name = 'academic.create.attendee.wizard'

    name = fields.Char(string="Name", required=True)


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
        
        # Mengisi Otomatis Fungsi dari Add Attendees
        for session in self.session_ids:
            att_data = [{
                'partner_id': att.id,
                'session_id': session.id,
                'name': str(random.randint(1, 100))    # Angka acak dari 1-100
              # 'name': generate_random_name()  # Panggil fungsi buat nama random
            } for att in self.partner_ids]

            session.attendee_ids = [(0, 0, data) for data in att_data] 

        return {'type': 'ir.actions.act_window_close'}


        # self.partner_ids = res.partner(1,2,3)
        # [(0,0,{'partner_id':1}),(0,0,{'partner_id':2}),(0,0,{'partner_id':3})]
        # [(0,0,{'partner_id':1})]
        # [(0,0,{'partner_id':1}),          (0,0,{'partner_id':2})]
        # [(0,0,{'partner_id':1}),          (0,0,{'partner_id':2}),         (0,0,{'partner_id':3})]
