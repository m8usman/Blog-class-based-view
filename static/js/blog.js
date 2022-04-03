$ (document).ready(function(){
        var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
        var $loader = '<i class="fa fa-spinner fa-spin"></i>'

// Change status of post (publish/un-publish)
       $(".statusBtn").click(function(){
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

// add new category
    var formData = new FormData();

      $(document).on('click', '#createCategoryBtn', function(e) {
        var $clickedBtnCategory = $(this);
        if($('#id_category_name').val() == ''){
                alert('Category Name is Required')

        }else{


        formData.append('name', $('#id_category_name').val())
        formData.append('description', $('#id_category_description').val())
        formData.append('action', 'create-category')
        formData.append('csrfmiddlewaretoken', csrfToken )
        $clickedBtnCategory.html($loader).attr('disabled', 'disabled');

          $.ajax({
              type: 'POST',
              url: $("#createCategoryForm").data('url'),
              data: formData,
              cache: false,
              processData: false,
              contentType: false,
              success: function (response){
                  $("#div_id_categories").append('<div class="form-check"><input type="checkbox" class="form-check-input" name="categories" checked value="' +response.categoryId+ '"><label class="form-check-label" for="id_categories_0">'+ $('#id_category_name').val() +'</label></div>')
                  $('#categoryModal .close').click()
              },
              complete: function(){
                $clickedBtnCategory.html('Add Category')
                $clickedBtnCategory.removeAttr('disabled');
                $("#createCategoryForm")[0].reset();
                },
              error: function(xhr, errmsg, err) {
                  console.log(xhr.status + ":" + xhr.responseText)
              }
          })

          }
      })

// add new tag
    var formData = new FormData();

      $(document).on('click', '#createTagBtn', function(e) {
        var $clickedBtnTag = $(this);
        if($('#id_tag_name').val() == ''){
                alert('Tag Name is Required')

        }else{


        formData.append('name', $('#id_tag_name').val())
        formData.append('description', $('#id_tag_description').val())
        formData.append('action', 'create-tag')
        formData.append('csrfmiddlewaretoken', csrfToken )
        $clickedBtnTag.html($loader).attr('disabled', 'disabled');

          $.ajax({
              type: 'POST',
              url: $("#createTagForm").data('url'),
              data: formData,
              cache: false,
              processData: false,
              contentType: false,
              success: function (response){
                  $("#div_id_tags").append('<div class="form-check"><input type="checkbox" class="form-check-input" name="tags" checked value="' +response.tagId+ '"><label class="form-check-label" for="id_tags_0">'+ $('#id_tag_name').val() +'</label></div>')
                  $('#tagModal .close').click()
              },
              complete: function(){
                $clickedBtnTag.html('Add Tag')
                $clickedBtnTag.removeAttr('disabled');
                $("#createTagForm")[0].reset();
                },
              error: function(xhr, errmsg, err) {
                  console.log(xhr.status + ":" + xhr.responseText)
              }
          })

          }
      })


});