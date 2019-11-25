## Flask ORM
Перед запуском вам треба налаштувати config.py, що знаходиться в корні 
додатка, для коректної 
роботи з вашою базою даних. Після цього загрузіть 
Insomnia.json в Insomnia чи Postman для початку роботи.
### Всі команди виконувати в Insomnia чи Postman
#### 1 Наповнюємо вашу базу таблицями
* Do POST http://127.0.0.1:5000/create_db
#### 2 Заповнюємо ваші таблиці даними
* Do POST http://127.0.0.1:5000/tenants
```
[
  	{"name": "Frodo", "age": 51, "sex": "male"},
	{"name": "Sam", "age": 36, "sex": "male"},
	{"name": "Merry", "age": 26, "sex": "male"},
	{"name": "Pippin", "age": 25, "sex": "male"}
]
```
* Do POST http://127.0.0.1:5000/address
```
[
  	{"city": "Mordor", "street": "Sauron 21", "tenant_id": 1},
	{"city": "Mordor", "street": "Sauron 22", "tenant_id": 2},
	{"city": "Fangorn", "street": "entova 23", "tenant_id": 3},
	{"city": "Fangorn", "street": "entova 24", "tenant_id": 4}
]
```
* Do POST http://127.0.0.1:5000/staff
```
[
	{"name": "Sauron", "position": "administrator", "salary": 100},
	{"name": "Saruman", "position": "manager", "salary": 90}
]
```
* Do POST http://127.0.0.1:5000/rooms
```
[
  {
    "level": "first",
    "status": "open",
    "price": 101,
		"tenant_id": 1
  },
	{
    "level": "first",
    "status": "closed",
    "price": 102,
		"tenant_id": 2
  },
	{
    "level": "second",
    "status": "open",
    "price": 103,
		"tenant_id": 3
  },
	{
    "level": "second",
    "status": "closed",
    "price": 104,
		"tenant_id": 4
  }
]
```
* Do POST http://127.0.0.1:5000/staff_and_room
```
[
	{"staff_id": 1, "room_id": 1},
	{"staff_id": 1, "room_id": 2},
	{"staff_id": 2, "room_id": 3},
	{"staff_id": 2, "room_id": 4}
]
```
### Використання 
Після запуску Insomnia.json вам буде доступно різні види запитів. 
Для більш широкого використання, ознайомтеся з кодом додатку.
