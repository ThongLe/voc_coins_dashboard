{% load staticfiles i18n %}

tables.activeTable = createTable(
    '#active-table',
    '{% url 'gv:api:uploaded_files:active' %}',
    [
        {
            name: 'deactivate_url',
            render: function ( data, type, row, meta ) {
                var deactivateURL = data;
                var redirectURL = "{% url 'gv:web:incidents:predict' %}";
                return `<a onclick="switchStatus('${deactivateURL}', '${redirectURL}')"><i class="fas fa-arrow-circle-left"></i></a>`;
            }
        },
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
            name: 'migrated',
            render: function ( data, type, row, meta ) {
                if (data)
                    return `<a href="${data}"><i class="fas fa-check-circle"></i></a>`;
                return `<a href="${data}"><i class="fas fa-circle"></i></a>`;
            }
        }
    ]
);


