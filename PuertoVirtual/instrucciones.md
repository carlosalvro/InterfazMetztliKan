# Instrucciones para abrir puerto virtual


- Para abrir el puerto serial, en una terminal de linux 

`$ socat -d -d pty,raw,echo=0,b115200 pty,raw,echo=0,b115200`

- Y se tiene que obtener algo como esto 
`2021/08/17 21:31:56 socat[8895] N PTY is /dev/pts/3`
`2021/08/17 21:31:56 socat[8895] N PTY is /dev/pts/4`
`2021/08/17 21:31:56 socat[8895] N starting data transfer loop with FDs [5,5] and [7,7]`

## Para probar que si funciona 
En otra terminal ponemos 
`$ cat /dev/pts/4`
	Y ahora le mandamos cosas en otra terminal con 
`$ echo hola :) > /dev/pts/3`

	Y en la terminal donde se escribio **cat ...** se debe de ver lo que se escribió
## Probar con archivo generador de numeros random
Igual que en el anterior abrimos una terminal y vemos lo que se manda a 4 con `cat`
y corremos el archivo `señal.py`