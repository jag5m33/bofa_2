import sys 
import logging 
#whenever an exception gets raised, i want to push my own custom message

# error, error_detail: sys (the error you are getting & error_detail, whcih is passed into the sys)
def error_message_details(error, error_detail: sys):

    # exc_info - execution information, first two not interest
    # the third:  _, _, exc_tb (gives you info about which file exception occured, which line etc)
    
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

        #[{x}] - x is just a placeholder to be filled later:
    error_message = "error occured in python script name: [{0}], line number: [{1}], error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error) 
    )
    return error_message


#call custom funciton predefined: Exception
class CustomException(Exception):
    # init - override the initial exception syntax w/ my own 
    def __init__(self, error_message, error_detail:sys):
        # super - run the EXCEPTION class METHODS but do it MY way with my parameters
        # automatically calls whatever function is called in origonal class: Exception: and save self.error_message 
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail = error_detail)
    # when we raise the custom exception this is the method it takes:
    def __str__(self):
        return self.error_message

    
if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e: # this e is our 'error message'
        logging.info('divide by zero error')
        raise CustomException(e, sys)

