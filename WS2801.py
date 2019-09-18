# The MIT License (MIT)
#
# Copyright (c) 2016 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import utime as time


def RGB_to_color(r, g, b):
    """Convert three 8-bit red, green, blue component values to a single 24-bit
    color value.
    """
    return ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)


def color_to_RGB(color):
    """Convert a 24-bit color value to 8-bit red, green, blue components.
    Will return a 3-tuple with the color component values.
    """
    return ((color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF)


class WS2801Pixels:
    """WS2801/SPI interface addressable RGB LED lights."""

    def __init__(self, count, spi):
        """Initialize set of WS2801/SPI-like addressable RGB LEDs.  Must
        specify the count of pixels, and either an explicit clk (clokc) and do
        (data output) line for software SPI or a spi instance for hardware SPI.
        """
        self._spi = spi
        # Setup buffer for pixel RGB data.
        self._count = count
        self._pixels = bytearray(count * 3)

    def show(self):
        """Push the current pixel values out to the hardware.  Must be called to
        actually change the pixel colors.
        """
        self._spi.write(self._pixels)
        time.sleep(0.002)

    def count(self):
        """Return the count of pixels."""
        return self._count

    def set_pixel(self, n, color):
        """Set the specified pixel n to the provided 24-bit RGB color.  Note you
        MUST call show() after setting pixels to see the LEDs change color!"""
        r = color >> 16
        g = color >> 8
        b = color
        # Note the color components will be truncated to 8-bits in the
        # set_pixel_rgb function call.
        self.set_pixel_rgb(n, r, g, b)

    def set_pixel_rgb(self, n, r, g, b):
        """Set the specified pixel n to the provided 8-bit red, green, blue
        component values.  Note you MUST call show() after setting pixels to
        see the LEDs change color!
        """
        assert n >= 0 and n < self._count, "Pixel n outside the count of pixels!"
        self._pixels[n * 3] = r & 0xFF
        self._pixels[n * 3 + 1] = g & 0xFF
        self._pixels[n * 3 + 2] = b & 0xFF

    def get_pixel(self, n):
        """Retrieve the 24-bit RGB color of the specified pixel n."""
        r, g, b = self.get_pixel_rgb(n)
        return (r << 16) | (g << 8) | b

    def get_pixel_rgb(self, n):
        """Retrieve the 8-bit red, green, blue component color values of the
        specified pixel n.  Will return a 3-tuple of red, green, blue data.
        """
        assert n >= 0 and n < self._count, "Pixel n outside the count of pixels!"
        return (self._pixels[n * 3], self._pixels[n * 3 + 1], self._pixels[n * 3 + 2])

    def set_pixels(self, color=0):
        """Set all pixels to the provided 24-bit RGB color value.  Note you
        MUST call show() after setting pixels to see the LEDs change!"""
        for i in range(self._count):
            self.set_pixel(i, color)

    def set_pixels_rgb(self, r, g, b):
        """Set all pixels to the provided 8-bit red, green, blue component color
        value.  Note you MUST call show() after setting pixels to see the LEDs
        change!
        """
        for i in range(self._count):
            self.set_pixel_rgb(i, r, g, b)

    def clear(self):
        """Clear all the pixels to black/off.  Note you MUST call show() after
        clearing pixels to see the LEDs change!
        """
        self.set_pixels(0)
