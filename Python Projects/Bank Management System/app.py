import streamlit as st
import json
import random
import string
from pathlib import Path


# Hide "Press Enter to apply" text in all inputs
st.markdown("""
    <style>
    .stTextInput > div > div > input:focus + div {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ---------------------------
# Load and Save JSON
# ---------------------------
DB_FILE = "data.json"

def load_data():
    if Path(DB_FILE).exists():
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

bank_data = load_data()


# ---------------------------
# Helpers
# ---------------------------
def generate_acc_no():
    while True:
        alph = random.choices(string.ascii_letters, k=3)
        nums = random.choices(string.digits, k=3)
        sp = random.choices("!@#$%^&*", k=1)
        acc = alph + nums + sp
        random.shuffle(acc)
        acc_no = "".join(acc)

        if all(acc_no != i["accountno"] for i in bank_data):
            return acc_no


def find_user(acc, pin):
    return next((i for i in bank_data if i["accountno"] == acc and i["pin_no"] == pin), None)


# ---------------------------
# Stylish Title Banner
# ---------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#00aaff; font-size:40px;'>🏦 Bank Management System</h1>
    <hr style="border:1px solid #00aaff;">
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Sidebar Menu
# ---------------------------
menu = st.sidebar.radio(
    "📌 Choose an option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "View Details",
        "Update Details",
        "Delete Account",
        "Send Money"
    ]
)


st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Premium UI Version**")


# ================================================================
# 1️⃣ CREATE ACCOUNT
# ================================================================
if menu == "Create Account":
    st.markdown("<h2 style='color:#00c853;'>🆕 Create Account</h2>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<h4>Enter Your Details</h4>", unsafe_allow_html=True)

        name = st.text_input("Full Name", key="create_name")
        age = st.number_input("Age", min_value=1, step=1, key="create_age")
        email = st.text_input("Email", key="create_email")
        pin = st.text_input("Choose 4-digit PIN", type="password",
                            placeholder="Enter 4 digit PIN", key="create_pin")

        if st.button("Create Account", key="create_btn"):
            if age < 18:
                st.error("❌ You must be at least 18 years old.")
            elif len(pin) != 4 or not pin.isdigit():
                st.error("❌ PIN must be exactly 4 digits.")
            elif "@" not in email or not email.endswith(".com"):
                st.error("❌ Invalid email. Email must contain '@' and end with '.com'")    
            else:
                accno = generate_acc_no()
                new_user = {
                    "name": name,
                    "age": age,
                    "email": email,
                    "pin_no": int(pin),
                    "accountno": accno,
                    "balance": 0
                }
                bank_data.append(new_user)
                save_data(bank_data)

                st.success("🎉 Account Created Successfully!")
                st.info(f"**Your Account Number:** `{accno}`\n**PIN:** `{pin}`")


# ================================================================
# 2️⃣ DEPOSIT MONEY
# ================================================================
if menu == "Deposit Money":
    st.markdown("<h2 style='color:#0091ea;'>💰 Deposit Money</h2>", unsafe_allow_html=True)

    acc = st.text_input("Account Number", key="dep_acc", placeholder="e.g. Ab3#29F")
    pin = st.text_input("PIN", type="password", key="dep_pin", placeholder="4 digit PIN")

    user = find_user(acc, int(pin)) if pin.isdigit() else None

    if user:
        st.info(f"Current Balance: ₹{user['balance']}")
        amount = st.number_input("Enter Amount", min_value=1, key="dep_amount")

        if st.button("Deposit", key="dep_btn"):
            if amount > 100000:
                st.error("❌ Deposit limit is ₹100000")
            else:
                user["balance"] += amount
                save_data(bank_data)
                st.success("✅ Deposit Successful!")
                st.info(f"New Balance: ₹{user['balance']}")
    else:
        st.warning("Enter valid details to continue.")


# ================================================================
# 3️⃣ WITHDRAW MONEY
# ================================================================
if menu == "Withdraw Money":
    st.markdown("<h2 style='color:#d50000;'>🏧 Withdraw Money</h2>", unsafe_allow_html=True)

    acc = st.text_input("Account Number", key="wd_acc", placeholder="e.g. Q2f*84A")
    pin = st.text_input("PIN", type="password", key="wd_pin", placeholder="4 digit PIN")

    user = find_user(acc, int(pin)) if pin.isdigit() else None

    if user:
        st.info(f"Current Balance: ₹{user['balance']}")
        amount = st.number_input("Enter Amount", min_value=1, key="wd_amount")

        if st.button("Withdraw", key="wd_btn"):
            if amount > user["balance"]:
                st.error("❌ Insufficient Balance")
            else:
                user["balance"] -= amount
                save_data(bank_data)
                st.success("💸 Withdrawal Successful")
                st.info(f"Remaining Balance: ₹{user['balance']}")
    else:
        st.warning("Enter valid account details.")


# ================================================================
# 4️⃣ VIEW DETAILS
# ================================================================
if menu == "View Details":
    st.markdown("<h2 style='color:#6a1b9a;'>📄 View Account Details</h2>", unsafe_allow_html=True)

    acc = st.text_input("Account Number", key="view_acc")
    pin = st.text_input("PIN", type="password", key="view_pin")

    if st.button("View", key="view_btn"):
        user = find_user(acc, int(pin)) if pin.isdigit() else None

        if not user:
            st.error("❌ No account found.")
        else:
            st.success("Account Found!")
            st.table(user)


# ================================================================
# 5️⃣ UPDATE DETAILS
# ================================================================
if menu == "Update Details":
    st.markdown("<h2 style='color:#ff6d00;'>✏️ Update Details</h2>", unsafe_allow_html=True)

    acc = st.text_input("Account Number", key="upd_acc")
    pin = st.text_input("PIN", type="password", key="upd_pin")

    user = find_user(acc, int(pin)) if pin.isdigit() else None

    if user:
        name = st.text_input("New Name", value=user["name"], key="upd_name")
        email = st.text_input("New Email", value=user["email"], key="upd_email")
        new_pin = st.text_input("New PIN", value=str(user["pin_no"]),
                                key="upd_newpin", type="password")

        if st.button("Update", key="upd_btn"):
            if not new_pin.isdigit() or len(new_pin) != 4:
                st.error("❌ PIN must be 4 digits.")
            else:
                user["name"] = name
                user["email"] = email
                user["pin_no"] = int(new_pin)
                save_data(bank_data)
                st.success("✨ Details Updated Successfully")
    else:
        st.warning("Enter valid credentials.")


# ================================================================
# 6️⃣ DELETE ACCOUNT
# ================================================================
if menu == "Delete Account":
    st.markdown("<h2 style='color:#aa00ff;'>🗑️ Delete Account</h2>", unsafe_allow_html=True)

    acc = st.text_input("Account Number", key="del_acc")
    pin = st.text_input("PIN", type="password", key="del_pin")

    user = find_user(acc, int(pin)) if pin.isdigit() else None

    if user:
        st.warning("⚠️ Are you sure you want to delete your account?")
        if st.button("Delete Permanently", key="del_btn"):
            bank_data.remove(user)
            save_data(bank_data)
            st.success("🗑️ Account Deleted Permanently!")
    else:
        st.info("Enter your account details to continue.")



# ================================================================
# 7️⃣ SEND MONEY (Account → Account & Bank → Bank)
# ================================================================
if menu == "Send Money":
    st.markdown("<h2 style='color:#00bfa5;'>💸 Send Money</h2>", unsafe_allow_html=True)

    transfer_type = st.radio(
        "Select Transfer Type",
        ["Account to Account (Same Bank)", "Bank to Bank Transfer"]
    )

    # -----------------------------
    # ACCOUNT TO ACCOUNT TRANSFER
    # -----------------------------
    if transfer_type == "Account to Account (Same Bank)":
        acc = st.text_input("Your Account Number", key="t1_acc")
        pin = st.text_input("Your PIN", type="password", key="t1_pin")

        sender = find_user(acc, int(pin)) if pin.isdigit() else None

        if sender:
            st.info(f"Current Balance: ₹{sender['balance']}")

            rec_acc = st.text_input("Receiver's Account Number", key="t1_rec")

            receiver = next((i for i in bank_data if i["accountno"] == rec_acc), None)

            if receiver:
                amount = st.number_input("Amount", min_value=1, key="t1_amt")

                if st.button("Send Money", key="t1_btn"):
                    if amount <= 0 or amount > sender["balance"]:
                        st.error("Invalid amount.")
                    else:
                        sender["balance"] -= amount
                        receiver["balance"] += amount
                        save_data(bank_data)

                        st.success("Money transferred successfully.")
                        st.info(f"New Balance: ₹{sender['balance']}")
            else:
                st.warning("Enter valid receiver account.")

        else:
            st.warning("Enter correct account and PIN to continue.")

    # -----------------------------
    # BANK TO BANK TRANSFER
    # -----------------------------
    if transfer_type == "Bank to Bank Transfer":

        bank_map = {
            "State Bank of India (SBI)": "sbi.json",
            "Punjab National Bank (PNB)": "pnb.json",
            "Indian Bank": "indian.json",
            "Canera Bank": "canera.json",
            "Bank of Baroda": "bob.json"
        }

        acc = st.text_input("Your Account Number", key="t2_acc")
        pin = st.text_input("Your PIN", type="password", key="t2_pin")

        sender = find_user(acc, int(pin)) if pin.isdigit() else None

        if sender:
            st.info(f"Current Balance: ₹{sender['balance']}")

            bank_choice = st.selectbox("Select Receiver's Bank", list(bank_map.keys()))
            rec_file = bank_map[bank_choice]

            try:
                with open(rec_file, "r") as f:
                    other_bank = json.load(f)
            except:
                st.error("Error loading bank file.")
                other_bank = None

            if other_bank is not None:
                rec_acc = st.text_input("Receiver's Account Number", key="t2_rec")

                receiver = next((i for i in other_bank if i["accountno"] == rec_acc), None)

                if receiver:
                    amount = st.number_input("Amount", min_value=1, key="t2_amt")

                    if st.button("Send Money", key="t2_btn"):
                        if amount <= 0 or amount > sender["balance"]:
                            st.error("Invalid amount.")
                        else:
                            sender["balance"] -= amount
                            receiver["balance"] += amount

                            save_data(bank_data)

                            with open(rec_file, "w") as f:
                                json.dump(other_bank, f, indent=4)

                            st.success("Money transferred successfully.")
                            st.info(f"New Balance: ₹{sender['balance']}")
                else:
                    st.warning("Receiver account not found.")
        else:
            st.warning("Enter valid account number and PIN.")



