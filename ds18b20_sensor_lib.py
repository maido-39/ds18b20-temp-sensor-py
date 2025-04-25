# ds18b20_sensor.py

import os
import glob
import time

class DS18B20Sensor:
    def __init__(self):
        self.initialized = False
        self.device_file = None
        self._initialize_sensor()

    def _initialize_sensor(self):
        """Initialize the DS18B20 sensor and locate the device file."""
        os.system('modprobe w1-gpio')   # Load 1-Wire GPIO module
        os.system('modprobe w1-therm')  # Load 1-Wire Thermometer module
        base_dir = '/sys/bus/w1/devices/'
        try:
            # Find the folder corresponding to the DS18B20 sensor (starts with '28')
            device_folder = glob.glob(base_dir + '28*')[0]
            self.device_file = device_folder + '/w1_slave'
            self.initialized = True
        except IndexError:
            raise RuntimeError('DS18B20 sensor not found. Please check the connection.')

    def read_temp_raw(self):
        """Read the raw temperature data from the sensor file."""
        with open(self.device_file, 'r') as f:
            return f.readlines()

    def get_temperature_celsius(self):
        """Parse and return the temperature in Celsius from the sensor."""
        if not self.initialized:
            raise RuntimeError('Sensor not initialized.')

        lines = self.read_temp_raw()
        retry_count = 0

        # Wait until the sensor output is valid (ends with 'YES')
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
            retry_count += 1
            if retry_count > 5:
                raise RuntimeError('Sensor is not responding.')

        # Extract temperature string after 't=' and convert to Celsius
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
        else:
            raise RuntimeError('Failed to parse temperature data.')

    def cleanup(self):
        """Clean up resources if needed (currently a placeholder)."""
        pass  # Example: os.system('rmmod w1-therm') if module unloading is required


# If the script is run directly, print temperature every second
if __name__ == '__main__':
    sensor = DS18B20Sensor()
    try:
        while True:
            temp_c = sensor.get_temperature_celsius()
            print(f"Current Temperature: {temp_c:.2f}°C")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by user.")
    finally:
        sensor.cleanup()
