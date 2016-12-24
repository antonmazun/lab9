$(document).ready(function(){
        $(".deletePhone").click(function(){
            btn = $(this);
            inp = $("#delete-post");
            inp.attr("value", btn.attr("value"));
        });
});


$(document).ready(function(){
        $("#delete-post").click(function(){
            btn = $(this);
            //alert(btn.attr("value"));
            $.ajax({type: "delete", url: $(location).attr('pathname') + '?phone=' + btn.attr("value"), success: function(result){
                alert(result);
               
                if (result.status === 'error'){
                    alert('error');}
                else
                    {$("#phone_" + btn.attr("value")).remove();}
            }});
        });
    });

$(document).ready(function(){
    $(".search").click(function(){
        btn = $(this);
        inp = $("#search");
        $.ajax({
            type: "GET",
            url : "/search/",
            data: {search: inp.val(), xhr: true},
            success: function(result){

              // result = jQuery.parseJSON(result);
             alert(result);
            $(".phone_container").remove();
//                if(result.length == 0){
//                    $("#phones_container").append('<div class = "phone_container"><h1>Not Found!</h1></div>');
//                }
//                else
            for(i in result){
                $("#phones_container").append('<div id = "phone_' + result[i].id + '"><p><a href  = "/phones_view/get/'+result[i].id+'">'+result[i].name+'</a></p><img src = "' + result[i].url + '" alt = ""  id = "content_image"><h3>Виробник: ' + result[i].manufacturer + ' </h3><p>Ціна $: ' + result[i].price + '</p><p>Рейтинг:' + result[i].rate + '</p><button class="btn  deletePhone" value="'+result[i].id+'" data-toggle="modal" data-target="#deleteModal">Видалити</button></div>');
            };
        }});
    });
});