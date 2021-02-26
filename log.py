import os, sys, logging
 
SAVE_DIRECOTRY: str = os.path.dirname(os.path.realpath(__file__)) + '/Data/'
if not os.path.exists(SAVE_DIRECOTRY): os.makedirs(SAVE_DIRECOTRY)
 
def message_logger(FOLDER_NAME: str, USER_FILE: str = None, LEVEL=logging.DEBUG):
    '''
    FOLDER_NAME: This is the server's name log file and directory.
    USER_FILE: Each user gets their own log file in that server. By default it's set to None unless specified.
    LEVEL: The level of logging.
    '''
    ''' Make folder if it doesn't exist '''
    if not os.path.exists(SAVE_DIRECOTRY + FOLDER_NAME): os.makedirs(SAVE_DIRECOTRY + FOLDER_NAME)
    
    logger = logging.getLogger(FOLDER_NAME)
    logger.setLevel(LEVEL)
    log_format = logging.Formatter('%(asctime)s - %(message)s', datefmt='%A %B %d %Y %I:%M:%S%p')
    
    ''' Creating and adding the console handler '''
    # console_handler = logging.StreamHandler(sys.stdout)
    # console_handler.setFormatter(log_format)
    # logger.addHandler(console_handler)
    
    ''' Creating and adding the file handler '''
    if USER_FILE: file_handler = logging.FileHandler(SAVE_DIRECOTRY + FOLDER_NAME + f'/{USER_FILE}.log', mode='a+')
    else: file_handler = logging.FileHandler(SAVE_DIRECOTRY + FOLDER_NAME + f'/{FOLDER_NAME}.log', mode='a+')
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    return logger
 
 
def log_message(server: str, channel: str, username: str, message: str):
    s_log = message_logger(server)
    s_log.debug(f'{username}: {message}')
    close_logger(s_log) # If we don't close the loggers, then the loggers all log when ever we log anything.
    u_log = message_logger(server, username)
    u_log.debug(message)
    close_logger(u_log)
    c_log = message_logger(server, channel)
    c_log.debug(f'{username}: {message}')
    close_logger(c_log)
 
def close_logger(log):
    handlers = log.handlers.copy()
    for handler in handlers:
        try:
            handler.acquire()
            handler.flush()
            handler.close()
        except (OSError, ValueError): pass
        finally: handler.release()
        log.removeHandler(handler) 
 
if __name__ == "__main__":
    # cant guarentee the comments below work, just found them in some github issue.
    log_message(server='TheCodingJs', # message.guild 
                 channel='general', # message.channel.mention
                 username='Top of Tech', # message.author
                 message='Is this working?11111' # message.content
                 )