document.getElementById('encodeButton').addEventListener('click', () => {
    const message = document.getElementById('messageInput').value;

    if (!message) {
        alert('Please enter a binary message.');
        return;
    }

    fetch('/encode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => {
        if (response.ok) {
            alert('Message encoded and playing.');
        } else {
            alert('Error encoding the message.');
        }
    });
});

document.getElementById('recordButton').addEventListener('click', () => {
    fetch('/decode', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('decodedMessage').innerText = 'Decoded message: ' + data.message;
    })
    .catch(error => {
        alert('Error decoding the message.');
    });
});
