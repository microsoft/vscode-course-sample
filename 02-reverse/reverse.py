words = ['magnificent', 'world', 'hello', 'python']

words.sort(reverse=True)

words = [ w[::-1] for w in words ]

print(words)
