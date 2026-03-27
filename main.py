from task_agent import task_agent_add, task_agent_show
from notes_agent import add_note, show_notes

def suggestion_agent():
    return "💡 Tip: Stay consistent! Complete your tasks on time."

def main_agent(user_input):
    user_input = user_input.lower()

    if "add task" in user_input:
        return task_agent_add(user_input)

    elif "show task" in user_input:
        return task_agent_show()

    elif "add note" in user_input:
        return add_note(user_input)

    elif "show note" in user_input:
        return show_notes()

    elif "suggest" in user_input:
        return suggestion_agent()

    else:
        return "🤖 Try: add task / show task / add note / show note / suggest"


print("🚀 Multi-Agent AI Assistant Started!")
print("Type 'exit' to stop\n")

while True:
    user_input = input("👉 You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    response = main_agent(user_input)
    print("🤖:", response)