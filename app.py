import streamlit as st

st.set_page_config(page_title="WeGang Pricing Dashboard", page_icon="🧑‍🤝‍🧑")

st.title("🧑‍🤝‍🧑 WeGang Pricing & Break-even Dashboard")
st.markdown("""
This dashboard helps you estimate infrastructure cost, set premium pricing, and see your break-even user count.

แดชบอร์ดนี้ช่วยให้คุณคำนวณต้นทุน, ตั้งราคาพรีเมียม และดูจุดคุ้มทุนของแอป WeGang ได้ทันที
""")

st.header("1. Infrastructure & Operation Cost (ต้นทุนต่อเดือน)")

infra_cost = st.number_input("Infra Cost (AWS + R2) / ต้นทุนระบบ (บาท)", min_value=0, value=8000, step=500)
soft_cost = st.number_input("Soft Cost (Dev, Support, Marketing) / ทีมงาน+ซัพพอร์ต (บาท)", min_value=0, value=1000, step=500)
total_cost = infra_cost + soft_cost

st.success(f"**ต้นทุนรวมต่อเดือน (Total Monthly Cost): {total_cost:,.0f} บาท**")

st.header("2. Set Your Premium Price (ตั้งราคาพรีเมียม)")

price_per_user = st.slider("Premium Price per User (THB) / ราคาต่อคนต่อเดือน", 19, 199, 59, 1)
st.caption("แนะนำเริ่มต้น 59 บาท/เดือน (Start with 59 THB/month for Thai market)")

st.header("3. Break-even Calculation (คำนวณจุดคุ้มทุน)")

break_even_users = total_cost / price_per_user if price_per_user > 0 else 0
st.metric("Break-even Paid Users (จำนวนผู้ใช้จ่ายเงินเพื่อคุ้มทุน)", f"{break_even_users:.0f} คน/เดือน")

st.header("4. Conversion Rate Simulator (ลองแปลง % ผู้ใช้ที่ยอมจ่าย)")
conversion_rate = st.slider("Paid Conversion Rate (%)", 1, 20, 5)
active_users_needed = break_even_users / (conversion_rate / 100) if conversion_rate > 0 else 0
st.metric("Estimated Active Users Needed (ประมาณ active users ที่ต้องมี)", f"{active_users_needed:,.0f} คน")

st.header("5. Annual Revenue & Margin (ประมาณรายได้และกำไร)")

annual_paid_users = st.number_input("Estimated Paid Users (Paid Users/Month)", min_value=0, value=int(break_even_users)+100)
annual_revenue = annual_paid_users * price_per_user * 12
annual_cost = total_cost * 12
profit = annual_revenue - annual_cost

col1, col2, col3 = st.columns(3)
col1.metric("Annual Revenue (รายได้/ปี)", f"{annual_revenue:,.0f} บาท")
col2.metric("Annual Cost (ต้นทุน/ปี)", f"{annual_cost:,.0f} บาท")
col3.metric("Estimated Profit (กำไร)", f"{profit:,.0f} บาท")

st.info("""
**Tips:**
- Lower your cost or increase premium price to reach break-even faster.
- Increase conversion rate (more people willing to pay) for sustainable growth.

**คำแนะนำ:**  
- ลดต้นทุนหรือเพิ่มราคาจะคุ้มทุนไวขึ้น  
- ถ้าทำให้ผู้ใช้ยอมจ่ายเพิ่ม (conversion สูงขึ้น) จะกำไรยั่งยืน
""")

st.markdown("---")
st.markdown("Aey - thungong@thatwhy.me Made for WeGang Pricing Simulation")