import os #作業系統(operating system)

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding= 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
					#跳過的意思,跳到下一個迴圈的意思
				name,price = line.strip().split(',')#.strip 清除（\) 和空格用
				products.append([name, price])
		return products


#使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		price = int(price)
		products.append([name, price])
	print(products)
	return products #回傳出來

#印出所有購買資訊
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])


#寫入檔案fi

def write_file(filename, products):
	with open(filename , 'w', encoding='utf-8') as f:
		#encoding='utf-8' 解決亂碼問題
		 f.write('商品,價格\n')
		 for p in products:
		 	f.write(p[0] + ',' + str(p[1]) + '\n')
			#str = 變為字串


def main():
	filename = ('products')
	if os.path.isfile(filename): #檢查檔案是否存在
		print('檔案存在')
		products = read_file('products.csv')
	else:
		print('檔案未建立')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
