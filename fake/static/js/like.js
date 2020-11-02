$(document).ready(function(){

    $('#like_button').click(function(e){
        e.preventDefault()
        console.log($('like').val())

        var idvideo = $('#idvideo').val()

        $.ajax({
            type: "GET",
            url: "/api/likeVideo/",
            headers:{"Authorization":"Token b189ce0582ce06018db2d6075746b75bf0ef7e5e"},
            data: {"idvideo": idvideo},
            success: function (response) {
                
                var numberLike = parseInt($('like').text())
                numberLike += '1'

                console.log(numberLike)
                $('like').text(numberLike)
            }
        });
    })
})