import math

def f(a,b,c):
    return math.sin(a*b*c)/(a*a+b*b+c*c)

def main():
    s = float(input('s='))
    t = float(input('t='))
    p=(f(1,t*t,s)+f(t,s*s,1))/(1+f(1,t*s,1)**2)
    print(p)

if __name__ == '__main__':
    main()