#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Need package => pip install translate
from translate import Translator

options = Translator(from_lang='pt-br', to_lang='spanish')

input_string = "Vamos agitar isso pessoal!"

translate = options.translate(input_string)
print(translate)  # ¡Vamos a sacudir esto, chicos!
