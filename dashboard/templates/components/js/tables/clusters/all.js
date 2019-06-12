{% load staticfiles i18n %}

tables.clusterTable = createTable(
    '#clusters-table',
    '{% url 'gv:api:clusters:index' %}',
    [
        {name: 'name'},
        {name: 'sector_count'},
        {name: 'frc_supply'},
        {
            name: 'url',
            render: function ( data, type, row, meta ) {
                return `<a href="${data}"><i class="fas fa-info-circle fa-fw"></i></a>`;
            }
        },
    ]
);