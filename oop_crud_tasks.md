# Практические задачи / Practice Tasks / Вазифаҳои амалӣ

Языки / Languages / Забонҳо: 🇬🇧 English · 🇷🇺 Русский · 🇹🇯 Тоҷикӣ

> Названия классов, полей и методов даны в `snake_case`. В Java / C# / JS используйте свой стиль (`getById`, `GetById`).
> Class, field and method names are in `snake_case`. In Java / C# / JS use your own style (`getById`, `GetById`).
> Номҳои синф, майдон ва метод бо `snake_case` дода шудаанд. Дар Java / C# / JS услуби худро истифода баред.

---

# Task 1. CRUD: Book and Author (no relation)

## 🇬🇧 English

**Goal.** Learn the basic CRUD pattern: store objects and manage them with five standard methods.

**Entities (two independent classes):**

| Class | Fields |
|---|---|
| `Book` | `id` (int, auto), `title` (str), `year` (int), `price` (float) |
| `Author` | `id` (int, auto), `full_name` (str), `birth_year` (int), `country` (str) |

**No relation:** `Book` has no `author_id` / `author` field, and `Author` has no list of books.

**Repositories.** Create `BookRepository` and `AuthorRepository`. Each stores its objects in memory (`dict {id: object}`) and has a counter `next_id`. Both have the same five methods:

| Method | What it does | Returns |
|---|---|---|
| `create(data)` | Validates data, assigns a new `id`, saves the object | the created object |
| `update(id, data)` | Changes the fields of an existing object | the updated object, or error if `id` not found |
| `delete(id)` | Removes the object | `True` if deleted, `False` if not found |
| `get_by_id(id)` | Finds one object | the object, or `None` / "not found" error |
| `get_all()` | Gets everything | list of all objects (empty list if none) |

**Rules:**
- `title` and `full_name` must not be empty.
- `price` > 0; `year` between 1000 and the current year; `birth_year` less than the current year.
- An `id` is never reused after deletion.
- On invalid data or unknown `id` show a clear error message (or raise an exception).

**Demo in `main`:** create 3 books and 3 authors → print `get_all()` → update one book and one author → delete one of each → call `get_by_id` with a non-existing id and show the error → print `get_all()` again.

## 🇷🇺 Русский

**Цель.** Освоить базовый шаблон CRUD: хранить объекты и управлять ими пятью стандартными методами.

**Сущности (два независимых класса):**

| Класс | Поля |
|---|---|
| `Book` | `id` (int, авто), `title` (str), `year` (int), `price` (float) |
| `Author` | `id` (int, авто), `full_name` (str), `birth_year` (int), `country` (str) |

**Без связи:** у `Book` нет поля `author_id` / `author`, у `Author` нет списка книг.

**Репозитории.** Создайте `BookRepository` и `AuthorRepository`. Каждый хранит объекты в памяти (`dict {id: объект}`) и имеет счётчик `next_id`. У обоих одинаковые пять методов:

| Метод | Что делает | Возвращает |
|---|---|---|
| `create(data)` | Проверяет данные, назначает новый `id`, сохраняет объект | созданный объект |
| `update(id, data)` | Изменяет поля существующего объекта | обновлённый объект или ошибку, если `id` не найден |
| `delete(id)` | Удаляет объект | `True`, если удалён, `False`, если не найден |
| `get_by_id(id)` | Находит один объект | объект или `None` / ошибку «не найден» |
| `get_all()` | Получает все объекты | список всех объектов (пустой список, если их нет) |

**Правила:**
- `title` и `full_name` не должны быть пустыми.
- `price` > 0; `year` от 1000 до текущего года; `birth_year` меньше текущего года.
- `id` не переиспользуется после удаления.
- При неверных данных или неизвестном `id` выводите понятное сообщение об ошибке (или бросайте исключение).

**Демонстрация в `main`:** создать 3 книги и 3 автора → вывести `get_all()` → изменить одну книгу и одного автора → удалить по одному → вызвать `get_by_id` с несуществующим id и показать ошибку → снова вывести `get_all()`.

## 🇹🇯 Тоҷикӣ

**Мақсад.** Омӯхтани шаблони асосии CRUD: нигоҳ доштани объектҳо ва идора кардани онҳо бо панҷ методи стандартӣ.

**Entity-ҳо (ду синфи мустақил):**

| Синф | Майдонҳо |
|---|---|
| `Book` | `id` (int, худкор), `title` (str), `year` (int), `price` (float) |
| `Author` | `id` (int, худкор), `full_name` (str), `birth_year` (int), `country` (str) |

