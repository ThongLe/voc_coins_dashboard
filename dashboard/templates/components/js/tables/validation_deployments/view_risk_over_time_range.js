{% load staticfiles i18n %}

tables.planRiskOverTimeRange = createTable(
    '#plan_risk_over_time_range-table',
    '{% url 'gv:api:validation_deployments:validation_deployment:plan_risk_allocations' validation_deployment_id=validation_deployment.id %}',
    [
        {name: 'sector'},
        {% for hour in deployment_context.hour_range %}
            {name: 'hour_{{ hour }}', render},
        {% endfor %}
        {name: 'risk'},
    ]
);

tables.actualRiskOverTimeRange = createTable(
    '#actual_risk_over_time_range-table',
    '{% url 'gv:api:validation_deployments:validation_deployment:actual_risk_allocations' validation_deployment_id=validation_deployment.id %}',
    [
        {name: 'sector'},
        {% for hour in deployment_context.hour_range %}
            {name: 'hour_{{ hour }}', render},
        {% endfor %}
        {name: 'risk'},
    ]
);
