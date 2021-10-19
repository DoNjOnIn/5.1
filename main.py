import math

def func(a,b,c):
    return math.sin(a*b*c)/(a*a+b*b+c*c)

def main():
    s = float(input('s='))
    t = float(input('t='))
    p=(func(1,t*t,s)+func(t,s*s,1))/(1+func(1,t*s,1)**2)
    print(p)

if __name__ == '__main__':
    main()