**Бе алоқа:** `Book` майдони `author_id` / `author` надорад ва `Author` рӯйхати китобҳо надорад.

**Repository-ҳо.** `BookRepository` ва `AuthorRepository` эҷод кунед. Ҳар кадом объектҳоро дар хотира (`dict {id: объект}`) нигоҳ медорад ва ҳисобкунаки `next_id` дорад. Ҳардуяшон панҷ методи якхела доранд:

| Метод | Чӣ мекунад | Чӣ бармегардонад |
|---|---|---|
| `create(data)` | Маълумотро месанҷад, `id`-и нав медиҳад, объектро нигоҳ медорад | объекти эҷодшуда |
| `update(id, data)` | Майдонҳои объекти мавҷударо тағйир медиҳад | объекти навшуда ё хатогӣ, агар `id` ёфт нашавад |
| `delete(id)` | Объектро несту нобуд мекунад | `True`, агар нест шуд, `False`, агар ёфт нашуд |
| `get_by_id(id)` | Як объектро меёбад | объект ё `None` / хатогии «ёфт нашуд» |
| `get_all()` | Ҳамаи объектҳоро мегирад | рӯйхати ҳамаи объектҳо (рӯйхати холӣ, агар набошанд) |

**Қоидаҳо:**
- `title` ва `full_name` набояд холӣ бошанд.
- `price` > 0; `year` аз 1000 то соли ҷорӣ; `birth_year` аз соли ҷорӣ хурдтар.
- `id` пас аз нест кардан дубора истифода намешавад.
- Ҳангоми маълумоти нодуруст ё `id`-и номаълум паёми равшани хатогӣ нишон диҳед (ё exception андозед).

**Намоиш дар `main`:** 3 китоб ва 3 муаллиф эҷод кунед → `get_all()`-ро чоп кунед → як китоб ва як муаллифро навсозӣ кунед → аз ҳар кадом якторо нест кунед → `get_by_id`-ро бо id-и мавҷуднабуда даъват карда, хатогиро нишон диҳед → бори дигар `get_all()`-ро чоп кунед.

---

# Task 2. Inheritance

## 🇬🇧 English

**Goal.** Understand how a child class reuses the fields and methods of a parent class and extends them.

**Classes:**

| Class | Inherits from | Own fields | `get_info()` returns |
|---|---|---|---|
| `Publication` | — | `title`, `year` | `"<title> (<year>)"` |
| `Book` | `Publication` | `pages` | `"Book: <title> (<year>), <pages> pages"` |
| `Magazine` | `Publication` | `issue_number` | `"Magazine: <title> (<year>), issue #<issue_number>"` |

**Rules:**
- `Book` and `Magazine` must **not** assign `title` and `year` themselves. Call the parent constructor (`super()` / `base()`).
- `get_info()` is overridden in the children. It may call the parent's `get_info()` to avoid duplicating code.

**Demo:** create `Book("Clean Code", 2008, 464)` and `Magazine("Forbes", 2024, 7)`, print `get_info()` of both. Also check that a `Book` object is an instance of `Publication` (`isinstance` / `instanceof`).

**Expected output:**
```
Book: Clean Code (2008), 464 pages
Magazine: Forbes (2024), issue #7
```

## 🇷🇺 Русский

**Цель.** Понять, как дочерний класс переиспользует поля и методы родителя и расширяет их.

**Классы:**

| Класс | Наследуется от | Свои поля | `get_info()` возвращает |
|---|---|---|---|
| `Publication` | — | `title`, `year` | `"<title> (<year>)"` |
| `Book` | `Publication` | `pages` | `"Book: <title> (<year>), <pages> pages"` |
| `Magazine` | `Publication` | `issue_number` | `"Magazine: <title> (<year>), issue #<issue_number>"` |

**Правила:**
- `Book` и `Magazine` **не** должны сами присваивать `title` и `year`. Вызовите конструктор родителя (`super()` / `base()`).
- `get_info()` переопределяется в дочерних классах. Можно вызвать `get_info()` родителя, чтобы не дублировать код.

**Демонстрация:** создайте `Book("Clean Code", 2008, 464)` и `Magazine("Forbes", 2024, 7)`, выведите `get_info()` обоих. Также проверьте, что объект `Book` является экземпляром `Publication` (`isinstance` / `instanceof`).

**Ожидаемый вывод:**
```
Book: Clean Code (2008), 464 pages
Magazine: Forbes (2024), issue #7
```

## 🇹🇯 Тоҷикӣ

**Мақсад.** Фаҳмидани он, ки синфи фарзанд майдонҳо ва методҳои волидро чӣ гуна истифода мебарад ва васеъ мекунад.

**Синфҳо:**

