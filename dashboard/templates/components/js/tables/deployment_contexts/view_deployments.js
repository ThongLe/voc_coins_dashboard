{% load staticfiles i18n %}

tables.deploymentsTable = createTable(
    '#deployments-table',
    '{% url 'gv:api:deployment_contexts:deployment_context:deployments' deployment_context_id=deployment_context.id %}',
    [
        {name: 'id'},
        {name: 'capitalized_stage'},
        {
            name: 'risk',
            render: function ( data, type, row, meta ) {
                return `${Math.round(data * 10000) / 100} %`;
            }
        },
        {
            name: 'utilization',
            render: function ( data, type, row, meta ) {
                return `${Math.round(data * 10000) / 100} %`;
            }
        },
        {
            name: 'status_color',
            render: function ( data, type, row, meta ) {
                return `<span class="dot ${data}"></span>`;
            }
        },
        {
            name: 'url',
            render: function ( data, type, row, meta ) {
                return `<a href="${data}"><i class="fas fa-info-circle fa-fw"></i></a>`;
            }
        },
    ],
    'GET',
    {
        deployment_context_id: {{deployment_context.id}}
    }
);
