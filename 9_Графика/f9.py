import scipy.integrate as integrate
import scipy.special as special
#В данном примере численно вычисляется значение определенного интеграла функции Бесселя
#  на отрезке [0,0.45] с помощью библиотеки QUADPACK (Fortran).
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
print(result)