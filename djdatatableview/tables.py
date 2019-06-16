from __future__ import unicode_literals

import attr
from django.template.loader import render_to_string


@attr.s
class TableBase(object):
    structure_template = 'djdatatableview/default.html'

    id = attr.ib()
    url = attr.ib()
    method = attr.ib(default='GET')
    columns = attr.ib(default=[])

    def __str__(self):
        context = dict(
            url=self.url,
            id=self.id,
            method=self.method,
            columns=self.columns
        )

        return render_to_string(self.structure_template, context)

