import logging, time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-16s %(name)-14s %(levelname)-8s %(message)s',
    datefmt='%m-%d-%y %H:%M',
    filename='time.log',
    filemode='w',
)

import logging

logger = logging.getLogger('0xdhrv')
logger.info('--- New Log ---')

amOut = True
startInTime = 0
stopInTime = 0
totalInTime = 0
# Your Overall Time in **Seconds**
timeLeft = 30600

def snd(message):
    logger.info(message)


def inn(message):
    global amOut, startInTime, stopInTime, totalInTime, timeLeft
    if amOut == True:
        amOut = False
        startInTime = time.perf_counter() 
        print('|- Left {:.2f} Mn'.format((timeLeft-totalInTime)/60))
        print('|') 
        logger.info('IN  %s', message)
    else:
        print('! ERR: Already In')


def out(message):
    global amOut, startInTime, stopInTime, totalInTime, timeLeft
    if amOut == False:
        amOut = True
        stopInTime = time.perf_counter()
        timeDiff = stopInTime - startInTime
        totalInTime += timeDiff
        print('|- In For {:.2f} Mn'.format(timeDiff/60))
        print('|')
        logger.info('OUT %s', message)
        logger.info('+ {:.2f} Mn'.format(timeDiff/60))
    else:
        print('! ERR: Already Out')
