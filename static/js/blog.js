$ (document).ready(function(){

        var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

//        $("#unPubBtn").click(function(){
//
////            var serializedData = $("#changePostStatusForm").serialize();
//
//            var dataId = $(this).data('id');
//
//            $.ajax({
//                url: '/post/' + dataId + '/updated/',
//                data:{
//                    csrfmiddlewaretoken: csrfToken,
//                    id: dataId
//                },
//                type: 'post',
//                success: function(){
//                    console.log('success')
//                }
//            })
//
//        });



       $("#unPubBtn").click(function(){

            var dataId = $(this).data('id');

            $.ajax({
                url: '/post/' + dataId + '/unpublished/',
                data:{
                    csrfmiddlewaretoken: csrfToken,
                    id: dataId
                },
                type: 'post',
                success: function(){
                $("#dropdown").append('<button id="pubBtn" type="button" class="dropdown-item" data-id="{{post.id}}" href="#">Publish</button>')

                }
            });

       });


       $("#pubBtn").click(function(){

            var dataId = $(this).data('id');

            $.ajax({
                url: '/post/' + dataId + '/published/',
                data:{
                    csrfmiddlewaretoken: csrfToken,
                    id: dataId
                },
                type: 'post',
                success: function(){
                $("#dropdown").append('<button id="pubBtn" type="button" class="dropdown-item" data-id="{{post.id}}" href="#">Publish</button>')

                }
            });

       });

});