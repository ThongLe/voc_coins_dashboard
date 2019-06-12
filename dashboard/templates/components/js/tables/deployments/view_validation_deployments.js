{% load staticfiles i18n %}

tables.validationDeploymentsTable = createTable(
    '#validation_deployments-table',
    '{% url 'gv:api:deployments:deployment:validations' deployment_id=deployment.id %}',
    [
        {name: 'id'},
        {name: 'deployment_context.name'},
        {name: 'deployment_context.date'},
        {name: 'plan_risk'},
        {name: 'actual_risk'},
        {
            name: 'status_color',
             render: function ( data, type, row, meta ) {
                return `<span class="dot ${data}"></span>`;
            }
        },
        {
            name: 'url',
            render: function renderColumn( data, type, row, meta ) {
                return `<a href="${data}"><i class="fas fa-info-circle fa-fw"></i></a>`;
            }
        },
    ]
);