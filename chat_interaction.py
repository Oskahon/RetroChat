# Contains the methods needed to interact with the chat

def write_to_chat(user, message):
    chat_message = f'{user}: {message}'

    with open('./logs/chat.txt', 'a') as file:
        file.write('\n' + chat_message)


def get_chat():
    with open('./logs/chat.txt', 'r') as file:
        chat_log = file.read()

    return chat_log
