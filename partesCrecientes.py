def partesCrecientes(lista):
	"""Recibe una lista de enteros con elementos unicos y devuelveun iterador
	 que genera todas las sublistas de la lista original que son crecientes."""
	
	# La lista vacia siempre es creciente y sublista de cualquier lista
	yield []

	# Para cada elemento de la lista
	for i in range(len(lista)):
		# generamos todas las sublistas crecientes de la lista que queda
		n = lista[i]
		for sublista in partesCrecientes(lista[i+1:]):
			# se les puede agregar  n si la sublista es vacia o el primer elemento es mayor que n
			if sublista == [] or sublista[0] > n:
				yield [n] + sublista

from sys import argv

if __name__ == '__main__':
	if len(argv) < 2:
		print("Uso: python partesCrecientes.py <lista>")
		exit(1)

	lista = [int(x) for x in argv[1:]]
	print("Lista:", lista)
	print("Partes crecientes:")
	for sublista in partesCrecientes(lista):
		print(sublista)