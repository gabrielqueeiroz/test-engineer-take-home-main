from MockDAQDevice import MockDAQDevice
import unittest

class TestMockDAQDevice(unittest.TestCase):
    def setUp(self):
        self.mock_daq = MockDAQDevice("MockDAQ")
        self.failure_pin = "Output_FAIL"
        self.all_tests_passed = True

    def tearDown(self):
        self.mock_daq.digital_input_channels = {}
        self.mock_daq.digital_output_channels = {}
        self.mock_daq.toggled_pins = {}

        if self._outcome.errors[1][1] is not None:
            self.all_tests_passed = False

    def tearDownModule(self):
        print(self.all_tests_passed)
        if self.all_tests_passed == False:
            self.mock_daq.configure_digital_output_channel(self.failure_pin)
            self.mock_daq.write_digital_pin(self.failure_pin, True)

    def test_toggle_rate_of_digital_pin(self):
        self.mock_daq.configure_digital_input_channel("Iput0")

        self.mock_daq.toggle_digital_input_pin("Input0")

        self.assertAlmostEqual(self.mock_daq.toggled_pins_rate()["Input0"], 1, delta=0.1)

    def test_timing_mechanism_accuracy(self):
        channel_name = "TestChannel"

        self.mock_daq.configure_digital_input_channel(channel_name)

        self.assertTrue(self.mock_daq.timing_accuracy(channel_name))

    def test_state_of_digital_pin_after_toggle(self):
        self.mock_daq.configure_digital_input_channel("Input2")

        self.mock_daq.toggle_digital_input_pin("Input2")
        
        self.assertTrue(self.mock_daq.read_digital_pin("Input2"))        

if __name__ == '__main__':
    unittest.main()
