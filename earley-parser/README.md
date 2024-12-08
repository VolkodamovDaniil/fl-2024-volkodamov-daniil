Для запуска самой задачи необходимо запустить `main.py` (например, посредством `python main.py`), после чего ввести входные данные в указанном формате. Если с форматом данных что-то не так, функция `validate_input` прервёт исполнение и выведет в консоль, что конкретно конкретно введено неправильно. Если же входные данные корректны, алгоритм решает поставленную задачу и выдаёт ответ в указанном формате.

Для запуска автоматизированных тестов необходимо запустить `tests.py` (например, посредством `python tests.py`). В случае корректного прохождения каждого теста выводится соответствующее сообщение, в случае некорректного — название теста и слова, в распознавании которых была допущена ошибка.