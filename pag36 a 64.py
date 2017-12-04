print 
print "ESTE PROGRAMA HALLA EL VALOR INTERMEDIO DE TRES VALORES"
a = input("ingrese a = ")
b = input("ingrese b = ")
c = input("ingrese c = ")
if a < b:
	max = b
	min = a
if max < c:
	max = c
if c < min:
	min = c
inter = (a+b+c)-(max + min)
print "intermedio es : ", inter




/////////////PAG 39

print 
print "ESTE PROGRAMA TE DICE SI FORMAN UN TRIANGULO O NO"
a = input("ingrese a = ")
b = input("ingrese b = ")
c = input("ingrese c = ")
if a>b:
	max = a
else:
	max = b
if max < c:
	max = c
s = (a+b+c)/2
if s > max:
	print "FORMAN TRIANGULO"
else:
	print "NO FORMAN TRIANGULO"
  
  /////////////////PAG 41
  
  print 
print "ESTE PROGRAMA EDINTIFICA DE UN NUMERO REAL EL SIGNO LA MAGNITUD Y LA FRACCION"
n = input("ingrese n = ")
if n > 0:
	signo = '+'
elif n == 0:
	signo = ''
else:
	signo = '-'
magnitud = float(abs(n))
entero = int(abs(magnitud))
fraccion = magnitud - entero
print
print "el signo es: ",signo," el entero es: ",entero," la fraccion es: ",fraccion




////////////PAG 43

print 
print "ESTE PROGRAMA EVALUA EL CUADRADO DE N"
n = input("ingrese n = ")
suma = 0
i = 1
while i<=n:
	suma = suma + (2*i-1)
	i = i + 1
print "la suma de cuadrados es ",suma


//////////PAG 45

print 
print "ESTE PROGRAMA SACA EL MAXIMO COMUN DIVISOR DE DOS NUMEROS"
a = input("ingrese a = ")
b = input("ingrese b = ")
while a != b:
	if a>b:
		a = a - b
	else:
		b = b -a
print "el MCD es ",b



//////////PAG 47

print 
print "ESTE PROGRAMA SACA EL RESIDUO DE DO NUMEROS"
a = input("ingrese a = ")
b = input("divido entre = ")
while (a % b)!= 0:
	r = (a % b)
	a=b
	b = r
print "el reciduo es ",b



///////PAG 49

print 
print "ESTE PROGRAMA NO DICE SI UN NUMERO E PRIMO O NO"
n = input("ingrese numero = ")
i = n/2

flag = True
while i>1 & flag == True:
	if n % i == 0:
		flag = False
	i = i - 1
if flag == True:
	print "es primo"
else:
	print "no es primo"
  
  
  ///////////PAG 51
  
  print 
print "ESTE PPROGRAMA HACE LA MULTIPLICACION RUSA"
a = input("ingrese valor de a = ")
b = input("ingrese valor de b = ")
suma = 0
while b>0:
	if b%2==1:
		suma = suma + a	
	a = 2*a
	b = abs(b/2)
print "la suma es ",suma


///////////PAG 53

print 
print "ESTE PPROGRAMA EVALUA EL EXPONECIAL APLICANDO LA SERIE DE TAYLOR DEL 1 A 15"
x = input("ingrese valor de x = ")
suma = 1
i = 1
t = 1
while (i<=15) & (abs(t) > -1):
	t = t * (x/i)
	suma = suma + t
	i = i + 1
print "la suma exponecial es ",suma


///////////PAG 55

print 
print "ESTE PPROGRAMA ES PARA DETERMINAR LA RAIZ APLICANDO EL ALGORITMO DE NEWTON"
n = input("ingrese valor de n = ")
x1 = 1

while True:
	x = x1
	x1 = 0.5*(x+(n/x))
	if abs(x-x1) <= 0.001:
		break
print "la interseccion es ",x1



//////////PAG 56

print
print "ESTE PROGRAMA SUMA LOS PRIMERO N NUMEROS ENTEROS"
n = input("ingerse el valor de n = ")
suma = 0
for i in range(0,n+1):
	suma = suma + i
print "la suma es ",suma


////////////PAG 57

print
print "ESTE PROGRAMA SUMA LOS PRIMERO N NUMEROS elevados al cuadrado"
n = input("ingerse el valor de n = ")
suma = 0
for i in range(0,n+1):
	suma = suma + (i*i)
print "la suma es ",suma




/////////PAG 58

print
print "ESTE PROGRAMA EVAL. 2 ALA N ITERATIVAMENTE"
n = input("ingerse el valor de n = ")
suma = 1
for i in range(1,n+1):
	suma = 2*suma
print "la suma es ",suma






///////PAG 60

print
print "ESTE PROGRAMA CALCULA EL SALARIO DE LOS N EMPLEADOS "
total = 0
contador = 0
numero = input("ingrese el numero de empleados: ")
while contador < numero:
	horas = input("ingrese horas: ")
	salario = input("ingrese salario: ")
	pago = horas * salario
	total = total + pago
	contador = contador + 1
	print "el pago es: ",pago
print "el total es: ",total





///////////PAG 62

n = input("ingrese n = ")
m = input("ingrese m = ")
x=1
y=1
for i in range(1,m):
	x = x*(n+1-i)
	y = y*i
coef = x/y
print "el coeficiente es: ",coef




///////////PAG 64

for n in range(1,99):
	for m in range((n+1),100):
		a = (m*m)-(n*n)
		b = 2*m*n
		h = (m*m)+(n*n)
		if h <= 100:
			print "valores",a ,b ,h
		

