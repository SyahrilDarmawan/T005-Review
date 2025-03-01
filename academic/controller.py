from odoo import http


class main(http.Controller):
    @http.route('/web/view/edit_custom', type='json', auth="user")
    def edit_custom(self, arch):
        return {'result': True}