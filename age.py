driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有' :
	print('只能輸入 有 或 沒有 喔...e04')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('為甚麼你開過車?屁孩!!')
elif driving == '沒有' :
	if age >= 18:
		print('你可以考駕照了...')
	else:
		print('再老一點就可以考了:)')