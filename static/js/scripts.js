document.addEventListener('DOMContentLoaded', () => {
    const chatbotForm = document.querySelector('#chatbot-form');
    const chatbotInput = document.querySelector('#chatbot-input');
    const chatbotMessages = document.querySelector('#chatbot-messages');

    chatbotForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const userMessage = chatbotInput.value.trim();
        if (!userMessage) return; // Prevent sending empty messages
        
        // Display the user message
        chatbotMessages.innerHTML += `<div class="message user">${userMessage}</div>`;

        // Send message to the server
        fetch('/chatbot', { // Make sure this endpoint matches your Flask route
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Display the bot response
            chatbotMessages.innerHTML += `<div class="message bot">${data.response}</div>`;
            chatbotMessages.scrollTop = chatbotMessages.scrollHeight; // Scroll to the bottom
        })
        .catch(error => {
            console.error('Error:', error);
            chatbotMessages.innerHTML += `<div class="message bot">Sorry, there was an error. Please try again later.</div>`;
        });

        // Clear the input field
        chatbotInput.value = '';
    });
});
