def sort_words(words):

    words_lower = [word.lower() for word in words]
    sorted_words = sorted(words_lower, key=lambda x: (x[0].isupper(), x.lower()))
    return sorted_words

def main():

    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            text = file.read()
        first_sentence = text.split(".")[0]  # отримати перше речення
        print("Перше речення:", first_sentence)
        words = first_sentence.replace(",", "").replace(".", "").split()  # очистити слова від знаків пунктуації
        sorted_words = sort_words(words)  # відсортувати слова
        print("Відсортовані слова:", sorted_words)
        print("Кількість слів:", len(sorted_words))
    except FileNotFoundError:
        print("Файл input.txt не знайдено.")

if __name__ == "__main__":
    main()