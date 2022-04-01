$ (document).ready(function(){
        var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
        var $loader = '<i class="fa fa-spinner fa-spin"></i>'

       $(".unPubBtn").click(function(){
            var $clickedBtn = $(this);
            var orignalContent = $clickedBtn.text();
            var postId = $clickedBtn.data('id');
            $clickedBtn.html($loader).attr('disabled', 'disabled');
            $.ajax({
                url: '/post/' + postId + '/update-status/',
                data:{
                    csrfmiddlewaretoken: csrfToken,
                    id: postId
                },
                type: 'post',
                success: function(resp){
                    console.log(resp)
                    if(resp.is_published === true){
                        $clickedBtn.html('Published').removeClass('btn-danger').addClass('btn-success');;
                    }else{
                        $clickedBtn.html('Unpublished').removeClass('btn-success').addClass('btn-danger');
                    }
                },
                complete: function(){

                    $clickedBtn.removeAttr('disabled');
                },
                error: function(error){
                    alert("Internal 500 error.");
                    $clickedBtn.html(orignalContent);
                }
            });
       });
});