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
        """Initiating and defining the Journal class filing"""
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
        
        if file_path.exists():
            content = file_path.read_text()
            existing_entries = content.count("## 📝 Entry")
            print("You already have {existing_entries} {'entry' if existing_entries == 1 else 'entries'} today. Add more if you like.")
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
            if line.strip().lower() == 'done':
                break
            lines.append(line)
        
        entry_content = "\n".join(lines)

        if not entry_content.strip():
            print("\nEmpty entry. Not saved.")
            return
     
        entry_num = existing_entries + 1
        timestamp = now.strftime("%I:%M %p")

        entry_text = f"\n## 📝 Entry {entry_num} - {timestamp}\n\n"
        entry_text += f"**Prompt:** {prompt}\n\n"
        entry_text += entry_content
        entry_text += "\n\n---\n"

        # Add to file
        if file_path.exists():
            # Append to existing file
            current_content = file_path.read_text()
            file_path.write_text(current_content + entry_text)
        else:
            # create new file with day header
            day_header = f"# {full_date}\n"
            file_path.write_text(day_header + entry_text)

        # Stats
        word_count = len(entry_content.split())
        char_count = len(entry_content)

        print()
        print("Journal entrey saved!")
        print(f" File: {file_path}")
        print(f" Words: {word_count}")
        print(f" Characters: {char_count}")
        if existing_entries > 0:
            print(f" Entry: {entry_num} of {entry_num} today")

    
    def list_entries(self, show_all=False):
        """List all journal entries"""
        print("="*80)
        print("All journal entries")
        print("="*80)
        print()

        # Retrieve all markdown files
        entries = sorted(self.journal_dir.glob("*.md"), reverse=True)

        if not entries:
            print("No journal entries yet. Create one with 'journal.py new'")
            return
        
        print(f"Total entries: {len(entries)}")
        print()

        # Show entries
        limit = None if show_all else 7

        print("Recent entries:" if not show_all else "All entries:")

        for i, entry_file in enumerate (entries):
            if limit and i >= limit:
                break 

            # Parse date from file name
            date_str = entry_file.stem
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                day_name = date_obj.strftime("%A")
            except:
                day_name = "Unknown"


            # Find context around match
            content_lower = content.lower()
            query_lower = query.lower()

            index = content_lower.find(query_lower)

            # Extract 50 characters before and after
            start = max(0, index - 50)
            end = min(len(content), index + len(query) + 50)
            context = content(start:end)


            # Clean up context
            context = context.replace('\n', ' ').strip()
            if start > 0:
                context = "..." + context
            if end < len(content):
                context = context + "..."

                matches.append({
                    'date': date_str,
                    'day': day_name,
                    'context': context
                })




































