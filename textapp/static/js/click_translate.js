// script.js
document.addEventListener('DOMContentLoaded', function() { // Ensure DOM is fully loaded
    const textarea = document.getElementById('text-box1');
    const processButton = document.getElementById('process-button');
    const clearButton = document.getElementById('clear-button');
    const processText = document.getElementById('processed-text');

    textarea.addEventListener('input', function() {
        processButton.disabled = textarea.value.trim() === ''; // If text area is blank, button is unclickable. Otherwise, it's clickable.
    });
    
    processButton.addEventListener('click', function() {
        const text = textarea.value.trim();  // Remove additional whitespace
        if (text !== '') {
            fetch('/textapp/processText/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Function to get CSRF token
                },
                body: JSON.stringify({ text: text })
            }) // return a Response object
            .then(response => response.json()) // Return JSON response and a Promise
            .then(data => { // Process the JSON response data
                console.log('Successfully processed data:', data);
                if (data.result) { // When Django Backend get successful Response
                    processText.textContent = data.result;
                } else if (data.message) { // When backend API accept error message
                    processText.textContent = "Error occurs! message as below: " + data.message;
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    });
 
    clearButton.addEventListener('click', function(){
        textarea.value = "";
        processButton.disabled = true;
    })

    // Function to get the CSRF token (from Django docs)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});