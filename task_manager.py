from api_integrations import call_external_api

def execute_task(command: str):
    if "status" in command:
        print("System running normally.")
    elif "api" in command:
        response = call_external_api()
        print(f"API Response: {response}")
    else:
        print("Task not recognized. Please try again.")
