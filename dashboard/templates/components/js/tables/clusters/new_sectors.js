{% load staticfiles i18n %}

tables.sectorsTable = createTable(
    '#sectors-table',
    [],
    [
        {name: 'code'},
        {name: 'name'},
        {name: 'division'},
        {
            name: 'remove_sector',
            render: function renderColumn( data, type, row, meta ) {
                return '<a onClick="removeSectorRow(\'' + data + '\')"><span class="glyphicon glyphicon-remove-circle"></span></a>';
            }
        },
    ]
);