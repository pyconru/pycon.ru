## Стоимость участия в PYCON RUSSIA 2019

Желающих участвовать оказалось много, и несмотря на то, что мы выкупили все номера на базах «Cronwell Яхонты Таруса» и «PineRiver», билеты с проживанием закончились.

## Билет без проживания стоит 17 000 рублей
Вы можете купить билет без проживания. В этом случае вы сами выбираете, где ночевать, сами оплачиваете и добираетесь до места ночевки. 

В стоимость билета входит:

• участие в конференции (2 дня);

• обед и ужин 24 июня, завтрак и обед 25 июня;

• все кофе-брейки;

• развлекательная программа;

• автобусы от станции метро «Аннино» до места проведения конференции 24 июня и обратно 25 июня.

Некоторые варианты, где вы можете остановиться на ночь: парк-отель [«Дракино»](http://www.drakino-hotel.ru/contact.html), санаторий [«Вятичи»](http://www.booking.com/Share-r2aKcC), [гостиницы в г. Обнинск](http://bit.ly/2HsPLB9), [гостиницы в г. Калуга](http://bit.ly/2VQiUz9).

Кроме этого, вы можете взять палатку и переночевать в ней на территории «Тарусы». Волонтеры покажут вам, где ее можно разбить. Обязательно возьмите собственную палатку или договоритесь с другом о месте в его палатке, арендовать палатку на месте не получится. Не забудьте про спальник, пенку, репелленты, теплую одежду (ночью может быть холодно). Принять душ можно будет в корпусе №11.

## Специальная цена для студентов

Гранты на студенческие билеты закончились.

## Регистрация на PYCON RUSSIA 2019

Если за ваше участие заплатит компания, укажите реквизиты в анкете регистрации, и мы вышлем вам счет на оплату. Либо напишите на [mppycon@gmail.com](mailto:mppycon@gmail.com), и мы выставим вам счет.

Мы работаем с участниками на основании [Договора-оферты](https://drive.google.com/drive/folders/1zi8DRX962ZoZzIAOizFm8j0s7Wt7hp4-?usp=sharing). Основанием для счета служит этот договор.

<b>Обратите внимание:</b> по правилам отеля заселение проходит с 17.30. До заселения в номера вещи можно будет оставить в специальном месте. 

Следующее повышение цены — 5 июня.

<form id="tickets_form" action="#" class="tickets">
  <div
    class="tickets--field show_if_checked set_action_if_checked"
    data-sif-watch='input'
    data-sif-src="#tickets_payment_company"
    data-sif-what="#toggle_company_details"
  >
    <div class="tickets--label">Метод оплаты</div>
    <label for="tickets_payment_company" class="tickets--label">
      <input
        type="radio"
        name="payment"
        value="company"
        id="tickets_payment_company"
        class="tickets--radio_input set_action_on_check"
        data-saic-action="#"
        data-saic-method="post"
      />
      За меня заплатит компания
    </label>
    <label for="tickets_payment_card" class="tickets--label">
      <input
        type="radio"
        name="payment"
        value="card"
        id="tickets_payment_card"
        class="tickets--radio_input set_action_on_check"
        data-saic-action="#"
        data-saic-method="post"
        checked
      />
      Заплачу сам банковской картой
    </label>
  </div>
  <div id="tickets_picker"></div>
  <div class="tickets--field">
    <label for="tickets_email" class="tickets--label">Почта</label>
    <input type="email" name="email" id="tickets_email" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_name" class="tickets--label">Имя и фамилия</label>
    <input type="text" name="name" id="tickets_name" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_phone" class="tickets--label">Телефон</label>
    <input type="text" name="phone" id="tickets_phone" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_company" class="tickets--label">Компания</label>
    <input type="text" name="company" id="tickets_company" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_position" class="tickets--label">Должность</label>
    <input type="text" name="position" id="tickets_position" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_city" class="tickets--label">Город</label>
    <input type="text" name="city" id="tickets_city" class="tickets--text_input" />
  </div>
  <div id="toggle_company_details" class="tickets--field">
    <label for="tickets_company_details" class="tickets--label">Укажите реквизиты компании</label>
    <textarea name="company_details" id="tickets_company_details" cols="30" rows="10" class="tickets--textarea"></textarea>
  </div>
  <div class="tickets--field">
    <div class="tickets--label">Нужно ли вам место в автобусе?</div>
    <label for="tickets_bus_yes" class="tickets--label">
      <input type="radio" name="bus" value="yes" id="tickets_bus_yes" class="tickets--radio_input" />
      Да
    </label>
    <label for="tickets_bus_no" class="tickets--label">
      <input type="radio" name="bus" value="no" id="tickets_bus_no" class="tickets--radio_input" checked />
      Нет
    </label>
  </div>
  <div class="tickets--field">
    <div class="tickets--label">Нужно ли вам место для палатки?</div>
    <label for="tickets_tent_yes" class="tickets--label">
      <input type="radio" name="tent" value="yes" id="tickets_tent_yes" class="tickets--radio_input" />
      Да
    </label>
    <label for="tickets_tent_no" class="tickets--label">
      <input type="radio" name="tent" value="no" id="tickets_tent_no" class="tickets--radio_input" checked />
      Нет
    </label>
  </div>
  <div class="tickets--field tickets--field-non_mandatory">
    <div class="tickets--label">Опыт разработки на Python <span class="tickets--non_mandatory">(не обязательно)</span></div>
    <label for="tickets_experience_senior" class="tickets--label">
      <input type="radio" name="experience" value="senior" id="tickets_experience_senior" class="tickets--radio_input" />
      Senior-разработчик Python
    </label>
    <label for="tickets_experience_middle" class="tickets--label">
      <input type="radio" name="experience" value="middle" id="tickets_experience_middle" class="tickets--radio_input" />
      Middle-разработчик Python
    </label>
    <label for="tickets_experience_junior" class="tickets--label">
      <input type="radio" name="experience" value="junior" id="tickets_experience_junior" class="tickets--radio_input" />
      Начинающий разработчик Python
    </label>
    <label for="tickets_experience_no" class="tickets--label">
      <input type="radio" name="experience" value="no" id="tickets_experience_no" class="tickets--radio_input" />
      Не пишу на Python
    </label>
  </div>
  <div class="tickets--field">
    <label for="tickets_agreement" class="tickets--label">
      <input type="checkbox" name="agreement" value="true" id="tickets_agreement" class="tickets--radio_input" />
      Даю <a href="https://drive.google.com/file/d/1UNIwtiqYnGZihgHoCf2szbktEsTcF-gz/view?usp=sharing">согласие</a> на обработку моих персональных данных.
    </label>
  </div>
  <div class="tickets--warning"></div>
  <input type="submit" value="Купить билеты" class="tickets--submit" />

  <input type="text" name="_gotcha" style="display:none" />
</form>

<div id="thanks" style="font-size: 18px; color: #4382b4; display: none;">Спасибо, мы скоро свяжемся с вами.</div>

<div id="tickets_widget_wrap" style="display: none;">
  <button type="button" class="" data-tc-event="5c5bc82fc5bbea000ca8cc16" data-tc-token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzcyI6InRpY2tldHNjbG91ZC5ydSJ9.eyJwIjoiNWM1ODE3NTM0ZmFhMzQwMDBiYmEzY2NlIn0.tzOwUZK1HxGx2pVCFT2P3Mx2wwDPKHbW7BIVHoMjGlE"> Купить билет </button>
</div>

<script src="https://code.jquery.com/jquery-2.2.3.min.js" integrity="sha256-a23g1Nt4dtEYOj7bR+vTu7+T8VP13humZFBJNIYoEJo=" crossorigin="anonymous"></script>
<script src="/2019/js/tickets-f.js"></script>

<script src="https://ticketscloud.com/static/scripts/widget/tcwidget.js"></script>
