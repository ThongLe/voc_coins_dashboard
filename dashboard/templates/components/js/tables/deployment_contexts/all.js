{% load staticfiles i18n %}

tables.deploymentContextsTable = createTable(
    '#deployment_contexts-table',
    '{% url 'gv:api:deployment_contexts:index' %}',
    [
        {name: 'name'},
        {name: 'cluster'},
        {name: 'date'},
        {
            name: 'url',
            render: function renderColumn( data, type, row, meta ) {
                return `<a href="${data}"><i class="fas fa-info-circle fa-fw"></i></a>`;
            }
        }
    ]
);