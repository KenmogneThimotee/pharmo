$(document).ready(function(){
    var current_pos = 0 
    var max = $('#playlist_list').length()
    //Prendre la premiere video et la metre dans la src du frame

    //Quand l'utilisateur clique sur next:
    /**
     * Prendre l'element suivant si on n'est pas a la fin de la liste
     * et la metre dans la src du frame
     * */
    $('#next').click(function(){
        var element = $('#playlist_list').get(current_pos + 1)

        
    })

    //Quand l'utilisateur clique sur previous

    /**
     * Prendre l'element precedent si on est pas au debut de la liste
     * et la metre dans la src du frame
     */
})