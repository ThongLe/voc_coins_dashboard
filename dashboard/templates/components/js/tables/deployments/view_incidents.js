{% load staticfiles i18n %}

tables.incidentsTable = createTable(
    '#incidents-table',
    '{% url 'gv:api:deployments:deployment:incidents' deployment_id=deployment.id %}',
    [
        {name: 'id'},
        {name: 'sector_name'},
        {name: 'frc_demand'},
        {name: 'start_time'},
        {name: 'engagement_time'},
        {
            name: 'is_urgent',
            render: function ( data, type, row, meta ) {
                if (data == 'U')
                    return '<input type="checkbox" checked disabled>';
                return '<input type="checkbox" disabled>';
            }
        },
        {name: 'date'},
        //{name: 'generated_incident_set_id'},
        //{name: 'generated_incident_set_id'},
    ]
);
