import tkinter as tk
import webbrowser
import openai  # Reference to OpenAI model
# Uncomment this if needed in the future
openai.api_key = "Open-AI-API-key"

def search_youtube(query, language):
    """Search YouTube for the query in the specified language."""
    search_query = f"{query} {language}".replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={search_query}"
    return url

def generate_study_plan(topics, total_minutes):
    """Generate a simple study plan."""
    try:
        topics_list = topics.split(",")
        minutes_per_topic = total_minutes / len(topics_list)
        study_plan = "\n".join([
            f"Topic: {topic.strip()} - Study for {minutes_per_topic:.2f} minutes." for topic in topics_list
        ])
        return study_plan
    except ZeroDivisionError:
        return "Error: No topics provided. Please enter at least one topic."
    except Exception as e:
        return f"Error generating study plan: {e}"

def handle_study_plan():
    """Handle the study plan generation based on user input."""
    topics = topics_entry.get()
    total_hours = hours_entry.get()

    if not topics.strip():
        result_text.set("Error: Please enter at least one topic.")
        return

    if not total_hours.isdigit():
        result_text.set("Error: Please enter a valid number of total hours.")
        return

    total_minutes = int(total_hours) * 60  # Convert hours to minutes
    result = generate_study_plan(topics, total_minutes)
    result_text.set(result)

def handle_clear_doubt():
    """Handle doubt clearing by searching YouTube based on user input."""
    doubt = doubt_entry.get()
    language = language_entry.get()

    if not doubt.strip():
        result_text.set("Error: Please enter a doubt to clarify.")
        return

    if not language.strip():
        result_text.set("Error: Please specify a language.")
        return

    youtube_url = search_youtube(doubt, language)
    webbrowser.open(youtube_url)
    result_text.set(f"Search results opened in your browser for: {doubt} ({language})")

def handle_study_tips():
    """Display AI study tips."""
    study_tips = """
AI Study Tips:
1. Break study sessions into 25-minute focused intervals (Pomodoro Technique).
2. Review topics with active recall techniques.
3. Take short breaks to refresh your mind.
4. Summarize key points after studying each topic.
5. Practice problem-solving for better retention.
    """
    result_text.set(study_tips)

# Create the GUI
root = tk.Tk()
root.title("Personalized Study Planner and Doubt Solver")
root.geometry("700x600")
root.configure(bg="#f5f5f5")

# Header
header = tk.Label(root, text="Personalized Study Planner and Doubt Solver", font=("Arial", 20, "bold"), fg="#ffffff", bg="#4caf50")
header.pack(pady=10, fill="x")

# Topic input
topics_frame = tk.Frame(root, bg="#f5f5f5")
tk.Label(topics_frame, text="Enter Topics (comma-separated):", font=("Arial", 12), bg="#f5f5f5", fg="#333333").pack(anchor="w", pady=5)
topics_entry = tk.Entry(topics_frame, width=60, font=("Arial", 12), bg="#ffffff", fg="#333333", relief="solid")
topics_entry.pack(pady=5)
topics_frame.pack(pady=10, padx=20, fill="x")

# Hours input
hours_frame = tk.Frame(root, bg="#f5f5f5")
tk.Label(hours_frame, text="Total Hours Available:", font=("Arial", 12), bg="#f5f5f5", fg="#333333").pack(anchor="w", pady=5)
hours_entry = tk.Entry(hours_frame, width=20, font=("Arial", 12), bg="#ffffff", fg="#333333", relief="solid")
hours_entry.pack(pady=5)
hours_frame.pack(pady=10, padx=20, fill="x")

# Doubt input
doubt_frame = tk.Frame(root, bg="#f5f5f5")
tk.Label(doubt_frame, text="Enter Your Doubt:", font=("Arial", 12), bg="#f5f5f5", fg="#333333").pack(anchor="w", pady=5)
doubt_entry = tk.Entry(doubt_frame, width=60, font=("Arial", 12), bg="#ffffff", fg="#333333", relief="solid")
doubt_entry.pack(pady=5)
doubt_frame.pack(pady=10, padx=20, fill="x")

# Language input
language_frame = tk.Frame(root, bg="#f5f5f5")
tk.Label(language_frame, text="Preferred Language:", font=("Arial", 12), bg="#f5f5f5", fg="#333333").pack(anchor="w", pady=5)
language_entry = tk.Entry(language_frame, width=20, font=("Arial", 12), bg="#ffffff", fg="#333333", relief="solid")
language_entry.pack(pady=5)
language_frame.pack(pady=10, padx=20, fill="x")

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
plan_button = tk.Button(button_frame, text="Generate Study Plan", font=("Arial", 14), bg="#2196f3", fg="#ffffff", activebackground="#1976d2", activeforeground="#ffffff", relief="flat", command=handle_study_plan)
plan_button.pack(side="left", padx=10, pady=10)

clear_button = tk.Button(button_frame, text="Clear Doubt", font=("Arial", 14), bg="#4caf50", fg="#ffffff", activebackground="#388e3c", activeforeground="#ffffff", relief="flat", command=handle_clear_doubt)
clear_button.pack(side="left", padx=10, pady=10)

study_tips_button = tk.Button(button_frame, text="Show Study Tips", font=("Arial", 14), bg="#ff9800", fg="#ffffff", activebackground="#fb8c00", activeforeground="#ffffff", relief="flat", command=handle_study_tips)
study_tips_button.pack(side="left", padx=10, pady=10)

button_frame.pack()

# Result display
result_text = tk.StringVar()
result_label_frame = tk.Frame(root, bg="#e8f5e9", relief="solid", borderwidth=1)
tk.Label(result_label_frame, text="Result:", font=("Arial", 14, "bold"), bg="#e8f5e9", fg="#4caf50").pack(anchor="w", padx=10, pady=5)
result_label = tk.Label(result_label_frame, textvariable=result_text, wraplength=650, font=("Arial", 12), bg="#ffffff", fg="#333333", justify="left", relief="solid")
result_label.pack(pady=10, padx=10, fill="x")
result_label_frame.pack(pady=20, padx=20, fill="x")

# Main loop
root.mainloop()