$(document).on('submit','#post-form',function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:"{% url 'buat_sumbangan:add_donasi' %}",
        data:{
            berat:$('#berat').val(),
            jenis :$("input[name='jenis-sampah']:checked").val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
        complete:function(json){
            alert("Donasi Diterima");
            document.getElementById("post-form").reset();
        }
    });
});

