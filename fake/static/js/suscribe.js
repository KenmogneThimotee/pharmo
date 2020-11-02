$(document).ready(function(){

    $('#subscribe').click(function(e){

        e.preventDefault()

        var username = $("#username").text()

        $.ajax({
            type: "GET",
            url: "/api/sabonne/",
            headers:{"Authorization":"Token b189ce0582ce06018db2d6075746b75bf0ef7e5e"},
            data: {"username":username},
            success: function (response) {
                
                var count = $('#subscriber_count').text()
                $('#subscriber_count').text(parseInt(count)+1)
            }
        });
    })

})