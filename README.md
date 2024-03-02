Моя программа заметок на Python, использующая встроенный json модуль для создания, сохранения, чтения, редактирования
и удаления заметок с помощью консольного ввода. Заметки будут храниться в файле с именем notes.json.

Эта программа определяет функции для создания, сохранения, чтения, редактирования и удаления заметок.
Заметки хранятся в списке с именем notesи сохраняются в файл JSON с именем notes.json.
Функция read_notes читает файл JSON и загружает заметки в notes список.
Функции create_note, edit_note и delete_note изменяют notes список и вызывают save_notes сохранение изменений в файле JSON.

Вот пример того, как вы можете использовать эту программу:

Запустите программу.
Выберите опцию из меню:
Вариант 1. Создайте новую заметку, указав заголовок и содержание.
Вариант 2: Прочитайте список примечаний.
Вариант 3. Отредактируйте существующую заметку, введя индекс заметки, новый заголовок и содержание.
Вариант 4. Удалите существующую заметку, введя индекс заметки.
Вариант 5: Выйти из программы.


upd:
новый код добавляет filter_notes_by_date() функцию, которая фильтрует заметки на основе заданных дат начала и окончания.
Теперь функция read_notes() принимает параметры даты начала и окончания и вызывает функцию filter_notes_by_date().
В основном цикле пользователю запрашивается дата начала и окончания, и функция read_notes() вызывается с этими параметрами,
если они предусмотрены.