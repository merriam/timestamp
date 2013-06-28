# -*- coding: utf-8 -*-

from datetime import datetime
import sublime_plugin

# Adding too much documentation:
#  1.  The original Gist had %M instead of %m in the strftime() class.  %M means minute,
#   while %m means month as a decimal.  
#  2.  To install this:
#       Sublime's menu Tools -> New Plugin..., 
#       Paste this gist over the sample given (use the raw button to see the gist as text)
#       Save the file in your Sublime Packages directory.   File -> Save As.. should suggest
#       an appropriate spot.  I recommend the name timestamp.py
#       All done.  It should work immediately.
#  3.  To use this:
#       Type "date" and hit tab.  Also try the words `isoD`, `now`, `datetime`, `utcnow`, `utcdatetime`,
#       `date` and `time` followed by tab.  You may have to hit tab twice if you have another symbol in
#       your current namespace.

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
