from TTS.tts.utils.text.phonemizers.gu_in_phonemizer import GU_IN_Phonemizer

# Create an instance of your phonemizer
phonemizer = GU_IN_Phonemizer()

# Test input: a sample Gujarati sentence (modify as needed)
sample_text = "ગુજરાતી ભાષા"
output = phonemizer.phonemize(sample_text)

print("Input Text:", sample_text)
print("Phonemized Output:", output)
