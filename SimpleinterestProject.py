import streamlit as st
from datetime import datetime

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, start_date, end_date):
    # Convert dates (date objects -> datetime)
    start = datetime.combine(start_date, datetime.min.time())
    end = datetime.combine(end_date, datetime.min.time())
    
    # Calculate time in months
    time_in_months = (end.year - start.year) * 12 + (end.month - start.month)
    
    # Convert months to years (float)
    time_in_years = time_in_months / 12
    
    # Simple Interest calculation
    simple_interest = (principal * rate * time_in_months) / 100
    
    # Final Amount
    final_amount = principal + simple_interest
    
    return simple_interest, final_amount, time_in_months, time_in_years


# Streamlit App
st.title("📊 Simple Interest Calculator")

# User Inputs
principal = st.number_input("Enter Principal Amount:", min_value=0.0, step=100.0)
rate = st.number_input("Enter Rate of Interest (per month %):", min_value=0.0, step=0.1)

start_date = st.date_input("Select Start Date:")
end_date = st.date_input("Select End Date:")

# Calculate when button clicked
if st.button("Calculate Interest"):
    if start_date >= end_date:
        st.error("⚠️ End Date must be after Start Date.")
    else:
        si, total, months, years = calculate_simple_interest(
            principal, rate, start_date, end_date
        )
        
        st.success("✅ Calculation Completed!")
        
        # Display all details in GUI
        st.markdown("### 📑 Calculation Summary")
        st.markdown(f"**Principal Amount:** ₹ {principal:,.2f}")
        st.markdown(f"**Rate of Interest:** {rate:.2f} % per month")
        st.markdown(f"**Start Date:** {start_date.strftime('%d-%m-%Y')}")
        st.markdown(f"**End Date:** {end_date.strftime('%d-%m-%Y')}")
        st.markdown(f"**Time Period:** {months} months ({years:.2f} years)")
        st.markdown(f"**Simple Interest:** ₹ {si:,.2f}")
        st.markdown(f"**Final Amount:** ₹ {total:,.2f}")
