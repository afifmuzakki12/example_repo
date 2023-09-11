# -*- coding: utf-8 -*-
from openerp import http

# class DymTelemarketing(http.Controller):
#     @http.route('/dym_telemarketing/dym_telemarketing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dym_telemarketing/dym_telemarketing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dym_telemarketing.listing', {
#             'root': '/dym_telemarketing/dym_telemarketing',
#             'objects': http.request.env['dym_telemarketing.dym_telemarketing'].search([]),
#         })

#     @http.route('/dym_telemarketing/dym_telemarketing/objects/<model("dym_telemarketing.dym_telemarketing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dym_telemarketing.object', {
#             'object': obj
#         })