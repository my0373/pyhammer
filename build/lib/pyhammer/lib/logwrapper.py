__author__ = 'myork'

import logging

def logdebug(message,context_id=0):
    """
    Wrapper to make sure (at least my modules) contain a context_id 
    
    """
    logging.debug("%s:%s" % (context_id,
                             message))



def logwarn(message,context_id=0):
    """
    Wrapper to make sure (at least my modules) contain a context_id 
    
    """
    logging.warn("%s:%s" % (context_id,
                             message))    


def logcrit(message,context_id=0):
    """
    Wrapper to make sure (at least my modules) contain a context_id 
    
    """
    logging.crit("%s:%s" % (context_id,
                             message))
    
def logerror(message,context_id=0):
    """
    Wrapper to make sure (at least my modules) contain a context_id 
    
    """
    logging.error("%s:%s" % (context_id,
                             message))
    
    
def loginfo(message,context_id=0):
    """
    Wrapper to make sure (at least my modules) contain a context_id 
    
    """
    logging.info("%s:%s" % (context_id,
                             message))