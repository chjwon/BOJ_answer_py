color = {'black': '0',
         'brown': '1',
         'red': '2',
         'orange': '3',
         'yellow': '4',
         'green': '5',
         'blue': '6',
         'violet': '7',
         'grey': '8',
         'white': '9'
         }
colorList=[]
for _ in range(3):
    colorList.append(color[input()])
print(int((colorList[0]+colorList[1]+('0'*int(colorList[2])))))
