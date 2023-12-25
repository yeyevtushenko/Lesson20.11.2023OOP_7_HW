class TextModifier:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        self.text = self.text.upper()

    def to_lowercase(self):
        self.text = self.text.lower()

    def remove_spaces(self):
        self.text = self.text.replace(" ", "")

    def encrypt_shift_left(self, shift_amount):
        encrypted_text = ""
        for char in self.text:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('а' if char.islower() else 'А') - shift_amount) % 26
                                   + ord('а' if char.islower() else 'А'))
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        self.text = encrypted_text

    def display_text(self):
        print(self.text)

# Отримання тексту від користувача
input_text = input("Введіть текст: ")
text_modifier = TextModifier(input_text)

print("\nОригінальний текст:")
text_modifier.display_text()

text_modifier.to_uppercase()
print("\nТекст у верхньому регістрі:")
text_modifier.display_text()

text_modifier.to_lowercase()
print("\nТекст у нижньому регістрі:")
text_modifier.display_text()

text_modifier.remove_spaces()
print("\nТекст без пробілів:")
text_modifier.display_text()

shift_amount = int(input("\nВведіть кількість позицій для шифрування: "))
text_modifier.encrypt_shift_left(shift_amount)
print(f"\nТекст зашифровано зі зсувом вліво на {shift_amount} позицій:")
text_modifier.display_text()
