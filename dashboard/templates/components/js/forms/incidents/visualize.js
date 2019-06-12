function createTableByData(data){
    return createTable(
        '#incidents-table',
        data,
        [
            {name: 'incident_no'},
            {name: 'type_name'},
            {
                name: 'incident_priority',
                render: function ( data, type, row, meta ) {
                    if (data == 'U')
                        return '<input type="checkbox" checked disabled>';
                    return '<input type="checkbox" disabled>';
                }
            },
            {name: 'dispatchdt'},
            {name: 'correct_arrivaldt'},
        ]
    );
}

function success(result){
//    data -> list
    tables.incidentsTable.destroy();
    tables.incidentsTable = createTableByData(result.data);
}

function updateChart(chart, data){
    // data = { labels, data }
    chart.data.labels = data.labels || [];
    chart.data.datasets[0].data = data.data || [];
    chart.update();
}

function viewHeatmap(urls, objs){
    data= {
        cluster: $('#id_cluster').val(),
        date: $('#processedDate').datepicker('getFormattedDate'),
        from_hour: $('#id_from_hour').val(),
        to_hour: $('#id_to_hour').val()
    };

    loadSectorsBoundaries(objs.manager, urls.heatmap, data);
    loadDataForChart(urls.chart, objs.chart, data);
    request({ url: urls.table, data, success });
}