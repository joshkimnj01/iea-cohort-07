import operator
import math

def calulate(op_a, op_b, oper):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "Log": math.log,
    }
    operation =operations.get(oper)
    if operation:
        try:
            return operation(op_a,op_b)
        except (ZeroDivisionError, ValueError ) as e:
            print (f"?? Operations not supported ==  {e} ??")
        except TypeError:
            print ("?? Values not the same and not supported ??")
      
    return None
def main():

    print("compute log   ",calulate(1,9,"Log"))
    print("compute add   ",calulate(1,9,"+"))
    print("compute multiply  ",calulate(1,9,"*"))
    

if __name__=='__main__':
    main()
