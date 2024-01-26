# logging level 3

# After some tests I decided to give it a try to the logging library:

import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)

# Use the logger as a context manager
with logging.LoggerAdapter(logging.getLogger(__name__), {'user': 'John Doe'}) as logger:
    logger.info('This log message is enhanced with extra context.')

# Regular logging outside the context manager
logging.info('This log message is outside the context manager.')


# So now whenever we need to log, we can use the statement with just like when we open
# files, and the handling of the resource is done automatically. Also looks smaller and 
# simpler to read...

# But!!!!

# By now my code is about 10K, and any single line of code that i repeat twice
# becomes kind of annoying. Also there are many places in the code that have 
# exception handling, so mixing log statements with logging becomes sort of a mess...
# So lets see the current version of logging.... 