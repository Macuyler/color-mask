import sys
import Image

def rgb(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def main():
	input_path = str(sys.argv[1])
	output_path = str(sys.argv[2])
	r, g, b = rgb(sys.argv[3])

	im = Image.open(input_path)   
	out = Image.new('RGBA', im.size, (0, 0, 0, 0))

	width, height = im.size
	for x in range(width):
    		for y in range(height):
        		p = im.getpixel((x,y))
        		if p[3] != 0:
            			out.putpixel((x,y), (r, g, b, p[3]))
	out.save(output_path, "PNG")
	out.show()
	return


if __name__ == '__main__':
	main()
