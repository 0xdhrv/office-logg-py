

![](media/logg.svg)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F0xdhrv%2Flogg-py&count_bg=%23000000&title_bg=%23000000&icon=&icon_color=%23FFFFFF&title=%CE%BB+%3D%3E&edge_flat=true)](https://hits.seeyoufarm.com)

> never worry about your in-out timings, again

**logg** is a simple logger written in python, as a console application, that is completely off the grid, and also saves your office log timings with various information in time.log

you can see time left and time elapsed anytime, to take good quality breaks without any worries

-----
## bit of code

```python
# main.py
...
logger = logging.getLogger('0xdhrv')
logger.info('--- New Log ---')
...
# Your Overall Time in **Minutes**
timeLeft = 510
...

```

change `timeLeft` (**in minutes**) according to your office timing needs,

when you get to your office just . :


$ python logg.py
description: a simple logger written in python, as a console 
    application, that is completely off the grid

usage: logg.py
    options:
      i, to trigger in event, and enter in time
      o, to trigger out event, and enter out time
      t, to see time elapsed
      l, to see time left
      s, to send message, to log message
      q, to quit application
      h, to display this help message
```

-----
## bit of logs

```log
06-15-21 21:33   0xdhrv         INFO     --- New Log ---
06-15-21 21:33   0xdhrv         INFO     IN  Reached Office
06-15-21 21:33   0xdhrv         INFO     OUT Coffee Break
06-15-21 21:33   0xdhrv         INFO     + 0.17 min(s)
06-15-21 21:33   0xdhrv         INFO     IN  Back
06-15-21 21:34   0xdhrv         INFO     Meeting @1400, 15/06/2021
```
