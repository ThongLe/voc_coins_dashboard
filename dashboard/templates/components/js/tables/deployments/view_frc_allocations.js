{% load staticfiles i18n %}

tables.frcAllocationsTable = createTable(
    '#frc-allocations-table',
    '{% url 'gv:api:deployments:deployment:frc_allocations' deployment_id=deployment.id %}',
    [
        {name: 'car'},
        {% for hour in deployment_context.hour_range %}
            {name: 'hour_{{ hour }}', render},
        {% endfor %}
        {
            name: 'utilization',
            render: function renderColumn( data, type, row, meta ) {
                var rate = Math.round(data * 10000) / 100;
                return `${rate} %`;
            }
        },
    ]
);
