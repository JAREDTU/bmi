h = input ('請輸入身高: ')
h = int(h)
w = input ('請輸入體重: ')
w = int(w)
bmi = w / (h / 100 ) ** 2
if bmi < 18.5:
	print ('BMI值為: ', bmi, '體重過輕' )
elif bmi >= 18.5 and bmi < 24:
	print ('BMI值為: ', bmi, '正常範圍')
elif bmi >= 24 and bmi <27:
	print ('BMI值為: ', bmi, '過重')
elif bmi >= 27 and bmi <30:
	print ('BMI值為: ', bmi, '輕度肥胖')
elif bmi >= 30 and bmi <35:
	print ('BMI值為: ', bmi, '中度肥胖')
else:
	print ('BMI值為: ', bmi, '重度肥胖')

