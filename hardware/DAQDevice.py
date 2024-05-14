from MockDAQDevice import MockDAQDevice

mock_daq = MockDAQDevice("MockDAQ")

mock_daq.configure_digital_input_channel("DI0")
mock_daq.configure_digital_output_channel("DO0")

mock_daq.write_digital_pin("DO0", True)

input_value = mock_daq.read_digital_pin("DI0")

mock_daq.toggle_digital_input_pin("DI0")
print("Digital Input Value:", input_value)
