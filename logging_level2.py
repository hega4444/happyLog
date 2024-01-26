# logging level 2

# My next step was to build a function:

import threading

# Create a lock
my_lock = threading.Lock()

def log_entry(self, log_object) -> bool:
# Log an entry in the log
    try:
        with my_lock:
            with open(self.log_file_name, 'a') as file:
                file.write(str(log_object).replace("\n", "") + '\n')

                print(str(log_object).replace("\n", "") + '\n')
    except IOError as e:
        print(f"An error occurred: {e.strerror}")



# So now we have a function that we can use along the code ans if we ever
# need to change the format, is gonna be much easier. 
# Also this tool logs on files too, very important when building secure systems.
# and everything is smoother.. but:

# If you notice this:
        # Create a lock
        # my_lock = threading.Lock()

# Is because when logging on files we need to make sure that we obtain the
# resource of the file and dont create problems when different parts of our
# program need to log. So lets see if there are better ways...