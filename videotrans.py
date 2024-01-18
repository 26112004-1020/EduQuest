# %%
import whisper
from pytube import YouTube
import os
import tensorflow as tf

# %%
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    
    DEVICE = "cuda:0"
else:
    
    DEVICE = "cpu"

# %%
model = whisper.load_model("D:/ML procts/Hack IT SSN/large.pt", device=DEVICE)

# %%
#url = https://www.youtube.com/shorts/JM8WIbqn9sI?feature=share
url =  "https://www.youtube.com/shorts/JM8WIbqn9sI?feature=share"
video = YouTube(url)

# %%
selector = video.streams.filter(only_audio=True)
selector = selector.first()

# %%
selector.download(filename='ChessLecture.mp4')

# %%
in_language = input()

# %%
final = model.transcribe('ChessLecture.mp4')


# %%
print(final['text'])

# %%
limited = final['text'][0:487]

# %%
from translate import Translator

translator = Translator(to_lang=in_language)
text_to_translate = limited
translated_text = translator.translate(text_to_translate)
print(translated_text)


