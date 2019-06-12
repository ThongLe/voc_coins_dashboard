{% load staticfiles i18n %}

tables.uploadedFilesTable = createTable(
    '#uploaded_files-table',
    '{% url 'gv:api:uploaded_files:index' %}',
    [
        {name: 'name'},
        {name: 'incident_count'},
        {name: 'uploaded_at'},
        {
            name: 'url',
            render: function ( data, type, row, meta ) {
                return `<a href="${data}"><i class="fas fa-info-circle fa-fw"></i></a>`;
            }
        }
    ]
);
