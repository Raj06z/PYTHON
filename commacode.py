def list_to_string(items):
    if not items:
        return "The list is empty."
    elif len(items) == 1:
        return items[0]
    else:
        return ", ".join(items[:-1]) + f", and {items[-1]}"

# Test cases
spam = ['apples', 'bananas', 'tofu', 'cats']
empty_list = []
single_item = ['hello']

print(list_to_string(spam))         # Output: 'apples, bananas, tofu, and cats'
print(list_to_string(empty_list))   # Output: 'The list is empty.'
print(list_to_string(single_item))  # Output: 'hello'