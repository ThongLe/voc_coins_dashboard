{% load staticfiles i18n %}

tables.tasksTable = createTable(
    '#tasks-table',
    '{% url 'gv:api:tasks:index' %}',
    [
        {name: 'id'},
        {name: 'capitalized_task_type'},
        {name: 'generating_time'},
        {name: 'optimizing_time'},
        {name: 'scheduling_time'},
        {name: 'evaluating_time'},
        {
            name: 'status_color',
            render: function ( data, type, row, meta ) {
                return '<span class="dot ' + data + '"></span>';
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
