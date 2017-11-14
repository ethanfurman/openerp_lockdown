"""
Taken from the OpenERP forums answer by Andrey Kolpakov.
https://www.odoo.com/forum/help-1/question/how-to-remove-manage-databases-2615
"""

from web import http
from web.controllers.main import Database, db_list

class Database_restrict(Database):
    @http.jsonrequest
    def create(self, req, fields):

        # check if it is not first installation - restrict!

        dblist = db_list(req)
        if len(dblist) > 0:
            raise Exception('Not allowed')

        return super(Database_restrict, self).create(req, fields)

    @http.jsonrequest
    def duplicate(self, req, fields):
        raise Exception('Not allowed')

    @http.jsonrequest
    def drop(self, req, fields):
        raise Exception('Not allowed')

    @http.httprequest
    def backup(self, req, backup_db, backup_pwd, token):
        raise Exception('Not allowed')

    @http.httprequest
    def restore(self, req, db_file, restore_pwd, new_db):
        raise Exception('Not allowed')

    @http.jsonrequest
    def change_password(self, req, fields):
        raise Exception('Not allowed')

