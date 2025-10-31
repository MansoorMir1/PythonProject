# Step 1: Import required library
from spellchecker import SpellChecker
import re  # For cleaning punctuation

# Step 2: Create the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def clean_text(self, text):
        """
        Removes unnecessary punctuation but keeps words and numbers separate.
        Example: "hello, world!" -> "hello world"
        """
        return re.sub(r'[^\w\s]', '', text)

    def correct_text(self, text):
        """
        Corrects spelling errors in the given text,
        skipping numbers or symbols.
        """
        # Clean text and split into words
        cleaned_text = self.clean_text(text)
        words = cleaned_text.split()
        corrected_words = []

        for word in words:
            # Skip numbers or symbols
            if not word.isalpha():
                corrected_words.append(word)
                continue

            # Get corrected version
            correct_word = self.spell.correction(word)

            # Only print correction if the word actually changed
            if correct_word != word:
                print(f'✏️ Correcting "{word}" → "{correct_word}"')

            corrected_words.append(correct_word)

        # Step 3: Return corrected sentence
        return ' '.join(corrected_words)

    # Step 4: Run the app
    def run(self):
        print("\n🔍 ---- Spell Checker ----")

        while True:
            text = input('\nEnter text to check (or type "exit" to quit"): ').strip()
            if text.lower() == 'exit':
                print('👋 Closing the program... Goodbye!')
                break
            elif not text:
                print("⚠️ Please enter some text!")
                continue

            corrected_text = self.correct_text(text)
            print(f'\n✅ Corrected text: {corrected_text}')

# Step 5: Run the main program
if __name__ == '__main__':
    app = SpellCheckerApp()
    app.run()
