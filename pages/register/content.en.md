## The tickets' cost

The tickets cost:

• 20 000 rubles (upon arrival in a double or triple room)

• 26 000 rubles (for single occupancy) 

<b>Your ticket includes:</b>

• Participation in the conference (2 days)
	
• Hotel accommodation
	
• Lunch and dinner on June, 24 and breakfast and lunch on June, 25
	
• All coffee breaks
	
• Entertainment
	
• Bus from the city to the venue and back.
	
## Special price for students
	
Special discount for students: -50%. To buy a ticket for a special price, send a student scan to mppycon@gmail.com, in return we will send you a promotional code. After entering this code, you will be able to buy a discount ticket.

## Registration

<form id="tickets_form" action="#" class="tickets">
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
        data-saic-action="#"
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
        data-saic-action="#"
        data-saic-method="post"
        checked
      />
      Credit card
    </label>
  </div>
  <div id="tickets_picker"></div>
  <div class="tickets--field">
    <label for="tickets_email" class="tickets--label">Email</label>
    <input type="email" name="email" id="tickets_email" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_name" class="tickets--label">Name</label>
    <input type="text" name="name" id="tickets_name" class="tickets--text_input" />
  </div>
  <div class="tickets--field">
    <label for="tickets_phone" class="tickets--label">Phone</label>
    <input type="text" name="phone" id="tickets_phone" class="tickets--text_input" />
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
    <input type="text" name="city" id="tickets_city" class="tickets--text_input" />
  </div>
  <div id="toggle_company_details" class="tickets--field">
    <label for="tickets_company_details" class="tickets--label">Your company details</label>
    <textarea name="company_details" id="tickets_company_details" cols="30" rows="10" class="tickets--textarea"></textarea>
  </div>
  <div class="tickets--field">
    <div class="tickets--label">Do you want to use the bus transfer?</div>
    <label for="tickets_bus_yes" class="tickets--label">
      <input type="radio" name="bus" value="yes" id="tickets_bus_yes" class="tickets--radio_input" />
      Yes
    </label>
    <label for="tickets_bus_no" class="tickets--label">
      <input type="radio" name="bus" value="no" id="tickets_bus_no" class="tickets--radio_input" checked />
      No
    </label>
  </div>
  <div class="tickets--field tickets--field-non_mandatory">
    <div class="tickets--label">Python experience <span class="tickets--non_mandatory">(non-mandatory)</span></div>
    <label for="tickets_experience_senior" class="tickets--label">
      <input type="radio" name="experience" value="senior" id="tickets_experience_senior" class="tickets--radio_input" />
      Senior developer
    </label>
    <label for="tickets_experience_middle" class="tickets--label">
      <input type="radio" name="experience" value="middle" id="tickets_experience_middle" class="tickets--radio_input" />
      Middle developer
    </label>
    <label for="tickets_experience_junior" class="tickets--label">
      <input type="radio" name="experience" value="junior" id="tickets_experience_junior" class="tickets--radio_input" />
      Beginner
    </label>
    <label for="tickets_experience_no" class="tickets--label">
      <input type="radio" name="experience" value="no" id="tickets_experience_no" class="tickets--radio_input" />
      I don't use Python
    </label>
  </div>
  <div class="tickets--field">
    <label for="tickets_agreement" class="tickets--label">
      <input type="checkbox" name="agreement" value="true" id="tickets_agreement" class="tickets--radio_input" />
      I <a href="https://drive.google.com/file/d/1UNIwtiqYnGZihgHoCf2szbktEsTcF-gz/view?usp=sharing">agree</a> with my personal data being collected and processed.
    </label>
  </div>
  <div class="tickets--warning"></div>
  <input type="submit" value="Buy tickets" class="tickets--submit" />

  <input type="text" name="_gotcha" style="display:none" />
</form>

<div id="thanks" style="font-size: 18px; color: #4382b4; display: none;">Thank you! We will contact you shortly.</div>

<div id="tickets_widget_wrap" style="display: none;">
  <button type="button" class="" data-tc-event="5c5bc82fc5bbea000ca8cc16" data-tc-token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzcyI6InRpY2tldHNjbG91ZC5ydSJ9.eyJwIjoiNWM1ODE3NTM0ZmFhMzQwMDBiYmEzY2NlIn0.tzOwUZK1HxGx2pVCFT2P3Mx2wwDPKHbW7BIVHoMjGlE"> Buy a ticket </button>
</div>

<script src="https://code.jquery.com/jquery-2.2.3.min.js" integrity="sha256-a23g1Nt4dtEYOj7bR+vTu7+T8VP13humZFBJNIYoEJo=" crossorigin="anonymous"></script>
<script src="/2019/js/tickets_en-1.js"></script>

<script src="https://ticketscloud.com/static/scripts/widget/tcwidget.js"></script>
