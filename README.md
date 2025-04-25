# 📡 DS18B20 Temperature Sensor Python Library

Python library for reading temperature from the DS18B20 1-Wire digital temperature sensor on Raspberry Pi.

> 🌡️ Simple and minimal library to initialize, read, and (optionally) clean up DS18B20 sensor readings.

---

## 📦 Features

- Sensor auto-initialization via `modprobe`
- Read temperature in Celsius
- Clean and modular object-oriented design
- CLI-mode: real-time reading at 1-second interval when run as script

---

## 🛠 Requirements

- Raspberry Pi with GPIO support
- DS18B20 temperature sensor connected and enabled
- Python 3.x
- `w1-gpio` and `w1-therm` kernel modules enabled

---

## 🚀 Installation

1. Enable 1-Wire interface on Raspberry Pi:
   ```bash
   sudo raspi-config
   # → Interface Options → 1-Wire → Enable
   sudo reboot
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/maido-39/ds18b20-python-lib.git
   cd ds18b20-python-lib
   ```

3. Run the script directly:
   ```bash
   python3 ds18b20_sensor_lib.py
   ```

---

## 🧪 Example Code

```python
from ds18b20_sensor_lib import DS18B20Sensor

sensor = DS18B20Sensor()

try:
    temperature = sensor.get_temperature_celsius()
    print(f"Current Temperature: {temperature:.2f}°C")
finally:
    sensor.cleanup()
```

---

## 🔁 CLI Mode

If you run `ds18b20_sensor_lib.py` directly, it will output the temperature in Celsius every second:

```bash
$ python3 ds18b20_sensor.py
Current Temperature: 23.56°C
Current Temperature: 23.56°C
...
```

Press `Ctrl+C` to exit.

---

## 🧹 Cleanup

The `cleanup()` function is included for future expansion or if unloading of modules becomes necessary, but it is currently a placeholder.

---
