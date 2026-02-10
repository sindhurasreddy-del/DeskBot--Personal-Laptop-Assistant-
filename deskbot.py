from task_manager import handle_command

def main():
    print("DeskBot – Personal Laptop AI Assistant")
    print("Type 'exit' to quit")

    while True:
        command = input(">> ").strip()
        if command.lower() == "exit":
            print("Exiting DeskBot...")
            break

        handle_command(command)

if __name__ == "__main__":
    main()
