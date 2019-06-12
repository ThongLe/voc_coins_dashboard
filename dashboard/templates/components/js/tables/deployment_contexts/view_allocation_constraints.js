{% load staticfiles i18n %}


tables.preallocationTable = createTable(
    '#preallocations-table',
    '{% url "gv:api:deployment_contexts:deployment_context:allocation_constraints" deployment_context_id=deployment_context.id %}',
    [
        { name: 'sector' },
        { name: 'frc_supply'},
        { name: 'from_hour' },
        { name: 'to_hour' },
    ]
);


