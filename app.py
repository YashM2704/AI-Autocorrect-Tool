from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from textblob_autocorrect import correct_spelling

text = input("Enter sentence: ")

corrected = correct_spelling(text)

print("\nCorrected Text:")
print(corrected)