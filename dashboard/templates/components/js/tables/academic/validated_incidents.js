{% load staticfiles i18n %}

tables.detailTable = createTable(
    '#details-table',
    [],
    [
        {name: 'id'},
        {name: 'start_time'},
        {
            name: 'urgent',
            render: function ( data, type, row, meta ) {
                if (data)
                    return '<input type="checkbox" checked disabled>';
                return '<input type="checkbox" disabled>';
            }
        },
        {name: 'engagement_time'},
        {name: 'frc_demand'},
        {name: 'dispatched_cars'},
        {name: 'dispatched_time'},
        {name: 'travel_time'},
        {name: 'return_traval_time'},
        {name: 'available_time'},
        {
            name: 'failed',
            render: function ( data, type, row, meta ) {
                if (data)
                    return '<span class="dot red"></span>';
                return '<span class="dot green"></span>';
            }
        },
    ]
);
