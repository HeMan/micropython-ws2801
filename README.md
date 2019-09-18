# MicroPython WS2801

A MicroPython library to interface with strands of WS2801 RGB LEDs. It's based
on Adafruit WS2801 library for regular Python.

## Examples

Copy the file to your device, using ampy, webrepl or compiling and deploying. eg.

```bash
$ ampy put ws2801.py
```

**Use a 7 pixel strand and set all LED's red**
```python
from machine import SPI
from ws2801 import WS2801Pixels

spi = SPI(1)
ws = WS2801Pixels(7, spi)

ws.set_pixels_rgb(255, 0, 0)
ws.show()
```

## Links

* [Adafruit WS2801](https://github.com/adafruit/Adafruit_Python_WS2801)
* [micropython.org](http://micropython.org)
* [Adafruit Ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)

## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).
