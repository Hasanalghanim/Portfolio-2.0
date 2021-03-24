document.addEventListener('DOMContentLoaded', function() {
var elems = document.querySelectorAll('.scrollspy');
var instances = M.ScrollSpy.init(elems,);
});


$(document).on('submit','#contact_form', function(e){
  e.preventDefault();

  $.ajax({
    type:'POST',
    url:'/sendemail/',
    data:{
      senderName:$('#senderName').val(),
      email:$('#email').val(),
      fromMessage:$('#fromMessage').val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },

    success: function () {
                   $("#emailsent").show();
                   setTimeout(function() { $("#emailsent").hide(); }, 20000);
            }

    })




  }
)
