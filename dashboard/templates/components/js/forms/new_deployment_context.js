{% load staticfiles i18n %}

function success(result){
    window.location.href = result.data.url;
}


function submitDeploymentContext() {
    var data = {
        name: $('#id_name').val(),
        cluster: $('#id_cluster').val(),
        frc_supply: parseInt($('#id_frc_supply').val()),
        date: $('#processedDate').datepicker('getFormattedDate'),
        from_hour: parseInt($('#id_from_hour').val()),
        to_hour: parseInt($('#id_to_hour').val()),
        training_size: parseInt($('#id_training_size').val()),
        testing_size: parseInt($('#id_testing_size').val()),
        allocation_constraints: []
    };

    if (sectors.length > 0) {
        for (var i = 0; i < sectors.length; i++) {
            data.allocation_constraints.push({
                sector: sectors[i],
                frc_supply: parseInt($(`#id_frc_supply_${sectors[i]}`).val()),
                from_hour: parseInt($(`#id_from_hour_${sectors[i]}`).val()),
                to_hour: parseInt($(`#id_to_hour_${sectors[i]}`).val())
            });
        }
    }

    data.allocation_constraints = JSON.stringify(data.allocation_constraints);

    request({
        url : '{% url "gv:api:deployment_contexts:index" %}',
        method: 'POST',
        data,
        success
    })
}