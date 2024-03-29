<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Text-to-speech

### Reconhecimento de Voz e Sintetização de Fala

A síntese da fala é a produção artificial da fala humana. Um sistema de computador usado para essa finalidade é chamado
de computador de fala ou sintetizador de fala e pode ser implementado em produtos de software ou hardware. Um sistema de
texto para fala (TTS) converte o texto do idioma normal em fala; outros sistemas renderizam representações linguísticas
simbólicas como transcrições fonéticas em fala. [Wikipedia](https://en.wikipedia.org/wiki/Speech_synthesis)

----

Requirements:

```commandline
pip install PyAudio  
pip install SpeechRecognition  
pip install pocketsphinx
```

* [eSpeak](http://espeak.sourceforge.net/) eSpeak é um sintetizador de fala de software de código aberto compacto para
  inglês e outros idiomas, para Linux e Windows.
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) é uma biblioteca para realização de reconhecimento de
  fala, com suporte para diversos motores e APIs, online e offline.
* [PyAudio](https://pypi.org/project/PyAudio/) biblioteca de fluxo de entrada/saída de áudio multiplataforma.

----

#### _Let's Code!_

#### Speech Synthesis: Sintetização

A síntese de fala (TTS) é definida como a produção artificial de vozes humanas. O principal uso
(e o que induziu sua criação) é a capacidade de traduzir um texto em fala falada automaticamente.

* [Sintetização com <b>Espeak</b>.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/synthesis/synthesis_espeak.py)
* [Sintetização com <b>Pyttsx3</b>.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/synthesis/synthesis_pyttsx3.py)
* [Sintetização com <b>GTTS</b> (Google-text-Speech).](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/synthesis/synthesis_gtts.py)
* [Sintetização online <b>GTTS</b> (Google) ou offline <b>Pyttsx3</b>.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/synthesis/synthesis_google_on_offline.py)

#### Voice Recognition: Reconhecimento de voz

O reconhecimento de voz ou de alto-falante é a capacidade de uma máquina ou programa de receber e interpretar um ditado
ou de entender e executar comandos falados. O reconhecimento de voz ganhou destaque e uso com o surgimento de IA e
assistentes inteligentes, como Alexa da Amazon, Siri da Apple e Cortana da Microsoft.

* [Reconhecimento de voz com <b>Sphinx</b> (basico).](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/speech_recognition/recognition_sphinx_basic.py)
* [AudioFile com <b>Sphinx</b>.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/speech_recognition/recognition_sphinx_reading_file.py)
* [Live Speech (sem interrupção) usando <b>Sphinx</b>.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/speech_recognition/recognition_sphinx_live.py)
* [Reconhecimento de voz (em linguagem PT) - <b>Google</b>.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/speech_recognition/recognition_pt.py)
* [Speech Recognition - Usando <b>API Google</b>.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/speech_recognition/recognition_google_api_google.py)

#### Exemplos de uso...

* [Welcome script.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/projects/project_welcome.py)
* [Lendo um arquivo de texto.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/projects/project_reading_file.py)
* [Comando de voz binario (sim e não).](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/projects/project_voice_binary_comm.py)
* [Matemática utilizando comando de voz.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/projects/project_voice_multiplication_comm.py)
* [Sintetização + reconhecimento de voz.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/projects/project_synthesis_recognition.py)
* [Assistente de navegação multitarefas.](https://github.com/JoseMateusCamargo/python/blob/master/tss-text-to-speech/projects/project_multi_task.py)

## Fim
