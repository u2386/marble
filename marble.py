#! /usr/bin/env python
# coding: utf-8

from PIL import Image

DEGREE = 16
GRAY_COLORS = 'B0XCJVYOUL":!,. '[::-1]
DEFAULT_IMG = 'David.jpg'


def main():
    im_path = DEFAULT_IMG
    gim = Image.open(im_path).convert('L')
    width, height = gim.size
    scale = width // 64
    gim.thumbnail((width//scale, height//scale))
    width, height = gim.size
    buffer = []
    pixels = gim.getdata()
    for h in range(height):
        for w in range(width):
            buffer.append(GRAY_COLORS[(pixels[h * width + w] // DEGREE)])
        buffer.append('\n')
    with open('output.txt', 'wt') as out:
        out.write(''.join(buffer))


if __name__ == '__main__':
    main()
