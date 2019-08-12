import os #作業系統(operating system)


products = []
if os.path.isfile('products.csv'):
	print('檔案存在')
	with open('products.csv', 'r', encoding= 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
				#跳過的意思,跳到下一個迴圈的意思
			name,price = line.strip().split(',')#.strip 清除（\) 和空格用
			products.append([name, price])
	print(products)
else:
	print('檔案未建立')


#使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	price = int(price)
	products.append([name, price])
print(products)

#印出所有購買資訊
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv' , 'w', encoding='utf-8') as f:
	#encoding='utf-8' 解決亂碼問題
	 f.write('商品,價格\n')
	 for p in products:
	 	f.write(p[0] + ',' + str(p[1]) + '\n')
		#str = 變為字串
