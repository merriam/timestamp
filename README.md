timestamp
=========

Sublime Text 2 plug-in to insert TimeStamps into your file.  Type 'now' and then hit tab for a 
quick timestamp.


This is a plugin and repository made from my gist so that it can handle Pull Requests 
and be registered with Sublime Package Control.   The original code was written by [Rob 
Crowie] [1] and then fixed by [reima] [2].

#.  To install this:
       Sublime's menu Tools -> New Plugin..., 
       Paste this gist over the sample given (use the raw button to see the gist as text)
       Save the file in your Sublime Packages directory.   File -> Save As.. should suggest
       an appropriate spot.  I recommend the name timestamp.py
       All done.  It should work immediately.
#.  To use this:
       Type "date" and hit tab.  Also try the words `isoD`, `now`, `datetime`, `utcnow`, `utcdatetime`,
       `date` and `time` followed by tab.  You may have to hit tab twice if you have another matching symbol 
       in your current namespace.
       
#.  Here are the current timestamp formats:

<table>
<tr><td>timestamp</td><td>Sat, 06 Jul 2013 08:55:49</td></tr>
<tr><td>date</td><td>2013-07-06</td></tr>
<tr><td>time</td><td>08:55:49</td></tr>
<tr><td>now</td><td>2013-07-06T08:55:49</td></tr>
<tr><td>datetime</td><td>2013-07-06T08:55:49</td></tr>
<tr><td>isoD</td><td>2013-07-06T08:55:49</td></tr>
<tr><td>utcnow</td><td>2013-07-06T15:55:49</td></tr>
<tr><td>utcdatetime</td><td>2013-07-06T15:55:49</td></tr>
</table>

[1]: https://gist.github.com/robcowie "Rob Crowie"
[2]: https://gist.github.com/reima "reima"
