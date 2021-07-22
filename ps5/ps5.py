# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    # initialize the parameters
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    # define getters
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate




#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        punctuation = string.punctuation
        text = text.lower()
        for notation in punctuation:
            text = text.replace(notation,'')
            phrase = self.phrase.replace(notation,'')
        text = text.split(' ')
        phrase = phrase.split(' ')
        for word in phrase:
            if word not in text:
                return False

        text = ''.join(text)
        phrase = ''.join(phrase)
        text.replace(' ','')
        phrase.replace(' ','')

        if phrase not in text:
            return False

        return True

# if __name__ == '__main__':
#     # text = 'The purple cow is sof!!@)*$   dfhaoi'
#     text = 'COW!!!! Purple!!!'
#     phrase = 'purple cow'
#     bool = PhraseTrigger(phrase)
#     print(bool.is_phrase_in(text))

# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    def __init__(self, title):
        # the trigger phrase
        self.title = title.lower()

    def evaluate(self, story):
        Title = story.get_title()
        # the whole title
        punctuation = string.punctuation
        Title = Title.lower()
        for notation in punctuation:
            Title = Title.replace(notation, ' ')
            title = self.title.replace(notation, ' ')
        Title = Title.split(' ')
        title = title.split(' ')
        for word in title:
            if word not in Title:
                return False

        Title = ''.join(Title)
        title = ''.join(title)
        Title.replace(' ','')
        title.replace(' ','')
        if title not in Title:
            return False


        return True


# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, description):
        self.description = description.lower()

    def evaluate(self, story):
        Description = story.get_description()
        punctuation = string.punctuation
        Description = Description.lower()
        for notation in punctuation:
            Description = Description.replace(notation, ' ')
            description = self.description.replace(notation, ' ')
        Description = Description.split(' ')
        description = description.split(' ')
        for word in description:
            if word not in Description:
                return False

        Description = ''.join(Description)
        description = ''.join(description)
        Description.replace(' ', '')
        description.replace(' ', '')
        if description not in Description:
            return False

        return True

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, time):
        time = datetime.strptime(time,'%d %b %Y %H:%M:%S')
        self.time = time.replace(tzinfo=pytz.timezone("EST"))


# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        news_time = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return self.time>news_time
class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        news_time = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return self.time<news_time

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    triggered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                triggered_stories.append(story)

    return triggered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    dict = {}
    list = []
    for variable in lines:
        cmd = variable.split(',')
        # print(cmd)
        if cmd[1] == 'TITLE':
            dict[cmd[0]] = TitleTrigger(cmd[2])
        elif cmd[1] == 'DESCRIPTION':
            dict[cmd[0]] = DescriptionTrigger(cmd[2])
        elif cmd[1] == 'AFTER':
            dict[cmd[0]] = AfterTrigger(cmd[2])
        elif cmd[1] == 'BEFORE':
            dict[cmd[0]] = BeforeTrigger(cmd[2])
        elif cmd[1] == 'AND':
            dict[cmd[0]] = AndTrigger(dict[cmd[2]],dict[cmd[3]])
        elif cmd[1] == 'NOT':
            dict[cmd[0]] = NotTrigger(dict[cmd[2]])
        elif cmd[1] == 'OR':
            dict[cmd[0]] = OrTrigger(dict[cmd[2]],dict[cmd[3]])
        elif cmd[0] == 'ADD':
            for variable in cmd[1:]:
                list.append(variable)
        else:
            raise NotImplementedError

    return list



    # print(lines) # for now, print it so you see what it contains!

# if __name__ == '__main__':
#     read_trigger_config('triggers.txt')

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

