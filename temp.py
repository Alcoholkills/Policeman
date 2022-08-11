sl = [
"Bold: \\u001b[1m",
"Underline: \\u001b[4m",
"Reversed: \\u001b[7m",
]

for item in sl:
    text = item.split(":")[0].upper().replace(" ", "_")
    hextext = item.split(":")[1]
    print(f"{text} = \"{hextext}\"")
