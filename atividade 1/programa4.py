contador = 1
soma_nota = 0

while contador <= 4:
    nota = float(input(f"digite a nota do {  contador } bimestre"))
    if nota < 0 or nota > 10:
        print("nota invalida. A nots deve estar entre 0 e 10")
        continue
    contador += 1
    soma_nota += nota
media = soma_nota /4
print("A media de notas é: ",media )
if media >= 7:
     print("o aluno esta aprovado")
else: 
      print("o aluno esta reprovado")
      