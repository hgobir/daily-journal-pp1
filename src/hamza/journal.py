import argparse
import pathlib
import os
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
    "What's one thing you want to remember about today?"
]



NEW_JOURNAL_TEMPLATE_1 = """
=====================================================
AI DAILY JOURNAL
=====================================================

Today: {}, {} {}, {}

💭 Reflection Prompt:\n\"{}\"

Start writing (type 'done' on a new line to finish):\n
"""

NEW_JOURNAL_TEMPLATE_2 = """

✓ Journal entry saved!
  File: {}
  Words: {}
  Characters: {}
"""


NEW_JOURNAL_TEMPLATE_FULL = """
=====================================================
AI DAILY JOURNAL
=====================================================

Today: {} {}

💭 Reflection Prompt:\n\"{}\"

Start writing (type 'done' on a new line to finish):
{}
✓ Journal entry saved!
  File: {}
  Words: {}
  Characters: {}
"""



NEW_JOURNAL_ENTRY = """
# {}, {} {}, {}

## 📝 Entry {} - {}

**Prompt:** {}

{}

---
"""


parser = argparse.ArgumentParser(description='Daily Journal')

subparsers = parser.add_subparsers(dest='command')

new_parser = subparsers.add_parser("new", help='generates new journal')

list_parser = subparsers.add_parser('list', help='list all journals')
list_parser.add_argument('--all', action='store_true', help='Show all entries')

search_parser=subparsers.add_parser('search', help='searches all journals')
search_parser.add_argument('query', action='store_true', help='Search term')

open_parser=subparsers.add_parser("open", help='opens specific journal')
open_parser.add_argument('date', action='store_true', help='Date (YYY-MM-DD)')

args = parser.parse_args()

if args.command == 'new':

    print("testing new")

    print("about to create new entry")


    journal_dir = pathlib.Path('src/hamza/journal')
    journal_dir.mkdir(exist_ok=True)

    now  =datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    day_name = now.strftime("%A")
    month_name = now.strftime("%B")
    day_date_name = now.strftime("%d")
    year_name =  now.strftime("%Y")

    time_str = now.strftime("%H:%m:%S %p")

    print(f"{date_str} {day_name}")

    prompt = random.choice(REFLECTION_PROMPTS)

    print(NEW_JOURNAL_TEMPLATE_1.format(day_name, month_name, day_date_name, year_name,  prompt))

    is_done = False

    content = ""

    while not is_done:


        intermediate_content = input()

        if intermediate_content == 'done':
            is_done = True
        else:
            content += "\n" + intermediate_content


    file_path = journal_dir / f"{date_str}.md"

    content_arr = content.split()
    content_arr_len = len(content_arr)

    c_count = 0
    for word in content_arr:

        for letter in word:

            c_count+=1



    print(c_count)
    print(NEW_JOURNAL_TEMPLATE_2.format(file_path, content_arr_len, c_count))


    print(time_str)

    entry_data = {
        'date': date_str,
        'date_name': day_name,
        'entry_number': 1,
        'timestamp': time_str,
        'prompt': prompt,
        'content': content,
        'word_count': content_arr_len,
        'char_count': c_count
    }





    new_entry = NEW_JOURNAL_ENTRY.format(day_name, month_name, day_date_name, year_name, 1, time_str, prompt, content)


    file_path.write_text(new_entry)


    




    # datetime.s

    file_path = journal_dir / f"{date_str}.md"
    # print(date_str)


    # new_parser.





elif args.command == 'list':
    print(f"testing list")
elif args.command == 'search':
    print(f"testing search")
elif args.command == 'open':
    print(f"testing open")
else:
    print("Invalid argument!")




































