import streamlit as st

# Page title
st.title("🧮 Calculator")

# Number inputs ( here we have to enter numbers)
num1 = st.number_input(
    "Enter first number",
    value=None,
    placeholder="Type first number"
)

num2 = st.number_input(
    "Enter second number",
    value=None,
    placeholder="Type second number"
)

# Operator selection
operation = st.selectbox(
    "Select your operator",
    ["+", "-", "*", "/"],
    index=None,
    placeholder="Choose an operation"
)

# Calculate button
if st.button("Calculate"):

    # Check if user entered everything
    if num1 is None or num2 is None or operation is None:
        st.warning("⚠️ Please fill in all the fields.")

    else:
        # Perform calculation
        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                st.error("❌ Cannot divide by zero.")
                st.stop()
            result = num1 / num2

        # Display result
        st.success(f"✅ Result = {result}")