from queue import Queue

q = Queue()


def generate_request(user):
    q.put(user)
    print(f"У кол центр надійшов дзвінок від {user}. Його номер в черці {q.qsize()}")


def process_request():
    if not q.empty():
        current_item = q.get()
        print(f"Користувач {current_item} покинув чергу і обсслуговується оператором кол центру.")
    else:
        print("Черга порожня")

def main():
    while True:
        print("\n--- КОЛ-ЦЕНТР ---")
        print("1. Додати дзвінок у чергу")
        print("2. Обслугувати дзвінок")
        print("3. Переглянути кількість дзвінків")
        print("4. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            user = input("Введіть ім'я користувача: ")
            generate_request(user)

        elif choice == "2":
            process_request()

        elif choice == "3":
            print(f"Кількість дзвінків у черзі: {q.qsize()}")

        elif choice == "4":
            print("Роботу кол-центру завершено.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
