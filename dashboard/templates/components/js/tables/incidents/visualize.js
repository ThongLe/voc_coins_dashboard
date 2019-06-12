{% load staticfiles i18n %}

tables.incidentsTable = createTable(
    '#incidents-table',
    [],
    [
        {name: 'incident_no'},
        {name: 'type_name'},
        {
            name: 'incident_priority',
            render: function ( data, type, row, meta ) {
                if (data == 'U')
                    return '<input type="checkbox" checked disabled>';
                return '<input type="checkbox" disabled>';
            }
        },
        {name: 'dispatchdt'},
        {name: 'correct_arrivaldt'},
    ]
);