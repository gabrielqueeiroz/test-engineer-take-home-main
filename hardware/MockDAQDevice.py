import time

class MockDAQDevice:
    def __init__(self, device_name):
        self.device_name = device_name
        self.digital_input_channels = {}
        self.digital_output_channels = {}
        self.toggled_pins = {}

    def configure_digital_input_channel(self, channel_name):
        self.digital_input_channels[channel_name] = False

    def configure_digital_output_channel(self, channel_name):
        self.digital_output_channels[channel_name] = False

    def read_digital_pin(self, channel_name):
        if channel_name in self.digital_input_channels:
            return self.digital_input_channels[channel_name]
        else:
            raise ValueError(f"Channel '{channel_name}' is not configured for digital input.")

    def write_digital_pin(self, channel_name, value):
        if channel_name in self.digital_output_channels:
            self.digital_output_channels[channel_name] = bool(value)
        else:
            raise ValueError(f"Channel '{channel_name}' is not configured for digital output.")

    def get_digital_output_status(self, channel_name):
        if channel_name in self.digital_output_channels:
            return self.digital_output_channels[channel_name]
        else:
            raise ValueError(f"Channel '{channel_name}' is not configured for digital output.")

    def toggle_digital_input_pin(self, channel_name):
        if channel_name not in self.digital_input_channels:
            raise ValueError(f"Channel '{channel_name}' is not configured for digital input.")

        start_time = time.time()

        if channel_name in self.toggled_pins:
            self.digital_input_channels[channel_name] = False
            del self.toggled_pins[channel_name]
        else:
            self.digital_input_channels[channel_name] = True
            self.toggled_pins[channel_name] = time.time()

        elapsed_time = time.time() - start_time
        
        if abs(elapsed_time - 1) > 1:
            raise RuntimeError(f"Timing error: Elapsed time was {elapsed_time} seconds.")

        time.sleep(max(0, 1 - elapsed_time))

    def toggled_pins_rate(self):
        rates = {}
        start_time = time.time()

        for pin, toggle_time in self.toggled_pins.items():
            elapsed_time = start_time - toggle_time
            rates[pin] = 1 / elapsed_time

        return rates
    
    def timing_accuracy(self, channel_name):
        try:
            self.toggle_digital_input_pin(channel_name)
            return True
        except RuntimeError:
            return False