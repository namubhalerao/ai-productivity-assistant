tasks = []

def task_agent_add(user_input):
    task = user_input.replace("add task", "").strip()
    tasks.append(task)
    return f"✅ Task Added: {task}"

def task_agent_show():
    if not tasks:
        return "No tasks yet"
    
    result = "📋 Your Tasks:\n"
    for i, t in enumerate(tasks, 1):
        result += f"{i}. {t}\n"
    
    return result