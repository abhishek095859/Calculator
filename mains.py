import os

#print(os.getcwd())
#print(os.listdir())

def write_file(filename, text):
    try: 
        with open(filename, 'w') as file:
            file.write(text)
        print(filename)
    except Exception as a:
        print("An error occurred")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        print(text)
    except FileNotFoundError as err:
        print(err)

while True:
    command=input("## ")

    if command.startswith("touch "):
        try:
            parts=command.split('"')
            filename=parts[1]
            text=parts[3]
            write_file(filename,text)
            read_file(filename)
        except Exception as a:
            print("wrong syntax")

    elif command.startswith("cd "):
        try:
            os.chdir(command.split(" ",1)[1])
            print(os.getcwd())
        except Exception as a:
            print("Error occurs")

    elif command == "ls ":
        files = [j for j in os.listdir() if os.path.isfile(j)]
        print(' '.join(j + "/ " for j in files))

    elif command == "pwd":
        print(os.getcwd())
    else:
        print("Unknown command")
