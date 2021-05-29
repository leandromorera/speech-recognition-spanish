# speech-recognition-spanish

You can use the following dataset:
https://www.kaggle.com/bryanpark/spanish-single-speaker-speech-dataset

transcript.txt must be formated by the file (DB/converter.py)
In your dictionary must be represented symbols of your transcription (DB/nuevo.json) we advice to avoid Upercase leeters and accent also ñ.

# for train:
python train.py "training/graves" "custom_trining.json"

# for prediction
python predict.py "trainings/graves.json" "trainings/graves.weights-xx-xx.xxxx.h5" "media/audio.wav"
