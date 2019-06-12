{% load staticfiles i18n %}


function buildSeclector(_type, from, to, defaultOption){
    return function ( data, type, row, meta ) {
        var selectBox = `<select class="form-control" id="id_${_type}_hour_${data}">`;
        for (var i = from; i <= to; i+= 2)
            selectBox += `<option ${ (i == defaultOption) ? 'selected' : '' } value="${i}">${i}</option>`;
        selectBox +=  '</select>';
        return selectBox;
    }
}


function buildFromHourSelector(_type){
    return buildSeclector('from', 0, 22, 0);
}

function buildToHourSelector(_type){
    return buildSeclector('to', 2, 24, 24);
}

tables.preallocationTable = createTable(
    '#preallocations-table',
    [],
    [
        { name: 'sector' },
        {
            name: 'frc_supply',
            render: function ( data, type, row, meta ) {
                return `<input type="number" class="form-control" id="id_frc_supply_${data}" value="1">`;
            }
        },
        {
            name: 'from_hour',
            render: buildFromHourSelector()
        },
        {
            name: 'to_hour',
            render: buildToHourSelector()
        },
        {
            name: 'delete',
            render: function ( data, type, row, meta ) {
                return `<a onclick="removeSector('${data}')"><i class="fas fa-times-circle"></i></a>`;
            }
        },
    ]
);


