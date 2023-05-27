console.log("tip##################");
$(function() {
	function addButton() {
        if ($("#octo-relay-on").length == 0 && $("#control").hasClass("active")) {
            $("#control-jog-custom").append('<div class="jog-panel"><div class="input-append input-block-level"><button id="octo-relay-on" class="btn btn-block" style="text-align: center;">Run Script</button></div></div>');

            // Add an event listener to the first button
            $("#octo-relay-on").click(function() {
                $.ajax({
                    url: API_BASEURL + "plugin/octo_button",
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({ command: "octo_relay_on" }),
                    contentType: "application/json; charset=UTF-8"
                });
            });
        }
    
        if ($("#octo-relay-off").length == 0 && $("#control").hasClass("active")) {
            $("#control-jog-custom").append('<div class="jog-panel"><div class="input-append input-block-level"><button id="octo-relay-off" class="btn btn-block" style="text-align: center;">Run Script</button></div></div>');
    
            // Add an event listener to the second button
            $("#octo-relay-off").click(function() {
                $.ajax({
                    url: API_BASEURL + "plugin/octo_button",
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({ command: "octo_relay_off" }),
                    contentType: "application/json; charset=UTF-8"
                });
            });
        }
    }

    addButton();

    // Add the buttons when the tab changes
    $(document).on("afterTabChange", function() {
        addButton();
    });
});