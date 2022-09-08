def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)


print(split_and_join('one two three'))
# output: one-two-three
