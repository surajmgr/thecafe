from fbchat import Client
from fbchat.models import Message


username = "thec.client.3"
password = "hungryCafe@1#"

client = Client(username, password)
# users = client.fetchThreadList()
users = client.fetchAllUsers()

for user in users:
    client.send(Message(text=f"Congratulations {user.name}, you are my best friend with 999 messages!"),
                thread_id=user.uid)

client.logout()


# print(users)

# detailed_users = [list(client.fetchThreadInfo(
#     user.uid).values())[0] for user in users]

# sorted_detailed_users = sorted(
#     detailed_users, key=lambda u: u.message_count, reverse=True)

# best_friend = sorted_detailed_users[:1]
# print("Best friend:", best_friend.name,
#       "with a message count of", best_friend.message_count)

# client.send(Message(text=f"Congratulations {best_friend.name}, you are my best friend with {best_friend.message_count} messages!"),
#             thread_id=best_friend.uid)
