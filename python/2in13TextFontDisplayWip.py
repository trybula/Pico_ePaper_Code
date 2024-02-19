import Century # Century Gothic ttf font converted using font_to_py.py (in my case 22 px height)
from pico_epaper import EPD_2in13_V3_Landscape #pico_epaper is renamed waveshare file suitable for my display
import framebuf

def rotate_invert_framebuf(fb, width, height):
    new_fb = framebuf.FrameBuffer(bytearray(width * height), height, width, framebuf.MONO_HMSB)
    for y in range(height):
        for x in range(width):
            new_fb.pixel(y, x, 1 - fb.pixel(x, y))
    return new_fb

def Font_text_display(text, font, x, y):
    global epd
    for n in text:
        char = font.get_ch(n)
        fbuf = framebuf.FrameBuffer(bytearray(char[0]), char[1], char[2], framebuf.MONO_HMSB)
        fbuf = rotate_invert_framebuf(fbuf, char[1], char[2])
        epd.blit(fbuf, x, y)
        x+=char[2]

epd = EPD_2in13_V3_Landscape()
epd.init()
black=0x00
white=0xff

epd.fill(white)
Font_text_display('Lorem Ipsum' , Century, 5, 5)

epd.display(epd.buffer)
epd.sleep()
