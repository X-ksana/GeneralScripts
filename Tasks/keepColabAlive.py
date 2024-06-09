"""
# Alive colab
- To avoid restarting the kernel due to inactivity while reading references/ searching solutions for certain tasks
- Not to overuse; I used it on cpu.
- Methods: Simple loop or sending signals to server at regular basis

"""

# 1. Create thread that runs a function to print a message every 5 minutes. 
# The flush=True ensures that the message is immediately printed, which helps to interact with the server and prevent disconnection.

import time

def keep_alive():
    while True:
        # Perform a minimal operation, such as printing the current time
        print("Keeping the session alive", flush=True)
        time.sleep(300)  # Wait for 5 minutes

# Start the keep_alive function in a separate thread
import threading
keep_alive_thread = threading.Thread(target=keep_alive)
keep_alive_thread.start()

# Else, small computation:
# Function to perform a minimal operation
def keep_session_active():
    while True:
        # Minimal operation (e.g., computing a small sum)
        _ = sum([i for i in range(100)])
        print("Keeping session alive with minimal operation")
        time.sleep(300)  # Wait for 5 minutes

# Start the background task
import threading
background_task = threading.Thread(target=keep_session_active)
background_task.start()


# 2. Use jave to stimulate
#  injects JavaScript into the notebook that simulates a keydown event every 5 minutes

from Ipython.display import javascript
# # JavaScript to simulate a click every 5 minutes
js_code = """
function keepAlive() {
    setInterval(() => {
        console.log('Simulating activity to keep the session alive');
        document.querySelector('body').dispatchEvent(new KeyboardEvent('keydown'));
    }, 300000);  // 300000 ms = 5 minutes
}
keepAlive();
"""

display(Javascript(js_code))
