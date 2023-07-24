$(document).ready(function() {
    
    $("#signupbtn").click(function() {
        var username = $("#username").val();
        var passwd = $("#passwd").val();

        const data = {
            username: username,
            passwd: passwd
        };

        fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                loadMenu();
                return response.text();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => console.log(data)) 
        .catch(error => console.error('Error:', error));
    });
});
