
# importing required libraries
import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

# this is the main function in which we define our app
def main():
    # header of the page
    html_temp = """
    <style>
        /* CSS styling */
        body {
            background-color: #f0f0f0;
        }
        .header {
            background-color: #007bff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .header h1 {
            color: white;
            text-align: center;
        }
        .input-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .result-container {
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
    <div class="header">
        <h1>Check your Loan Eligibility</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    Gender = st.selectbox('Gender', ("Male", "Female", "Other"))
    Married = st.selectbox('Marital Status', ("Unmarried", "Married", "Other"))
    ApplicantIncome = st.number_input("Monthly Income in Rupees")
    LoanAmount = st.number_input("Loan Amount in Rupees")
    result = ""

    # when 'Check' is clicked, make the prediction and store it
    if st.button("Check"):
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount)
        st.markdown(
            f'<div class="result-container"><b>Your loan is {result}</b></div>',
            unsafe_allow_html=True)

# defining the function which will make the prediction using the data which the user inputs
def prediction(Gender, Married, ApplicantIncome, LoanAmount):
    # 2. Loading and Pre-processing the data
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1

    if Married == "Married":
        Married = 1
    else:
        Married = 0

    # 3. Building the model to automate Loan Eligibility
    prediction = classifier.predict([[Gender, Married, ApplicantIncome, LoanAmount]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred

if __name__ == '__main__':
    main()
