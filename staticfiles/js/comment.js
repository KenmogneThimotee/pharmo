$(document).ready(function(){


    $("#comment").click(function(e){
        e.preventDefault()

        var data = $("#formComment").serialize()
        console.log(data)

        $.ajax({
            type: "POST",
            url: "/api/comment/",
            headers:{"Authorization":"Token b189ce0582ce06018db2d6075746b75bf0ef7e5e"},
            data: data,
            success: function (response) {
                
                var li = $("#listComment").clone()
                var username = $("#username").text()

                $.ajax({
                    type:"GET",
                    url: "/api/userDetail/",
                    headers:{"Authorization":"Token b189ce0582ce06018db2d6075746b75bf0ef7e5e"},
                    data: {"username":username},
                    success: function (resp) {
                        console.log("Test lililili ")
                        console.log(li.find("#img"))
                        li.find("#image").attr('src',resp.profilePicture)
                        li.find('#timesince').text("0 minute ago")
                        li.find('#contenue').text($('#contenue').val())
                        $('#contenue').val("")

                        $('#commentlist').before(li)
                        li.attr('hidden', false)
                        li.show()
                        console.log(li)
                    }
                });
            }
        });
    })
})