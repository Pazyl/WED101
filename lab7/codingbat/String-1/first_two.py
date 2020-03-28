def first_two(str):
    length = len(str)
    if len(str) > 2:
        length = 2
    return str[:length]


print(first_two('Hello'))


def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str