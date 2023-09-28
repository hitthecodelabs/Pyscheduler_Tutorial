
import sys
import traceback

def log_error():
    try:
        # Your code here
        pass
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        error_l = exc_tb.tb_lineno
        cadena_error = str(exc_type) + " => " + str(exc_obj)
        error_info = traceback.format_exc()

        # Append the error details to the error_log.txt
        with open('error_log.txt', 'a') as f:
            f.write(cadena_error + "\n" + error_info + "\n\n")

if __name__ == "__main__":
    log_error()
