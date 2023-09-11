css = '''
<style>
/* Updated Creative Chat Message Styles */
.chat-message {
    padding: 1.5rem;
    border-radius: 0.8rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center; /* Center items vertically */
}

.chat-message.user {
    background-color: #ff5733; /* Bright orange background for user messages */
    color: white; /* Text color */
}

.chat-message.bot {
    background-color: #3498db; /* Blue background for bot messages */
    color: white; /* Text color */
}

.chat-message .avatar {
    width: 15%; /* Adjust avatar width */
    margin-right: 1rem; /* Add spacing between avatar and message */
}

.chat-message .avatar img {
    max-width: 100%;
    max-height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 85%; /* Adjust message width */
    padding: 1rem; /* Increase message padding */
    border-radius: 0.5rem; /* Add border-radius to message container */
    background-color: rgba(0, 0, 0, 0.1); /* Semi-transparent background */
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Add a subtle box shadow */
}

/* Add hover effect for messages */
.chat-message.user:hover,
.chat-message.bot:hover {
    transform: scale(1.05); /* Enlarge the message on hover */
    transition: transform 0.3s ease;
}

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJ3fRyYN7bASivSLlVoGGQuUrBlkdfhPL_zA&usqp=CAU" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
<img src="https://w7.pngwing.com/pngs/178/595/png-transparent-user-profile-computer-icons-login-user-avatars-thumbnail.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
