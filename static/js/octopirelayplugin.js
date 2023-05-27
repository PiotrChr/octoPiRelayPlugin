$(function() {
	function addButton() {
        if ($("#octo-relay-on").length == 0) {
            $("#control").append('<div style="margin-top:40px"><div class="input-append input-block-level"><button id="octo-relay-on" class="btn btn-block btn-success" style="text-align: center;">Turn printer on</button></div></div>');

            $("#octo-relay-on").click(function() {
                $.ajax({
                    url: OctoPrint.options.baseurl + "plugin/octopirelayplugin/relay",
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({ command: "octo_relay_on" }),
                    contentType: "application/json; charset=UTF-8"
                });
            });
        }
    
        if ($("#octo-relay-off").length == 0) {
            $("#control").append('<div class=""><div class="input-append input-block-level"><button id="octo-relay-off" class="btn btn-block btn-danger" style="text-align: center;">Turn printer off</button></div></div>');
    
            $("#octo-relay-off").click(function() {
                $.ajax({
                    url: OctoPrint.options.baseurl + "plugin/octopirelayplugin/relay",
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({ command: "octo_relay_off" }),
                    contentType: "application/json; charset=UTF-8"
                });
            });
        }
    }

    addButton();
});