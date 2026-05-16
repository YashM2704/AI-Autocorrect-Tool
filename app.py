from pathlib import Path
from preprocessing import preprocess_text
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from textblob_autocorrect import correct_spelling
text = input("Enter sentence: ")
corrected = correct_spelling(text)
processed = preprocess_text(text)
print("\nCorrected Text:")
print(corrected)
print("\nProcessed Text:")
print(processed)