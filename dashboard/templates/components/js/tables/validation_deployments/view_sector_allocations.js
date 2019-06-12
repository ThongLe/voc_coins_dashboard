{% load staticfiles i18n %}

tables.planFrcAllocations = createTable(
    '#plan_sector_allocations-table',
    '{% url 'gv:api:validation_deployments:validation_deployment:plan_sector_allocations' validation_deployment_id=validation_deployment.id %}',
    [
        {name: 'sector'},
        {% for hour in deployment_context.hour_range %}
            {name: 'hour_{{ hour }}', render},
        {% endfor %}
    ]
);

tables.actualFrcAllocations = createTable(
    '#actual_sector_allocations-table',
    '{% url 'gv:api:validation_deployments:validation_deployment:actual_sector_allocations' validation_deployment_id=validation_deployment.id %}',
    [
        {name: 'sector'},
        {% for hour in deployment_context.hour_range %}
            {name: 'hour_{{ hour }}', render},
        {% endfor %}
    ]
);
