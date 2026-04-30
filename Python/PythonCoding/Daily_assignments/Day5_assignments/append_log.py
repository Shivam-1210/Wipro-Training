
text = "This is a new log entry."


with open("log.txt", "a") as file:
    file.write(text + "\n")


with open("log.txt", "r") as file:
    contents = file.read()

print("Contents of log.txt:")
print(contents)