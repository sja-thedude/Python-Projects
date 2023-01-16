def madlib():
    body_part = input("Enter a body part: ")
    verb = input("Enter a verb: ")
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    adj3 = input("Enter another adjective: ")
    adj4 = input("Enter another adjective: ")
    adj5 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun_plural_1 = input("Enter a plural noun: ")
    noun_plural_2 = input("Enter another plural noun: ")

    madlib = f"I love computer programming because its {adj1}! The journey to becoming a \
good programmer starts with hope in your mind and a dream in your {body_part}. Through blood, \
sweat, and {noun_plural_1}, hopefully it never ends. Yes, once you learn to {verb}, it becomes \
a part of your life identity and you can become a super {adj2} hacker. Knowledge of programming \
lets you take control of your {noun1}. You can create your own personal {noun_plural_2}, anything \
from developing {adj3} software to analyzing data and making predictions about the {noun2}. You can \
maybe even recreate Jarvis and make him extra {adj4}. I hope you'll start your {adj5} journey by \
coding with SJA :)"

    print(madlib)
