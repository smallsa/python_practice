names = ['kele', 'xuebi', 'didi', 'jiejie']
for i in range(len(names)):
    print(names[i].title()+' '+'我想和你共进晚餐')
print(names[0].title()+' '+'无法共进晚餐')
names[0] = 'yeye'
for j in range(len(names)):
    print(names[j].title()+' '+'我想和你共进晚餐')
print('我找到了一个更大的餐桌')
names.insert(0, 'popo')
names.insert(3, 'shiyi')
names.append('last')
for k in range(len(names)):
    print(names[k].title()+' '+'我想和你共进晚餐')

print('抱歉，我只能邀请两位嘉宾共进晚餐')
print(names.pop(0)+' '+'很抱歉无法与你共进晚餐')
print(names.pop(0)+' '+'很抱歉无法与你共进晚餐')
print(names.pop(0)+' '+'很抱歉无法与你共进晚餐')
print(names.pop(0)+' '+'很抱歉无法与你共进晚餐')
print(names.pop(0)+' '+'很抱歉无法与你共进晚餐')
print(names[0].title()+' '+'很高兴与你共进晚餐')
print(names[1].title()+' '+'很高兴与你共进晚餐')
del names[0]
del names[0]
print(names)