| Синф | Аз кӣ мерос мегирад | Майдонҳои худӣ | `get_info()` чӣ бармегардонад |
|---|---|---|---|
| `Publication` | — | `title`, `year` | `"<title> (<year>)"` |
| `Book` | `Publication` | `pages` | `"Book: <title> (<year>), <pages> pages"` |
| `Magazine` | `Publication` | `issue_number` | `"Magazine: <title> (<year>), issue #<issue_number>"` |

**Қоидаҳо:**
- `Book` ва `Magazine` набояд `title` ва `year`-ро худашон таъин кунанд. Конструктори волидро даъват кунед (`super()` / `base()`).
- `get_info()` дар синфҳои фарзанд override карда мешавад. Барои такрор накардани код `get_info()`-и волидро даъват кардан мумкин аст.

**Намоиш:** `Book("Clean Code", 2008, 464)` ва `Magazine("Forbes", 2024, 7)` эҷод кунед, `get_info()`-и ҳардуро чоп кунед. Инчунин санҷед, ки объекти `Book` намунаи `Publication` аст (`isinstance` / `instanceof`).

**Натиҷаи интизорӣ:**
```
Book: Clean Code (2008), 464 pages
Magazine: Forbes (2024), issue #7
```

---

# Task 3. Encapsulation

## 🇬🇧 English

**Goal.** Hide the internal state of an object and allow changes only through methods that enforce rules.

**Class `BankAccount`:**

| Member | Access | Description |
|---|---|---|
| `owner` | private | account owner's name |
| `balance` | private | current balance |
| `__init__(owner, initial_balance=0)` | public | `initial_balance` must be >= 0 |
| `deposit(amount)` | public | adds money; `amount` must be > 0 |
| `withdraw(amount)` | public | subtracts money; `amount` must be > 0 and <= `balance` |
| `get_balance()` | public | returns the balance |
| `get_owner()` | public | returns the owner |

**Rules:**
- No setter for `balance`. It changes only through `deposit` and `withdraw`.
- On a rule violation, show an error message or raise an exception, and **leave the balance unchanged**.

**Demo:** create an account with 100 → `deposit(50)` → balance 150 → `withdraw(200)` → error, balance still 150 → `withdraw(30)` → balance 120. Then try `account.balance = 1000000` from outside and explain in a comment why it does not work (or is not allowed).

## 🇷🇺 Русский

**Цель.** Скрыть внутреннее состояние объекта и разрешить менять его только через методы, которые проверяют правила.

**Класс `BankAccount`:**

| Член класса | Доступ | Описание |
|---|---|---|
| `owner` | private | имя владельца счёта |
| `balance` | private | текущий баланс |
| `__init__(owner, initial_balance=0)` | public | `initial_balance` должен быть >= 0 |
| `deposit(amount)` | public | добавляет деньги; `amount` > 0 |
| `withdraw(amount)` | public | снимает деньги; `amount` > 0 и <= `balance` |
| `get_balance()` | public | возвращает баланс |
| `get_owner()` | public | возвращает владельца |

**Правила:**
- Сеттера для `balance` нет. Баланс меняется только через `deposit` и `withdraw`.
- При нарушении правил выведите сообщение об ошибке или бросьте исключение, **баланс при этом не меняется**.

**Демонстрация:** создайте счёт со 100 → `deposit(50)` → баланс 150 → `withdraw(200)` → ошибка, баланс всё ещё 150 → `withdraw(30)` → баланс 120. Затем попробуйте `account.balance = 1000000` снаружи и объясните в комментарии, почему это не работает (или не разрешено).

## 🇹🇯 Тоҷикӣ

**Мақсад.** Пинҳон кардани ҳолати дохилии объект ва иҷозат додани тағйирот танҳо тавассути методҳое, ки қоидаҳоро месанҷанд.

**Синфи `BankAccount`:**

| Узви синф | Дастрасӣ | Тавсиф |
|---|---|---|
| `owner` | private | номи соҳиби ҳисоб |
| `balance` | private | баланси ҷорӣ |
| `__init__(owner, initial_balance=0)` | public | `initial_balance` бояд >= 0 бошад |
| `deposit(amount)` | public | пул илова мекунад; `amount` > 0 |
| `withdraw(amount)` | public | пул мегирад; `amount` > 0 ва <= `balance` |
| `get_balance()` | public | балансро бармегардонад |
| `get_owner()` | public | соҳибро бармегардонад |

**Қоидаҳо:**
- Барои `balance` setter нест. Баланс танҳо тавассути `deposit` ва `withdraw` тағйир меёбад.
- Ҳангоми вайрон шудани қоида паёми хатогӣ нишон диҳед ё exception андозед, **баланс бетағйир мемонад**.

