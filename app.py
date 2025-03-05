from flask import Flask, render_template, request #Импорт фреймворка веб-приложений
app = Flask(__name__) #Объект который управляет сайтом
questions = [
    {"text": "Проводишь ли ты больше 3 часов в день в соцсетях?", "weight": 2},
    {"text": "Чувствуешь ли тревогу, когда нет доступа к телефону?", "weight": 3},
    {"text": "Используешь ли гаджеты перед сном?", "weight": 1}
] #список вопросов(2 ключа(text - вопрос, weight - ценность вопроса
@app.route("/", methods=["GET", "POST"]) #Отвечает за главную страницу,GET - открыть страницу, POST - отправить ответы
def index(): #Обработка главной страницы
    if request.method == "POST": # проверка отправились ли ответы
        score = 0
        for i in range(len(questions)):
            answer = request.form.get(f"q{i}") #получение ответа на вопрос от польз
            if answer == "yes":
                score += questions[i]["weight"]
        if score <= 2:
            result_text = "У тебя всё под контролем!" # нет зависимости
        elif score <= 5:
            result_text = "Стоит уменьшить время в телефоне." #Небольшая зависимость
        else:
            result_text = "Опасный уровень зависимости! Попробуй цифровой детокс." #Сильная зависимость
        return render_template("result.html", result=result_text) #Вывод результата пользователю
    return render_template("index.html", questions=questions)
if __name__ == "__main__": #Код работает только если запустить файл напрямую
    app.run(host="0.0.0.0", port=5000) #Вывод ошибок если будут
