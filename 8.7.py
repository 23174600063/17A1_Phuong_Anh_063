a=int(input("nhập số điện:"))
if a>400:
    s=1678*50+50*1734+100*2014+100*2536+100*2834+(a-400)*2927
if a>300:
    s=1678*50+50*1734+100*2014+100*2536+(a-300)*2834
if a>200:
    s=1678*50+50*1734+100*2014+(a-200)*2536
if a>100:
    s=1678*50+50*1734+(a-100)*2014
if a>50:
    s=1678*50+(a-50)*1734
else:
    s=1678*a
print("tiền điện:",s,"đồng")