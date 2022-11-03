function editBank() {
    $.ajax({
        type: 'POST',
        url: '/profile_user/edit_profile',
        data: $('#edit-bank-form').serialize(),
        
        success: function(response) {
            alert("Profile Successfully Updated!");
        },
        error: function(xhr, status, error) {
            var err = JSON.parse(xhr.responseText);
            alert(err.Message);
        }
    })
}


function editReg() {
    $.ajax({
        type: 'POST',
        url: '/profile_user/edit_profile',
        data: $('#edit-reg-form').serialize(),
        
        success: function(response) {
            alert("Profile Successfully Updated!");
        },
        error: function(xhr, status, error) {
            var err = JSON.parse(xhr.responseText);
            alert(err.Message);
        }
    })
}