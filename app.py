import streamlit as st
import urllib.parse

# ژمارەیا تە یا واتس ئەپێ
MY_WHATSAPP = "9647504909929" 

st.set_page_config(page_title="Mardin Qasrok", page_icon="🍕")

# دیزاینا سایتێ
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url("https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1000");
        background-size: cover;
        color: white;
    }
    h1, h2, h3, p, label { color: white !important; text-align: right; direction: rtl; }
    .food-card {
        background-color: rgba(30, 30, 30, 0.9);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #444;
        margin-bottom: 20px;
        text-align: center;
    }
    /* ستایلێ دوکما سۆر */
    .stButton>button {
        background-color: #e74c3c !important;
        color: white !important;
        border-radius: 10px;
        width: 100%;
        border: none;
    }
    input, textarea { background-color: #222 !important; color: white !important; text-align: right !important; direction: rtl !important; }
</style>
""", unsafe_allow_html=True)

st.title("🍴 خارنگەها ماردین قەسرۆک")

# لیستا خوارنان
menu_data = [
    {"id": "piz", "name": "پیتزا ایطالي 🍕", "price": 5000, "opts": ["مریشک 🍗", "گۆشت 🥩", "نیڤ ب نیڤ 🌗"]},
    {"id": "laf_s", "name": "لەفا سوری 🌯", "price": 2000, "opts": ["فەلافل", "پەتاتە", "تێکەڵاو"]},
    {"id": "laf_m", "name": "لەفا مریشکی 🍗", "price": 1000, "opts": ["ئاسایی", "تیژ 🔥"]},
    {"id": "lb", "name": "لەحم بعجین 🌮", "price": 2500, "opts": ["سادە", "دگەل پەنێری"]}
]

if "cart" not in st.session_state:
    st.session_state.cart = []

# نیشاندانا خوارنان دگەل بۆشایییا تێبینییان
for food in menu_data:
    with st.container():
        st.markdown(f'<div class="food-card">', unsafe_allow_html=True)
        st.markdown(f"### {food['name']}")
        st.write(f"بها: {food['price']} دینار")
        
        f_type = st.selectbox(f"جۆرێ خوارنێ:", food['opts'], key=f"t_{food['id']}")
        f_qty = st.number_input(f"ژمارە:", min_value=1, max_value=20, value=1, key=f"q_{food['id']}")
        
        # بۆشایییا تێبینییا تایبەت بۆ هەر خوارنەکێ
        f_note = st.text_input(f"تێبینی بۆ {food['name']}:", placeholder="بۆ نموونە: بلا باش قەلی بیت...", key=f"n_{food['id']}")
        
        if st.button(f"🛒 زێدە بکە", key=f"b_{food['id']}"):
            st.session_state.cart.append({
                "name": food['name'],
                "type": f_type,
                "qty": f_qty,
                "note": f_note,
                "price_val": food['price'] * f_qty
            })
            st.toast(f"✅ {food['name']} زێدە بوو")
        st.markdown('</div>', unsafe_allow_html=True)

# پشکا سەبەتەی و ناردنێ
if st.session_state.cart:
    st.divider()
    st.header("🛒 سەبەتەیا تە")
    grand_total = 0
    details = ""
    for item in st.session_state.cart:
        price = item.get('price_val', 0)
        qty = item.get('qty', 1)
        name_item = item.get('name', 'خوارن')
        type_item = item.get('type', 'ئاسایی')
        note_item = item.get('note', '')
        
        grand_total += price
        st.write(f"🔹 {qty} {name_item} ({type_item}) - {note_item}")
        
        # زێدەکرنا تێبینییا کڕیاری بۆ ناڤ نامەیا واتس ئەپێ
        details += f"- {qty} {name_item} ({type_item})"
        if note_item:
            details += f" [تێبینی: {note_item}]"
        details += "\n"
    
    st.subheader(f"💰 کۆمێ گشتی: {grand_total} دینار")
    
    # ئامادەکردنا نامەیێ
    msg = f"📦 تەڵەبەکا نوو هات!\n\n🍴 خوارن:\n{details}\n💵 کۆم: {grand_total} دینار"
    url = f"https://wa.me/{MY_WHATSAPP}?text={urllib.parse.quote(msg)}"
    
    st.markdown(f'<a href="{url}" target="_blank" style="background:#25d366; color:white; padding:15px; border-radius:10px; text-decoration:none; display:block; text-align:center; font-weight:bold;">✅ تەمامکرن د واتس ئەپێ دا</a>', unsafe_allow_html=True)
    st.info("تەڵەب ب کێمتر ژ ١ سەعەت دێ گەهیت. دگەل ڕێز و سلاڤان.")

if st.button("🗑️ پاکژکرنا سەبەتەی"):
    st.session_state.cart = []
    st.rerun()
