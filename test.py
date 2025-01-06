try:
    import time
    import RPi.GPIO as GPIO
    print("All necessary libraries are installed.")
except ImportError as e:
    print(f"Error importing library: {e}")
