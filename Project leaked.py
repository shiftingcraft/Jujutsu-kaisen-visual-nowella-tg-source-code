# bot.send_message(message.from_user.id, "Концовка ??? Секретная - Ты грязный хакер иди играй а не смотри код игры")
from telebot import *
token = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
bot = TeleBot(token)
@bot.message_handler(commands=["f19"])
def nowellagoodend(message):
    bot.send_photo(message.from_user.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsuH2ILJomVDIxTyQNRXMvzFfWPRBuBXfCnYCWM0zD7g&s")
    bot.send_message(message.from_user.id, "А ты хорош.")
    bot.send_photo(message.from_user.id, "https://cdn.epicstream.com/images/ncavvykf/epicstream/279d2e9814b164c738592e9b3b8ab6c5dd687edd-2400x1440.jpg?rect=0,90,2400,1260&w=1200&h=630&auto=format")
    bot.send_message(message.from_user.id, "Молодец! Теперь ты оффициально маг 1 уровня!")
    bot.send_photo(message.from_user.id, "https://i.pinimg.com/originals/ab/a5/5e/aba55e8114c8b6f104d434673544d0af.jpg")
    bot.send_message(message.from_user.id, "Ты сейчас серьезно?! Это же недопустимо! Он должен стать магом 3 уровня!")
    bot.send_photo(message.from_user.id, "https://www.mundodeportivo.com/alfabeta/hero/2023/05/satoru-gojo-jujutsu-kaisen.jpg?width=768&aspect_ratio=16:9&format=nowebp")
    bot.send_message(message.from_user.id, "А мне пофик")
    bot.send_message(message.from_user.id, "Концовка 3/3 хорошая. Ты попал в магический колледж и стал магом 1 уровня")

@bot.message_handler(commands=["f12"])
def nowellafight5(message):
    bot.send_message(message.from_user.id, "Что ты выберешь /f14 - бить правой рукой /f15 - бить левой рукой /f16 - бить левой ногой /f17 - бить правой ногой /f18 - бить правой рукой по голове /f19 - бить левой рукой по голове /f20 - бить левой ногой по голове /f21 - бить правой ногой по голове")
@bot.message_handler(commands=["f8"])
def nowellafight4(message):
    bot.send_message(message.from_user.id, "Что ты выберешь /f10 - бить правой рукой /f11 - бить левой рукой /f12 - бить левой ногой /f13 - бить правой ногой")
@bot.message_handler(commands=["f10", "f11", "f13", "/f14", "f15", "f16", "f17", "f18", "f20", "f21"])
def nowellaneutralend2(message):
    bot.send_message(message.from_user.id, "Концовка 2.5/3 Нейтральная - Тебе помогла Кугисаки но тебя все равно приняли в магический колледж и сделали магом 2 уровня. /newgame для новой игры")
@bot.message_handler(commands=["f7"])
def nowellafight3(message):
    bot.send_message(message.from_user.id, "Что ты выберешь /f8 - бить правой ногой /f9 - бить левой ногой")
@bot.message_handler(commands=["f4"])
def nowellafight2(message):
    bot.send_message(message.from_user.id, "Что ты выберешь /f5 - бить правой рукой /f6 - бить левой рукой /f7 - апперкод")
@bot.message_handler(commands=["f1"])
def nowellafight1(message):
    bot.send_message(message.from_user.id, "Что ты выберешь /f3 - бить правой рукой /f4 - бить левой рукой")
@bot.message_handler(commands=["f2", "f3", "f5", "f6", "f9"])
def nowellaneutralend(message):
    bot.send_message(message.from_user.id, "Концовка 2/3 Нейтральная - Тебе помогла Кугисаки но тебя все равно приняли в магический колледж и сделали магом 3 уровня так как ты не показал свои возможности. /newgame для новой игры")

@bot.message_handler(commands=["q6"])
def nowellafight(message):
    bot.send_message(message.from_user.id, "Автор: Чтобы выйти на хорошую концовку тебе нужно выбрать правильную комбинацию.")
    bot.send_message(message.from_user.id, "Что ты выберишь /f1 - бить правой рукой /f2 - бить левой рукой")
def nowella3(message):
    bot.send_photo(message.from_user.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFeboUN09SfdiIHucqgtqJLXHM7UzyhNUTZg&s")
    bot.send_message(message.from_user.id, "Uzou muzou hito no nari Kyosei shinshou jingai aa mononoke mitai da. Kyoshin tankai inochi yadoshi Ato wa pappara pa na nakami naki ningen.")
    bot.send_photo(message.from_user.id, "https://i.pinimg.com/originals/57/88/a5/5788a5963d1009e21a9c32acdd7d6214.jpg")
    bot.send_message(message.from_user.id, "Про себя - Yoseru kitai fubyoudou na jinsei Sainou mo nai daijou hi nichijou ga. Onshin byoudou ni botsu kosei Tadoru kioku boku ni ibasho nado nai kara.")
    bot.send_message(message.from_user.id, "Я очень долго шел. Я немного устал.")
    bot.send_photo(message.from_user.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUCuYklJddxwTtAYBXyIeW_D5pq4OYFRtz7dPB73g_wn5PnnSD8lF11qyKkRdDAobvLhU&usqp=CAU")
    bot.send_message(message.from_user.id, "Существуют несколько уровней проклятых духов: от 4 до 1 и также есть особый уровень. Такая же система с магами. Тебе прийдется сразиться с духом 4 уровня и там нас ожидает моя ученица - Нобара Кугисаки! Я думаю вы поладите!")
    bot.send_photo(message.from_user.id, "https://static.wikia.nocookie.net/jujutsu-kaisen/images/0/0b/Yuji_afraid_of_Jogo_%28Anime%29.png/revision/latest?cb=20201114063838")
    bot.send_message(message.from_user.id, "Про себя - У НИХ ЕСТЬ ДЕВУШКИ")
    bot.send_message(message.from_user.id, "https://www.youtube.com/watch?v=IVxBxOCtPUY")
    bot.send_message(message.from_user.id, "Все таки мы дошли")
    bot.send_photo(message.from_user.id, "https://static.wikia.nocookie.net/jujutsu-kaisen/images/a/aa/Nobara_staying_true_to_herself_%28Anime%29.png/revision/latest?cb=20201017023605")
    bot.send_message(message.from_user.id, "Здравствуйте учитель Годжо!")
    bot.send_photo(message.from_user.id, "https://i.pinimg.com/736x/a7/53/9a/a7539ae742a93aff46050c5bfa79b5c1.jpg")
    bot.send_message(message.from_user.id, "У нас что теперь есть еще один мужик в магическом колледже!?")
    bot.send_photo(message.from_user.id, "https://asset.kompas.com/crops/9_MBHaHOmNsW78CbYeZTfXDVDIg=/46x0:876x553/750x500/data/photo/2023/09/21/650b9b6f28d8d.png")
    bot.send_message(message.from_user.id, "Дыааааааа)))))")
    bot.send_message(message.from_user.id, "И его зовут Итадори Юджи!")
    bot.send_photo(message.from_user.id, "https://static.wikia.nocookie.net/jujutsu-kaisen/images/0/0b/Yuji_afraid_of_Jogo_%28Anime%29.png/revision/latest?cb=20201114063838")
    bot.send_message(message.from_user.id, "...")
    bot.send_photo(message.from_user.id, "https://qph.cf2.quoracdn.net/main-qimg-1acd324f0758fd639f381426df97df47-lq")
    bot.send_message(message.from_user.id, "Ладно. Привет новенький. Наша цель изгнать проклятого духа 4 уровня.")
    bot.send_photo(message.from_user.id, "https://static.wikia.nocookie.net/jujutsu-kaisen/images/6/66/Kechizu_%28Anime%29.png/revision/latest/scale-to-width-down/138?cb=20210308013652")
    bot.send_message(message.from_user.id, "Автор: Простите! Никто не выкладывает в сеть таких слабых проклятых духов. Спасибо за понимание")
    bot.send_photo(message.from_user.id, "https://asset.kompas.com/crops/9_MBHaHOmNsW78CbYeZTfXDVDIg=/46x0:876x553/750x500/data/photo/2023/09/21/650b9b6f28d8d.png")
    bot.send_message(message.from_user.id, "А вот и он нападай")
    bot.send_message(message.from_user.id, "Что ты выберешь /q5 - бежать /q6 начать битву")
@bot.message_handler(commands=["q5"])
def nowellabadend(message):
    bot.send_photo(message.from_user.id, "https://i.ebayimg.com/images/g/r5gAAOSwso9lOGFl/s-l400.png")
    bot.send_message(message.from_user.id, "ТЫ СЕЙЧАС СЕРЬЕЗНО?")
    bot.send_photo(message.from_user.id, "https://www.mundodeportivo.com/alfabeta/hero/2023/10/yuji-itadori-aumento-de-poder-jujutsu-kaisen-capitulo-238-del-manga.jpg?width=768&aspect_ratio=16:9&format=nowebp")
    bot.send_message(message.from_user.id, "Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ Я ПЕРЕДУМАЛ")
    bot.send_message(message.from_user.id, "Плохая концовка. Концовка 1/3 - вы не попали в колледж и предали Нобару и Годжо. /newgame для новой игры")
@bot.message_handler(commands=["q4","2"])
def nowella2variant4(message):
    bot.send_photo(message.from_user.id , 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1QjgBeixcRg4K2-rQu2-Loho96EJ5nJcnvVfF9fOdkA&s')
    bot.send_message(message.from_user.id, 'Хорошо.')
    nowella3(message)
@bot.message_handler(commands=["1"])
def nowella2pre(message):
    bot.send_photo(message.from_user.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk44FOFw4rTKJFpB7Vn0WFz4DoNoZ_BTU4YPvzUhztFA&s")
    bot.send_message(message.from_user.id, 'Давай')
    nowella2inf2(message)

def nowella2inf2(message):
    bot.send_message(message.from_user.id, "/q1 - Ты кто? /q2 - А ты сильный? /q3 - У тебя хорошие ученеки? /q4 - Ладно я готов к проверке")
@bot.message_handler(commands=["q1"])
def nowella2variant1(message):
    bot.send_message(message.from_user.id, 'Я? Меня зовут Годжо Сатору. Я очень веселый и из-за этого меня недолюбливают. Этого тебе пока что достаточно')
    nowella2inf2(message)
@bot.message_handler(commands=["q2"])
def nowella2variant2(message):
    bot.send_photo(message.from_user.id, "https://www.hindustantimes.com/ht-img/img/2023/07/28/1600x900/Screenshot_2023-07-27_234919_1690524990508_1690525009794.png")
    bot.send_message(message.from_user.id, '*воспоминания*')
    bot.send_message(message.from_user.id, 'Сильнейший!')
    nowella2inf2(message)
@bot.message_handler(commands=["q3"])
def nowella2variant3(message):
    bot.send_message(message.from_user.id, 'Лучшие! Вот например Фушигуру Мэгуми - это человек который тебя спас от проклятого духа')
    nowella2inf2()



    

@bot.message_handler(commands = ["newgame"])
def nowella(message):
    bot.send_photo(message.from_user.id, "https://static0.gamerantimages.com/wordpress/wp-content/uploads/2022/11/gojo-satoru.jpg")
    bot.send_message(message.from_user.id, "Привееееееет! Ты Итадори Юджи, да? Ты, я слышал, хочешь попасть в магический колледж. Хе. Ты для меня слаб. Но я дам тебе шанс. Так как ты ел пальцы Сукуны я дам тебе шанс(Если ты съешь все 20 пальцев то Сукуна пробудится и всему миру настанет конец. Владельцу дает возможность переключаться на Сукуну, а тот, когда пожелает, переключит тебя обратно)")
    bot.send_message(message.from_user.id, "Что ты выберешь? /1 - Давай поговорим. /2 - Ладно я готов")
        



@bot.message_handler(commands=["start"])


def get_text_messages(message):
    bot.send_message(message.from_user.id, "Добро Пожаловать!")
    bot.send_photo(message.from_user.id, "https://staticg.sportskeeda.com/editor/2022/01/cbc36-16421825565301-1920.jpg?w=640")
    bot.send_message(message.from_user.id, "Это визуальная новелла по аниме магическая битва где тебе нужно попасть в магический колледж(сюжет не совсем как в аниме) Предыстория: Ты - Итадори Юджи. Ты хочешь попасть в магический колледж и желаешь стать сильнее чтобы защищать людей. Ты встретил учителя магического колледжа и тебе нужно убедить его чтобы попасть туда.")
    bot.send_message(message.from_user.id, "Напиши /newgame чтобы начать игру")

        


            



    

bot.polling(none_stop=True)