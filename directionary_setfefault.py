
import pprint

message = 'You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.'
count = {}

for character in message:
    count.setdefault (character, 0)
    count[character] = count[character] + 1

message_formatted = pprint.pformat(count)
print (message_formatted)
pprint.pprint(count)