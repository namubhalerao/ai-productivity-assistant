notes = []

def add_note(user_input):
    note = user_input.replace("add note", "").strip()
    notes.append(note)
    return f"📝 Note added: {note}"

def show_notes():
    if not notes:
        return "No notes yet"
    
    result = "🗒️ Your Notes:\n"
    for i, n in enumerate(notes, 1):
        result += f"{i}. {n}\n"
    
    return result