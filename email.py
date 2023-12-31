class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'

command = input()
emails_list = []

while command != "Stop":
    sender, receiver, content = command.split()
    email_info = Email(sender, receiver, content)
    emails_list.append(email_info)

    command = input()

indexes = list(map(int, input().split(', ')))

for index in indexes:
    emails_list[index].send()

for current_email in emails_list:
    print(current_email.get_info())
