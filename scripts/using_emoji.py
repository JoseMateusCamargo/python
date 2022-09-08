# Method #1: Using Unicode's
kissing = "\U0001F618"
mask = "\U0001F637"
happy = "\U0001F600"

print(f"...Kissing: {kissing}\n"
      f"...Mask: {mask}\n"
      f"...Happy: {happy}")

# Method #2: Using CLDR short name
print("\N{grinning face}")
print("\N{slightly smiling face}")
print("\N{winking face}")
