"""Markdown-based AI Daily Journal"""

import argparse
from pathlib import Path
from datetime import datetime
import random


REFLECTION_PROMPTS = [
    "What's one small thing that brought you joy today?",
    "What challenged you today, and what did you learn from it?",
    "What are you grateful for right now?",
    "What's on your mind that you need to get out?",
    "What progress did you make today, no matter how small?",
    "What would you do differently if you could redo today?",
    "Who or what inspired you today?",
    "What's something you're looking forward to?",
    "What did you do today that aligned with your values?",
    "What's one thing you want to remember about today?",
    "How did you take care of yourself today?",
    "Who in your family did you connect with today, and how did it go?",
    "Did you make a spiritual connection today? If so, how did it impact you?"
]


class Journal:
    def __init__(self, journal_dir="Journal"):
        """Initiating and defining the Journal file class"""
        self.journal_dir = Path(journal_dir)
        self.journal_dir.mkdir(exist_ok=True)


    def get_today_entry(self):
       """Get today file path"""
       date_str = datetime.now().strftime("%Y-%m-%d")
       return self.journal_dir/ f"{date_str}.md"
       

    def get_entry(self, date_str):
        """Get a specific date file path"""
        return self.journal_dir/ f"{date_str}.md"


    def create_entry(self):
        """Create a new journal entry"""
        print("="*80)
        print("="*20 + "AI Daily Journal" + "="*20)
        print("="*80)
        print()

        # Get the current date/time
        now = datetime.now()
        full_date = now.strftime("%A, %B %d, %Y")
        print(f"Today: {full_date}")
        print()

        file_path = self.get_today_entry()
        existing_entries = 0
        
        if file_path.exist():
            content = file_path.read_text()
            existing_entries = content.count("## 📝 Entry")
            print("You already have {existing_entries} {'entry' if existing_entries == 1 else 'entries'} today. Adding more!")
            print()

        # Get random prompt
        prompt = random.choice(REFLECTION_PROMPTS)
        print("Reflection Prompt:")
        print(f"{prompt}")
        print()

        print("Start writing (type 'done' on a new line to finish")

        lines = []
        while True:
            line = input("> ") 
            if line.strip().lower() =='done':
                break
            lines.append(line)
        
        entry_content = "\n". join(lines)

        if not entry_content.strip():
            print("\nx Empty entry. Not saved.")
            return
        







              


# Check if file exists
if file_path.exists():
    content = file_pathe.read_text()
else:
    content = ""
    

# Write file
file_path.write_text(content)

# List all journal files
entries = sorted(journal_dir.glob("*.md"))


parser = argparse.ArgumentParser(description="AI Daily Journal")

# Add subcommands
subparsers = parser.add_subparsers(dest='command')

# 'new' command'
new_parser = subparsers.add_parser('new', help='Create new entry')

# 'list' command 
list_parser = subparsers.add_parser('list', help='List all entries')
list_parser.add_argument('--all', action='store_true', help='Show all entries')

# 'search' command 
search_parser = subparsers.add_parser('search', help='Search entries')
search_parser.add_argument('query', help='Search term')

# 'open' command
open_parser = subparsers.add_parser('open', help='Open entry')
open_parser.add_argument('date', help='Date (YYY-MM-DD)')

# Parse arguments
args = parser.parse_args()
if args.command == 'new': 
    create_entry()
elif args.command == 'list':
    list_entries(show_all=args.all)
elif args.command == 'search':
    search_entries(args.query)
elif args.command == 'open':
    open_entry(args.date)


prompt = random.choice(REFLECTION_PROMPTS)
print(f"Reflection Prompt:\n\"{prompt}\"")





































