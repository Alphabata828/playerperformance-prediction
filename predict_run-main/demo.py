import streamlit as st
import util

def main():
    st.title("Run Prediction App")

    # Input form
    PLAYER = st.text_input("Player Name")
    Avg = st.number_input("Batting Average")
    BF = st.number_input("Balls Faced", step=1, format="%d")
    SR = st.number_input("Strike Rate")
    Fours = st.number_input("Number of Fours", step=1, format="%d")
    Six = st.number_input("Number of Sixes", step=1, format="%d")

    if st.button("Predict Run"):
        try:
            # Make prediction
            prediction = util.estimated_run(PLAYER, Avg, BF, SR, Fours, Six)

            # Display prediction
            st.success(f"Estimated Run: {prediction}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    util.load_saved_artifacts()
    main()
