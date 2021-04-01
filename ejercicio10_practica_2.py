def get_total_value(table_values, word):
  """ Esta funcion calcula el valor de la palabra ingresada por teclado.

  dicci_value es un diccionario de forma letra:valor
  """
  chars = list(word)
  total_value = 0
  for current_char in chars:
    total_value += table_values[current_char] 
  return total_value            
              
def read_word():
  """ Esta funcion retorna la palabra ingresada por teclado en formato mayuscula """
  return input("Ingrese una palabra: ").upper()
  
def get_scrabble_tabe_values():
  """ Esta funcion retorna un diccionario con la representacion de la tabla de valores del juego Scrabble """
  return { 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P':3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'k': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10 } 

scrabble_tabe_values = get_scrabble_tabe_values()
word = read_word()
total_value = get_total_value(scrabble_tabe_values, word)
print (f"Valor total: {total_value}")

