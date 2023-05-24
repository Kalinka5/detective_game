# DETECTIVE_GAME
![Pypi](https://img.shields.io/pypi/v/detective?color=orange)
![Python](https://img.shields.io/pypi/pyversions/detective?color=blueviolet)
![Forks](https://img.shields.io/github/forks/Kalinka5/detective_game?style=social)

This **detective game** is about an incredibly interesting murder and how detective Dan Kalini uncovers it all.

**In this game** you will finally feel like a detective. All you need is logical thinking, good attention and a little bit of luck to complete this game.
___

## *Files_location*
<details>
<summary>Open</summary>

+ :file_folder: archives
  + detective_game_rar
  + detective_game_zip
  + python_files_rar
  + python_files_zip
+ :file_folder: programme
  + :file_folder: audio
  + :file_folder: audio_ukr
  + :file_folder: characters
  + game
  + hard_mini_games
  + health_exception
  + main
  + questions
  + story
+ text_of_audiofiles
+ text_of_audiofiles_ua
</details>

___

## *Usage*
To begin with you have two option to open this game. 
- First you can open executable file in **detective_game** [archives](https://github.com/Kalinka5/detective_game/tree/main/archives);
- Second you can open any IDE and run *"main"* program in **python_files** [arhives](https://github.com/Kalinka5/detective_game/tree/main/archives).
___

## *Example*
When you open the programme you will choose the language you are comfortable with (*ukrainian* or *english*). Also you can choose play game with audio :sound: or without it :mute:. 

![example1](https://user-images.githubusercontent.com/106172806/215560978-70ff98a8-e36e-479b-8bed-b6e921a82850.jpg)

The game also features a choice of actions. Where the character goes or what phrase he says :thinking:.

![example2](https://user-images.githubusercontent.com/106172806/215561010-d57ef97c-c97f-44d1-9e88-152cb20113ec.jpg)

There are easy and hard levels. If you chose hard difficalty level you will play short games. Also in this level you will have lives :hearts: and if you lose everything, you will automatically lose :dizzy_face:.

![example3](https://user-images.githubusercontent.com/106172806/215561028-2ec3b8c8-7ce1-4992-a733-dfceccf2856b.jpg)

___

## *Mini_games*
*In detective game you have 3 mini games.:video_game:*
- "Guess the number" :8ball:
- "Dice rolling" :game_die:
- "Rock, paper, scissors" :rock: :page_with_curl: :scissors:

<details>
<summary>Guess the number :8ball:</summary>

It's first game where you should guess the number which computer was guessed.
Here’s what it looks like:
  
![game1](https://user-images.githubusercontent.com/106172806/215561082-c87e3ec3-0d8c-48a7-b5e4-67e7b92e2ad2.JPG)
</details>

___

<details>
<summary>Dice rolling :game_die:</summary>

This is second game, where you must roll the dice and sum of the digits must be greater than or equal to 8. Here’s what it looks like:

![game2](https://user-images.githubusercontent.com/106172806/215561130-a0879b40-74c9-41b8-a36a-567694933a07.JPG)
</details>

___

<details>
<summary>Rock :rock:, paper :page_with_curl:, scissors :scissors:</summary>

And there is last game where you should play famous child game "Rock, paper, scissors". I hope you know rules of this game. Here’s what it looks like:

![game3](https://user-images.githubusercontent.com/106172806/215561164-c381981f-92cf-4662-a555-e7bd8ec7ee29.JPG)
![game3_1](https://user-images.githubusercontent.com/106172806/215561177-9ead4165-7bc2-4a93-a47c-816938cd1c74.JPG)
</details>

___

## *PyTorch*
<details>
<summary>Open</summary>

And the trump card in my program is the voices of [Silero models](https://github.com/snakers4/silero-models).

With this module you can set more than 100 votes to the character. 

First of all, import [torch](https://github.com/pytorch/pytorch) and [soundfile](https://pypi.org/project/SoundFile/) in our programm.
```python
import torch
import soundfile as sf
```

Then make configuration of character:
```python
language = 'en'
model_id = 'v3_en'
sample_rate = 48000
speaker = 'en_70'  # en_0, en_1, ..., en_117, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu or gpu


model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)

model.to(device)
```
In conclusion, we convert text to speach and save it in _wav_ format.
```python
def author_speak(what: str, n):
    audio = model.apply_tts(ssml_text=what,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sf.write(f'vvauthor_say{n}.wav', audio, sample_rate)
```
</details>

___

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
</picture>
