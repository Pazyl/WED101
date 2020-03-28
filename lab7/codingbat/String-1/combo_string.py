def combo_string(a, b):
    new_str = a + b + a
    if len(a)> len(b):
        new_str = b + a + b
    return new_str


print(combo_string('Hello', 'hi'))