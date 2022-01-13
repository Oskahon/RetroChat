import os
import chat_interaction


def main():
    print('Enter username.')
    username = input()

    print('Enter message.')
    message = input()

    if not os.path.isfile('./logs/chat.txt'):
        with open('./logs/chat.txt', 'w') as file:
            file.write('Chat log for the RetroChat!')

    chat_interaction.write_to_chat(username, message)

    chat = chat_interaction.get_chat()
    print(chat)


if __name__ == '__main__':
    main()
