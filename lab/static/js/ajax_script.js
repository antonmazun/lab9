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
