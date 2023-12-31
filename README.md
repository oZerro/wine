# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка
Python 3 уже должен быть установлен
    
1. Клонируйте репозиторий с github - для этого выполните в консоли:  
```
git clone https://github.com/oZerro/wine.git
```

2. Создайте виртуальное окружение.  
Для создания виртуального окружения:  
- Перейдите в директорию своего проекта.  
```
cd wine
``` 
- Выполните:  
```
python -m venv venv
```

3. Активируйте виртуальное окружение.  
Для активации виртуального окружения выполните:  
- для Windows  
 ```
venv\Scripts\activate.bat
```   
- для Linux и MacOS
```
source venv/bin/activate
``` 
4. Установите зависимости:  
```
pip install -r requirements.txt
```  

5. Создайте файл **.env** в вашей деректории проекта.  
- для Windows
```
type nul > .env
```
- для Linux и MacOS
```
touch файл.txt
``` 

6. Откройте файл **.env** в любом текстовом редакторе и добавьте ваш путь до файла xlsx где собрана вся информация о винах - сохраните.  
Строка будет выглядеть так:  
`PATH_TO_FILE='тут ваш путь до xlsx файла'`


## Как запустить
Для запуска - из директории проекта выполните команду в консоли:  
```
python main.py
```    

Так же вы можете передать в аргументе собственный путь до файла:  
```
python main.py --path qwerty.xlsx
```  
Код выше будет брать информацию из файла **(qwerty.xlsx)**  

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
