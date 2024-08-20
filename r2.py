
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	name = None
	allen_word = 0
	viki_word = 0
	allen_sticker = 0
	viki_sticker = 0
	allen_image = 0
	viki_image = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2: ]:
				if m == '貼圖':
					allen_sticker += 1
				elif m == '圖片':
					allen_image += 1
				else:
					allen_word += len(m)					
		elif name == 'Viki':
			for m in s[2: ]:
				if m == '貼圖':
					viki_sticker += 1
				elif m == '圖片':
					viki_image += 1
				else:	
					viki_word += len(m)
	print('Allen說了', allen_word, '個字')
	print('Allen傳了', allen_sticker, '個貼圖')
	print('Allen傳了', allen_image, '張照片')
	print('Viki說了', viki_word, '個字')
	print('Viki傳了', viki_sticker, '個貼圖')
	print('Viki傳了', viki_image, '張照片')
	



def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:	
			f.write(line + '\n')

def main():
	lines = read_file('Line-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)
main()
