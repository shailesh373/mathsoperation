from mathoperation.addOp import addValue
from mathoperation.subOp import subValue
from mathoperation.multiOp import multiValue
from mathoperation.divOp import divValue

if __name__ == '__main__' :
    print ('this is main code')
    val1 = int(input('enter the first number = '))
    val2 = int(input('enter the second number = '))
    op = input('which op you want to do ? ' )

    if op.lower() == 'add':
        a1 = addValue(val1 ,val2)
        print(f'addition = {a1} ')
    elif op.lower() == 'sub':
        a2 = subValue(val1 ,val2) 
        print('substract' ,a2)
    elif op.lower() == 'multi':
        a3 = multiValue(val1 ,val2) 
        print('multiplication' ,a3)
    elif op.lower() == 'div':
        a4 = divValue(val1 ,val2) 
        print('division' ,a4)      
    else:
        print('please choose currect op add,sub' )
        

