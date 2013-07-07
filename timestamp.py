# -*- coding: utf-8 -*-

from datetime import datetime
import sublime_plugin

#  Sublime Text 2 plug-in to insert TimeStamps into your file. Type 
# 'now' and then hit tab for a quick timestamp.
#
#  This is a plugin and repository made from my gist so that it can 
# handle Pull Requests and be registered with Sublime Package Control. 
# The original code was written by Rob Crowie and then fixed by reima.
#
#  To use this:
#   Type "date" and hit tab.  Also try the words `isoD`, `now`, `datetime`, 
#   `utcnow`, `utcdatetime`, `date` and `time` followed by tab.  You may have 
#    to hit tab twice if you have another matching symbol in your current namespace.
#
#  See https://github.com/merriam/timestamp for more informaiton.

class TimestampCommand(sublime_plugin.EventListener):
    """Expand `isoD`, `now`, `datetime`, `utcnow`, `utcdatetime`,
       `date`, `time`, and `timestamp`
    """
    def on_query_completions(self, view, prefix, locations):
        if prefix in ('isoD', 'now', 'datetime'):  # 2013-06-27T23:34:00
            val = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        elif prefix in ('utcnow', 'utcdatetime'):  # 2013-06-28T06:35:54
            val = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        elif prefix == 'date':       # 2013-06-27
            val = datetime.now().strftime('%Y-%m-%d')
        elif prefix == 'time':       # 23:34:12
            val = datetime.now().strftime('%H:%M:%S')
        elif prefix == 'timestamp':  # Thu, 27 Jun 2013 23:36:15
            val = datetime.now().strftime('%a, %d %b %Y %H:%M:%S')
        else:
            val = None

        return [(prefix, prefix, val)] if val else []
