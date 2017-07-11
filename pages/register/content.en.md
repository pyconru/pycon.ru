To participate in the conference, you should register and pay for the ticket.

<b>Tickets cost:</b>

• 17 000 rubles (upon arrival in a double or triple room)

• 27 000 rubles (for single occupancy)

<b>Your ticket includes:</b>

• Participation in the conference (2 days)

• Hotel accommodation

• Lunch and dinner on July, 16 and breakfast and lunch on July, 17

• All coffee breaks

• Entertainment

• Bus from the city to the venue and back.


<b>Special price for students — 9 000 rubles.</b> To buy a ticket for a special price, send a student scan to om.itpeople@gmail.com, in return we will send you a promotional code. After entering this code, you will be able to buy a discount ticket.

<b>Ticket for a partner — 6 000 rubles.</b> It includes hotel accommodation, meals, coffee breaks, participation in an afterparty, but not visiting reports.

<form id="tickets_form" action="https://money.yandex.ru/eshop.xml" class="tickets">
  <div id="tickets_picker"></div>
  <div class="tickets--field">
    <label for="tickets_email" class="tickets--label">Email</label>
    <input type="email" name="custEmail" id="tickets_email" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_name" class="tickets--label">Name</label>
    <input type="text" name="custName" id="tickets_name" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_phone" class="tickets--label">Phone</label>
    <input type="text" name="cps_phone" id="tickets_phone" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_company" class="tickets--label">Company</label>
    <input type="text" name="company" id="tickets_company" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_position" class="tickets--label">Position</label>
    <input type="text" name="position" id="tickets_position" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_city" class="tickets--label">City</label>
    <input type="text" name="custAddr" id="tickets_city" class="tickets--text_input" />
  </div>
  <div
    class="tickets--field show_if_checked set_action_if_checked"
    data-sif-watch='input'
    data-sif-src="#tickets_payment_company"
    data-sif-what="#toggle_company_details"
  >
    <div class="tickets--label">Payment method</div>
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
      My company pays for me
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
      Credit card
    </label>
  </div>
  <div id="toggle_company_details" class="tickets--field">
    <label for="tickets_company_details" class="tickets--label">Your company details</label>
    <textarea name="company_details" id="tickets_company_details" cols="30" rows="10" class="tickets--textarea"></textarea>
  </div>
  <div class="tickets--field tickets--field-non_mandatory">
    <div class="tickets--label">Python experience<span class="tickets--non_mandatory"> (non-mandatory)</span></div>
    <label for="tickets_experience_expert" class="tickets--label">
      <input type="radio" name="experience" value="expert" id="tickets_experience_expert" class="tickets--radio_input"/>
      Experienced
    </label>
    <label for="tickets_experience_novice" class="tickets--label">
      <input type="radio" name="experience" value="novice" id="tickets_experience_novice" class="tickets--radio_input" />
      Beginner
    </label>
    <label for="tickets_experience_no" class="tickets--label">
      <input type="radio" name="experience" value="no" id="tickets_experience_no" class="tickets--radio_input" />
      I don't use Python
    </label>
  </div>
  <div class="tickets--warning"></div>
  <input type="submit" value="Buy tickets" class="tickets--submit" />

  <input type="hidden" name="shopId" value="135957" />
  <input type="hidden" name="scid" value="98736" />
  <input type="hidden" name="paymentType" value="AC" />
  <input type="hidden" name="orderDetails" id="tickets_order_details" />
  <input type="text" name="_gotcha" style="display:none" />
</form>

<script src="https://code.jquery.com/jquery-2.2.3.min.js" integrity="sha256-a23g1Nt4dtEYOj7bR+vTu7+T8VP13humZFBJNIYoEJo=" crossorigin="anonymous"></script>
<script src="/2017/js/tickets_en-11.js"></script>
