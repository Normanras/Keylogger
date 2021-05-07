import shutil
import os
import datetime
import re
from datetime import datetime

dateTime = datetime.now()
dateObj = dateTime.date()
timeObj = dateTime.time().isoformat(timespec='minutes')
user = os.path.expanduser('~')

date = input("What is the date of the file? Format (%Y-%M-%D):   ")
shutil.copy2("log_{}.txt".format(date), "cleanup_{}.txt".format(date))
shutil.copy2("log_{}.txt".format(date), "deletions_{}.txt".format(date))
deletions_file = ("deletions_{}.txt".format(date))
cleanup_file = ("cleanup_{}.txt".format(date))

def docdata():
    with open(deletions_file, 'r') as a:
        for line in a:
            a2 = a.read()
            alength = len(a2)
            awords = a2.split()
            a2words = len(awords)
            comword = Counter(awords)
            a_occur = comword.most_common(4)
            a.close(deletions_file)

    suma = open(deletions_file, "w")
    suma.write(f"\n** Total length in characters: {alength} **"+f"\n** Number of words: {a2words} **")
    suma.write(f"\n** Most Common Words: {a_occur} **")
    
    with open(cleanup_file, "r") as b:
        for line in b:
            b2 = b.read()
            blength = len(b2)
            bwords = b2.split()
            b2words = len(bwords)
            bomword = Counter(bwords)
            b_occur = bomword.most_common(4)
            b.close(cleanup_file)
    
    sumb = open(cleanup_file, "w")
    sumb.write(f"\n**Total length in characters: {blength}**"+f"\n**Most used word: {b2words}")
    sumb.write(f"\n** Most Common Words: {b_occur} **")


def remove_spaces(spaces):
    doc = open(current_file, "w")
    doc.read
    cleaned = re.sub("s+", " ", doc)
    return(cleaned)

def backspace_cleanup(grep):
    delt = open(deletions_file, "r")
    data = delt.read()
    greps = data.count("|")


def close_program():
    delclose = open(deletions_file, "a")
    delclose.write("\n**~~ Program End. ~~**"+f"\nDate: {dateObj}" + f"\nTime: {timeObj}")
    delclose.close()
    
    curclose = open(cleanup_file, "a")
    curclose.write("\n**~~ Program End. ~~**"+f"\nDate: {dateObj}" + f"\nTime: {timeObj}")
    curclose.close()

close_program()