**Намоиш:** ҳисобро бо 100 эҷод кунед → `deposit(50)` → баланс 150 → `withdraw(200)` → хатогӣ, баланс ҳанӯз 150 → `withdraw(30)` → баланс 120. Баъд `account.balance = 1000000`-ро аз берун санҷед ва дар comment шарҳ диҳед, ки чаро кор намекунад (ё иҷозат нест).

---

# Task 4. Polymorphism

## 🇬🇧 English

**Goal.** Call the same method on different objects and get different behavior, without checking the object's type.

**Classes:**

| Class | Fields | `area()` formula |
|---|---|---|
| `Shape` (base) | `name` | returns 0 (to be overridden) |
| `Circle` | `radius` | π × radius² |
| `Rectangle` | `width`, `height` | width × height |
| `Triangle` | `base`, `height` | 0.5 × base × height |

Each class also overrides `describe()`, which returns `"<name>: area = <area rounded to 2 decimals>"`.

**Rules:**
- Put all shapes in **one** list of type `Shape`.
- Loop through the list and call `describe()` / `area()`. **Do not** use `if` / `instanceof` / `type()` to choose the formula.
- Write a function `total_area(shapes)` that sums the areas.

**Demo:** `Circle(3)`, `Rectangle(4, 5)`, `Triangle(6, 2)`.

**Expected output:**
```
Circle: area = 28.27
Rectangle: area = 20.00
Triangle: area = 6.00
Total area = 54.27
```

**Bonus:** add a `Square` class **without changing** the loop or `total_area`.

## 🇷🇺 Русский

**Цель.** Вызывать один и тот же метод у разных объектов и получать разное поведение, не проверяя тип объекта.

**Классы:**

| Класс | Поля | Формула `area()` |
|---|---|---|
| `Shape` (базовый) | `name` | возвращает 0 (будет переопределён) |
| `Circle` | `radius` | π × radius² |
| `Rectangle` | `width`, `height` | width × height |
| `Triangle` | `base`, `height` | 0.5 × base × height |

Каждый класс также переопределяет `describe()`, который возвращает `"<name>: area = <площадь, округлённая до 2 знаков>"`.

**Правила:**
- Поместите все фигуры в **один** список типа `Shape`.
- Пройдите по списку и вызовите `describe()` / `area()`. **Нельзя** использовать `if` / `instanceof` / `type()` для выбора формулы.
- Напишите функцию `total_area(shapes)`, которая суммирует площади.

**Демонстрация:** `Circle(3)`, `Rectangle(4, 5)`, `Triangle(6, 2)`.

**Ожидаемый вывод:**
```
Circle: area = 28.27
Rectangle: area = 20.00
Triangle: area = 6.00
Total area = 54.27
```

**Бонус:** добавьте класс `Square` **без изменения** цикла и `total_area`.

## 🇹🇯 Тоҷикӣ

**Мақсад.** Як методро барои объектҳои гуногун даъват кардан ва рафтори гуногун гирифтан, бе санҷиши навъи объект.

**Синфҳо:**

| Синф | Майдонҳо | Формулаи `area()` |
|---|---|---|
| `Shape` (асосӣ) | `name` | 0 бармегардонад (override карда мешавад) |
| `Circle` | `radius` | π × radius² |
| `Rectangle` | `width`, `height` | width × height |
| `Triangle` | `base`, `height` | 0.5 × base × height |

Ҳар як синф инчунин `describe()`-ро override мекунад, ки `"<name>: area = <масоҳат бо 2 рақами баъди вергул>"` бармегардонад.

**Қоидаҳо:**
- Ҳамаи шаклҳоро дар **як** рӯйхати навъи `Shape` гузоред.
- Рӯйхатро бо давр гузаред ва `describe()` / `area()`-ро даъват кунед. Барои интихоби формула `if` / `instanceof` / `type()` истифода **набаред**.
- Функсияи `total_area(shapes)` нависед, ки масоҳатҳоро ҷамъ мекунад.

**Намоиш:** `Circle(3)`, `Rectangle(4, 5)`, `Triangle(6, 2)`.

**Натиҷаи интизорӣ:**
```
Circle: area = 28.27
Rectangle: area = 20.00
Triangle: area = 6.00
Total area = 54.27
```

**Бонус:** синфи `Square`-ро **бе тағйир додани** давр ва `total_area` илова кунед.

---

# Task 5. Abstraction (+ review of all principles)

## 🇬🇧 English

**Goal.** Define *what* objects must do in an abstract class, and leave *how* to the child classes. Then combine all four OOP principles.

