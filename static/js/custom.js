var expanded = false;

function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

$('#candidate_login_btn').click(function (e) { 
    e.preventDefault();
    $('#signup_div').hide();
    $('#login_div').show();
});

$('#candidate_signup_btn').click(function (e) { 
    e.preventDefault();
    $('#login_div').hide();
    $('#signup_div').show();
    
});