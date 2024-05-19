import time as t

try:
    diary = open("user_diary.txt", "r+")
    diary_lines = diary.readlines()
    diary.truncate(0)
except FileNotFoundError:
    diary = open("user_diary.txt", "x+")
    diary_lines = diary.readlines()
try:
    dates_file = open("user_diary_dates.txt", "r+")
    date_lines = dates_file.readlines()
    dates_file.truncate(0)
except FileNotFoundError:
    dates_file = open("user_diary_dates.txt", "x+")
    date_lines = dates_file.readlines()
def save(f, df, ls, ds):
    print("Saving... do not exit the program, it will do that on its own.")
    for l in ls:
        f.write(f"{l}\n")
    for d in ds:
        df.write(f"{d}\n")
    exit()
def mainloop(file, lines, task, dates, dfile):
    if task == "A":
        date = t.strftime("%A, %b %d, %Y at %I:%M:%S %p")
        dates.append(f"{date}\n")
        bas = input("What do you want to say in your entry? --> ")
        entry = f"{date} - {bas}"
        lines.append(entry)
    elif task == "D":
        print("Here are the dates, as well as their numbers:")
        for d in dates:
            curr = dates.index(d) + 1
            print(f"{curr}) {d}")
        to_del = int(input("Enter the number of the entry to delete (see numbers before dates in above list) --> ")) - 1
        try:
            del dates[to_del]
            del lines[to_del]
        except IndexError:
            print(f"Invalid number ({to_del + 1} > {len(date_lines)}).")
    elif task == "V":
        for d in dates:
            curr = dates.index(d) + 1
            print(f"{curr}) {d}")
        to_see = int(input("Enter the number of the entry to view (see numbers before dates in above list) --> ")) - 1
        try:
            print(lines[to_see])
        except IndexError:
            print(f"Invalid number ({to_see + 1} > {len(date_lines)}).")
    elif task == "Q":
        save(file, dfile, lines, dates)
    else:
        print("Invalid input.")
        save(file, dfile, lines, dates)

try:
    while True:
        wtd = input("""What do you wish to do?
                    To add an entry, type A.
                    To delete an entry, type D.
                    To view an entry, type V.
                    To exit, type Q.
                    
                    Enter your answer here --> """).upper()
        mainloop(diary, diary_lines, wtd, date_lines, dates_file)
except KeyboardInterrupt:
    print("KEYBOARD INTERRUPT DETECTED!")
    save(diary, dates_file, diary_lines, date_lines)
