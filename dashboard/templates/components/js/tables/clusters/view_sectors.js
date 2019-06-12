{% load staticfiles i18n %}

tables.sectorsTable = createTable(
    '#sectors-table',
    '{% url 'gv:api:clusters:cluster:sectors' cluster_id=cluster.id %}',
    [
        {name: 'name'},
    ]
);

