var djdatatableview = (function(){
    function renderColumn( data, type, row, meta ) { return data; }

    function initialize(name, opts) {
        var els = $('#' + name);
        var options = djdatatableview.getOptions(els[0], opts)
        return els.DataTable(options);
    }

    function getOptions(dtview, opts) {
        opts = opts || {}

        var ajaxOptions = {};

        if (dtview.attributes.getNamedItem('source-url')){
            ajaxOptions = {
                ajax: {
                    url: dtview.attributes.getNamedItem('source-url').textContent,
                    contentType: "application/json",
                    headers: { 'X-CSRFToken': jQuery("[name=csrfmiddlewaretoken]").val() },
                    type: "GET"
                }
            }
        }

        var newOpts = Object.assign(
            {},
            ajaxOptions,
            opts
        )

        return newOpts;
    }

    var api = {
        initialize,
        getOptions
    }
    return api;
})()