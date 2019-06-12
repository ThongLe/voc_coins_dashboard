{% load staticfiles i18n %}

tables.inactiveTable = createTable(
    '#inactive-table',
    '{% url 'gv:api:uploaded_files:inactive' %}',
    [
        {name: 'name'},
        {name: 'incident_count'},
        {name: 'uploaded_at'},
        {
            name: 'url',
            render: function ( data, type, row, meta ) {
                return `<a href="${data}"><i class="fas fa-info-circle fa-fw"></i></a>`;
            }
        },
        {
            name: 'activate_url',
            render: function ( data, type, row, meta ) {
                var activateURL = data;
                var redirectURL = "{% url 'gv:web:incidents:predict' %}";
                return `<a onclick="switchStatus('${activateURL}', '${redirectURL}')"><i class="fas fa-arrow-circle-right"></i></a>`;
            }
        },
    ]
);