from translate import Translator  # pip install translate

options = Translator(from_lang='pt-br', to_lang='spanish')
input_string = "Vamos agitar isso pessoal!"

translate = options.translate(input_string)
print(translate)  # console: ¡Vamos a sacudir esto, chicos!
