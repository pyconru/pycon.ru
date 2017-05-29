<!--  Регистрация скоро откроется. -->

 Чтобы принять участие в конференции, зарегистрируйтесь и оплатите билет.
 
 <b>Обратите внимание:</b> количество мест на конференцию ограничено количеством номеров в отеле.

<b>Стоимость билетов до 30 июня:</b>

• 15 500 (при заселении в двухместный или трехместный номер)

• 22 000 (при одноместном заселении)

<b>В стоимость билета входит:</b>

• участие в конференции (2 дня);

• проживание;

• обед и ужин 16 июля, завтрак и обед 17 июля;

• все кофе-брейки;

• развлекательная программа;

• автобусы от станции метро «Аннино» до места проведения конференции и обратно 16 и 17 июля.

 <b>Специальная цена для студентов</b> — 9000 рублей. Цена фиксированная, действует все время продажи билетов. Чтобы купить билет по спец.цене, пришлите скан студенческого на [om.itpeople@gmail.com](om.itpeople@gmail.com), в ответ мы вышлем промокод. Введя этот код, вы сможете купить билет со скидкой.

Если участие будет оплачивать <b>юридическое лицо</b>, укажите реквизиты в анкете регистрации, и мы вышлем вам счет на оплату. Либо напишите на [om.itpeople@gmail.com](om.itpeople@gmail.com), и мы выставим вам счет.

<b>Обратите внимание:</b> по правилам отеля заселение проходит с 17.30. До заселения в номера вещи можно будет оставить в специальном месте. Если вам принципиально важен «ранний заезд», напишите нам об этом заранее. Это платная услуга.

<form id="tickets_form" action="https://money.yandex.ru/eshop.xml" class="tickets">
  <div id="tickets_picker"></div>
  <div class="tickets--field">
    <label for="tickets_email" class="tickets--label">Почта</label>
    <input type="email" name="custEmail" id="tickets_email" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_name" class="tickets--label">Имя и фамилия</label>
    <input type="text" name="custName" id="tickets_name" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_phone" class="tickets--label">Телефон</label>
    <input type="text" name="cps_phone" id="tickets_phone" class="tickets--text_input" />
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
    <input type="text" name="custAddr" id="tickets_city" class="tickets--text_input" />
  </div>
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
        data-saic-action="https://formspree.io/om.itpeople@gmail.com"
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
        data-saic-action="https://money.yandex.ru/eshop.xml"
        data-saic-method="get"
        checked
      />
      Заплачу сам банковской картой
    </label>
  </div>
  <div id="toggle_company_details" class="tickets--field">
    <label for="tickets_company_details" class="tickets--label">Укажите реквизиты компании</label>
    <textarea name="company_details" id="tickets_company_details" cols="30" rows="10" class="tickets--textarea"></textarea>
  </div>
  <div class="tickets--field tickets--field-non_mandatory">
    <div class="tickets--label">Опыт разработки на Python <span class="tickets--non_mandatory">(не обязательно)</span></div>
    <label for="tickets_experience_expert" class="tickets--label">
      <input type="radio" name="experience" value="expert" id="tickets_experience_expert" class="tickets--radio_input"/>
      Опытный разработчик Python
    </label>
    <label for="tickets_experience_novice" class="tickets--label">
      <input type="radio" name="experience" value="novice" id="tickets_experience_novice" class="tickets--radio_input" />
      Начинающий разработчик Python
    </label>
    <label for="tickets_experience_no" class="tickets--label">
      <input type="radio" name="experience" value="no" id="tickets_experience_no" class="tickets--radio_input" />
      Не пишу на Python
    </label>
  </div>
  <div class="tickets--warning"></div>
  <input type="submit" value="Купить билеты" class="tickets--submit" />

  <input type="hidden" name="shopId" value="135957" />
  <input type="hidden" name="scid" value="98736" />
  <input type="hidden" name="paymentType" value="AC" />
  <input type="hidden" name="orderDetails" id="tickets_order_details" />
  <input type="text" name="_gotcha" style="display:none" />
</form>

<script src="https://code.jquery.com/jquery-2.2.3.min.js" integrity="sha256-a23g1Nt4dtEYOj7bR+vTu7+T8VP13humZFBJNIYoEJo=" crossorigin="anonymous"></script>
<script src="/2017/js/tickets-7.js"></script>
