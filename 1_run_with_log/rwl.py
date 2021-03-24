import traceback

def run_with_log(func):
    with open('log.txt','a') as log:
        try:
            func()
        except Exception as e:
            tb = str(traceback.extract_tb(e.__traceback__))
            msg = str(type(e))+' '+str(e) + ' in function named \"' +func.__name__+ '\"' + '\n\t'+tb + '\n'
            log.write(msg)
            print(msg)