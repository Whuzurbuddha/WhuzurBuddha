$(document).ready(function() {
    $("#signupbtn").click(function() {
        var username = $("#username").val();
        var passwd = $("#passwd").val();
        var passwdr = $("#passwdr").val();
        if (passwd != passwdr) {
            alert("Your passwords do not match.");
        } else {
            sendData(username, passwd);
            alert("You were successfully registrated!")
        }
    });
});

function sendData(username, passwd) {
    $.post("http://localhost:3000/addUser", { username: username, passwd: passwd }, function(data) {
        alert(data);
    });
}
