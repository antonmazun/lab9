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

               result = jQuery.parseJSON(result);
             alert(result);
            $(".phone_container").remove();
                if(result.length == 0){
                    $("#phones_container").append('<div class = "phone_container"><h1>Not Found!</h1></div>');
                }
                else
            for(i in result){
                $("#phones_container").append('<div class = " phone_container" id = "phone_' + result[i].id + '"><div class = "thumbnail"><img src = "' + result[i].url + '" alt = ""  class = "img-responsive" id = "content_image"><div class = "caption"><h3>Виробник: ' + result[i].name + ' </h3><p>Ціна $: ' + result[i].price + '</p><p>Рейтинг:' + result[i].rate + '</p></div></div></div>');
                
                
                    
{%endif%}


 
           <button class="btn  deletePhone" value="{{i.id}}" data-toggle="modal" data-target="#deleteModal">Видалити</button>
            </div>
            };
        }});
    });
});