# 密碼重試程式
password = 'a123456'
x = 3
while x > 0:
	pwd = input('請輸入密碼: ') 
	if pwd != password:
		x = x - 1
		if x > 0:
			print('密碼錯誤! 還有%x次機會 '%x)
		else:
			print('登入失敗!')
	else:
		print('登入成功!')
		break