**Classes:**

| Class | Type | Members |
|---|---|---|
| `Employee` | **abstract** | `name`; abstract method `calculate_salary()`; regular method `show_info()` that prints `"<name>: salary = <calculate_salary()>"` |
| `FullTimeEmployee` | concrete | `monthly_salary`; `calculate_salary()` returns `monthly_salary` |
| `PartTimeEmployee` | concrete | `hourly_rate`, `hours_worked`; `calculate_salary()` returns `hourly_rate × hours_worked` |

**Rules:**
- `Employee` cannot be instantiated. Show what happens when you try (error), in a comment or in the demo.
- `show_info()` is written **once** in `Employee` and works for both children.
- Write `total_payroll(employees)` that sums the salaries of a list of employees.
- Fields are private with getters (encapsulation).
- In comments, mark one place for each principle: **abstraction**, **inheritance**, **polymorphism**, **encapsulation**.

**Demo:** `FullTimeEmployee("Anna", 3000)`, `PartTimeEmployee("Bob", 20, 80)`.

**Expected output:**
```
Anna: salary = 3000
Bob: salary = 1600
Total payroll = 4600
```

## 🇷🇺 Русский

**Цель.** Описать в абстрактном классе, *что* должны уметь объекты, а *как* — оставить дочерним классам. Затем объединить все четыре принципа ООП.

**Классы:**

| Класс | Тип | Члены |
|---|---|---|
| `Employee` | **абстрактный** | `name`; абстрактный метод `calculate_salary()`; обычный метод `show_info()`, который печатает `"<name>: salary = <calculate_salary()>"` |
| `FullTimeEmployee` | конкретный | `monthly_salary`; `calculate_salary()` возвращает `monthly_salary` |
| `PartTimeEmployee` | конкретный | `hourly_rate`, `hours_worked`; `calculate_salary()` возвращает `hourly_rate × hours_worked` |

**Правила:**
- `Employee` нельзя создать. Покажите, что происходит при попытке (ошибка), в комментарии или в демонстрации.
- `show_info()` написан **один раз** в `Employee` и работает для обоих наследников.
- Напишите `total_payroll(employees)`, которая суммирует зарплаты списка сотрудников.
- Поля приватные, с геттерами (инкапсуляция).
- В комментариях отметьте по одному месту для каждого принципа: **абстракция**, **наследование**, **полиморфизм**, **инкапсуляция**.

**Демонстрация:** `FullTimeEmployee("Anna", 3000)`, `PartTimeEmployee("Bob", 20, 80)`.

**Ожидаемый вывод:**
```
Anna: salary = 3000
Bob: salary = 1600
Total payroll = 4600
```

## 🇹🇯 Тоҷикӣ

**Мақсад.** Дар синфи абстрактӣ тавсиф кардан, ки объектҳо *чӣ* кор карда метавонанд, ва *чӣ тавр* кор карданро ба синфҳои фарзанд вогузоштан. Баъд ҳар чор принсипи OOP-ро муттаҳид кардан.

**Синфҳо:**

| Синф | Навъ | Узвҳо |
|---|---|---|
| `Employee` | **абстрактӣ** | `name`; методи абстрактии `calculate_salary()`; методи оддии `show_info()`, ки `"<name>: salary = <calculate_salary()>"` чоп мекунад |
| `FullTimeEmployee` | мушаххас | `monthly_salary`; `calculate_salary()` `monthly_salary`-ро бармегардонад |
| `PartTimeEmployee` | мушаххас | `hourly_rate`, `hours_worked`; `calculate_salary()` `hourly_rate × hours_worked`-ро бармегардонад |

**Қоидаҳо:**
- `Employee`-ро эҷод кардан мумкин нест. Дар comment ё дар намоиш нишон диҳед, ки ҳангоми кӯшиш чӣ мешавад (хатогӣ).
- `show_info()` **як маротиба** дар `Employee` навишта мешавад ва барои ҳардуи меросгирандагон кор мекунад.
- `total_payroll(employees)`-ро нависед, ки маошҳои рӯйхати коргаронро ҷамъ мекунад.
- Майдонҳо private бо getter мебошанд (инкапсулятсия).
- Дар comment-ҳо барои ҳар як принсип як ҷоро қайд кунед: **абстраксия**, **мерос**, **полиморфизм**, **инкапсулятсия**.

**Намоиш:** `FullTimeEmployee("Anna", 3000)`, `PartTimeEmployee("Bob", 20, 80)`.

**Натиҷаи интизорӣ:**
```
Anna: salary = 3000
Bob: salary = 1600
Total payroll = 4600
```
