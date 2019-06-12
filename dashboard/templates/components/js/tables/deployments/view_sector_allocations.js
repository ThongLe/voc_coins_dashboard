{% load staticfiles i18n %}

var hoverHour;
function highlightColumn(domOjbect, table) {
    domOjbect.on( 'mouseenter', 'td', function () {
        var sector = table.cell(this).row().data().sector;
        var colIdx = table.cell(this).index().column;

        $( table.cells().nodes() ).removeClass( 'highlight' );
        $( table.column( colIdx ).nodes() ).addClass( 'highlight' );

        var manager = maps.map;

        var newHoverHour = ((colIdx - 1) * 2);
        if (newHoverHour in manager.hourLayers) {
            for (var i = 0; i < 24; i += 2)
                if (i in manager.hourLayers)
                    manager.map.removeLayer( manager.hourLayers[i]);
            hoverHour = newHoverHour;
            manager.hourLayers[hoverHour].addTo(manager.map);
        }
    } );
}

function render( data, type, row, meta ) {
    if (data == 0) return '';
    return data;
}

tables.sectorAllocationsTable = createTable(
    '#sector-allocations-table',
    '{% url 'gv:api:deployments:deployment:sector_allocations' deployment_id=deployment.id %}',
    [
        {name: 'sector'},
        {% for hour in deployment_context.hour_range %}
            {name: 'hour_{{ hour }}', render},
        {% endfor %}
        {name: 'risk'},
    ]
);

highlightColumn($('#sector-allocations-table tbody'), tables.sectorAllocationsTable);