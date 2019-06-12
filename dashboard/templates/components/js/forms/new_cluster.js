{% load staticfiles i18n %}

function successHandler(result){
    window.location.href = result.data.url;
}

function collectClusterData(){
    return {
        name: $('#clusterName').val(),
        sectors: sectors.join(','),
        frc_supply: $('#frcSupply').val()
    };
}

function submitCluster(){
    var url = '{% url "gv:api:clusters:index" %}';
    var data = collectClusterData();
    request({url, method: 'POST', data, success: successHandler})
}

{% include "web/components/js/tables/clusters/new_sectors.js" %}