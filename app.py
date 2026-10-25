import streamlit as st

st.set_page_config(
    page_title="SmartCare | Health Information Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# SmartCare is an educational, rule-based information tool.
# It does not diagnose, predict disease, or replace a qualified clinician.

HEALTH_TOPICS = {
    "Cold and cough": {
        "overview": "Colds and coughs can have many causes, including common viral infections, allergies, and irritation. This tool cannot determine the cause.",
        "self_care": [
            "Rest and drink fluids.",
            "Avoid smoke and other irritants.",
            "Consider asking a pharmacist or clinician about suitable symptom relief, especially for children, pregnancy, or existing medical conditions.",
        ],
        "seek_help": "Seek medical advice if symptoms worsen, persist, or you have concerns. Get urgent help for difficulty breathing, blue/grey lips, severe chest pain, confusion, or inability to stay awake."
    },
    "Headache": {
        "overview": "Headaches are common and can have many causes. A symptom selection alone cannot identify the cause.",
        "self_care": [
            "Rest in a quiet place and drink water.",
            "Take a break from screens if they worsen the discomfort.",
            "Ask a qualified clinician or pharmacist before taking medicine if you are unsure what is suitable for you.",
        ],
        "seek_help": "Seek urgent medical help for a sudden, extremely severe headache, a headache after a serious head injury, or headache with weakness, confusion, fainting, fever with a stiff neck, or new vision or speech problems."
    },
    "Fever": {
        "overview": "Fever can occur with infections and other conditions. This tool cannot identify the cause or determine how serious an illness is.",
        "self_care": [
            "Rest and drink fluids.",
            "Monitor how you feel and follow a clinician's advice.",
            "For infants, pregnancy, older adults, or people with serious medical conditions, seek professional advice early.",
        ],
        "seek_help": "Seek urgent help for difficulty breathing, confusion, seizure, severe dehydration, a stiff neck with severe headache, or if someone is difficult to wake. A baby younger than 3 months with a temperature of 38°C or higher needs urgent medical assessment."
    },
    "Stomach discomfort": {
        "overview": "Stomach discomfort can have many causes, from temporary digestive issues to conditions requiring medical attention. This tool cannot tell which applies.",
        "self_care": [
            "Sip fluids if you can keep them down.",
            "Choose simple foods if tolerated and avoid foods that seem to worsen symptoms.",
            "Seek professional advice if discomfort is persistent or worrying.",
        ],
        "seek_help": "Get urgent medical help for severe or worsening abdominal pain, blood in vomit or stool, a hard/swollen abdomen with severe pain, fainting, or repeated vomiting with signs of dehydration."
    },
    "Stress or low mood": {
        "overview": "Stress and low mood can affect sleep, concentration, and daily life. Support from trusted people and qualified professionals can help.",
        "self_care": [
            "Consider a short, gentle activity or a calming breathing exercise if it feels comfortable.",
            "Try to maintain regular meals, sleep, and contact with supportive people.",
            "Consider speaking with a mental health professional if these feelings persist or interfere with daily life.",
        ],
        "seek_help": "If you may hurt yourself or someone else, or cannot keep yourself safe, contact local emergency services or go to the nearest emergency department now. In India, Tele-MANAS offers mental health support at 14416."
    },
}

SYMPTOM_GUIDANCE = {
    "Cough or sore throat": {
        "info": "Cough or sore throat can have several causes. Selecting this symptom cannot establish a diagnosis.",
        "next": "Rest, drink fluids, and seek medical advice if symptoms worsen or persist.",
    },
    "Headache": {
        "info": "Headache has many possible causes; this tool cannot determine the cause.",
        "next": "Rest and hydrate if appropriate. Seek urgent help for sudden severe pain or neurological symptoms.",
    },
    "Fever or feeling hot": {
        "info": "Fever can occur with many illnesses. Your symptoms and medical history matter.",
        "next": "Rest, drink fluids, and monitor your condition. Seek care early for infants or people at higher risk.",
    },
    "Nausea or stomach discomfort": {
        "info": "Digestive symptoms have many possible causes and cannot be diagnosed through this tool.",
        "next": "Take small sips of fluid if tolerated. Seek urgent care for severe pain, blood, fainting, or severe dehydration.",
    },
    "Tiredness": {
        "info": "Tiredness may be associated with sleep, stress, lifestyle, or health conditions.",
        "next": "Consider rest and regular meals. Arrange a medical review if tiredness is persistent, severe, or unexplained.",
    },
    "Skin irritation or rash": {
        "info": "Skin changes can have many causes. A description alone cannot identify the cause.",
        "next": "Avoid suspected irritants. Seek urgent help for swelling of the tongue/throat, breathing difficulty, or a rapidly spreading rash with severe illness.",
    },
}

URGENT_WARNING_SIGNS = [
    "Severe difficulty breathing or choking",
    "Severe chest pain or pressure",
    "Sudden weakness on one side, new speech difficulty, or facial drooping",
    "Unconsciousness, a seizure, or severe confusion",
    "Severe bleeding or a serious injury",
    "Swelling of the tongue or throat, especially with breathing difficulty",
    "Immediate risk of self-harm or inability to stay safe",
]

FAQ = [
    {
        "question": "Can SmartCare diagnose a disease?",
        "answer": "No. SmartCare provides general educational information using predefined rules. It does not diagnose, predict disease, or replace medical assessment."
    },
    {
        "question": "Is my information saved?",
        "answer": "This starter app does not save symptom selections to a database. Avoid entering names, contact details, or other personal health information."
    },
    {
        "question": "What should I do in an emergency?",
        "answer": "Do not rely on this website. Contact local emergency services or go to the nearest emergency department. In India, the pan-India emergency number is 112."
    },
    {
        "question": "Is BMI a diagnosis?",
        "answer": "No. BMI is a screening measure based on height and weight. It does not directly measure body fat or overall health and may not be appropriate for every person."
    },
]

def show_disclaimer():
    st.info(
        "Educational use only — SmartCare does not diagnose or treat medical conditions. "
        "If symptoms are severe, rapidly worsening, or worrying, seek professional medical care. "
        "For an emergency in India, call 112."
    )

st.title("🩺 SmartCare")
st.subheader("Healthcare Information Assistant")
st.write("Explore general health information, preventive-care tips, and guidance on when to seek professional help.")
show_disclaimer()

with st.sidebar:
    st.title("Navigation")
    page = st.radio(
        "Choose a section",
        ["Home", "Symptom Information", "Health Library", "BMI Calculator", "Emergency Guidance", "FAQs"],
    )
    st.divider()
    st.caption("SmartCare • Local rule-based prototype • No paid API required")

if page == "Home":
    st.markdown("### Welcome to SmartCare")
    st.write("A simple healthcare information prototype built with Python and Streamlit.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Health topics", len(HEALTH_TOPICS))
    col2.metric("Symptom categories", len(SYMPTOM_GUIDANCE))
    col3.metric("Paid APIs required", "0")
    st.markdown("### What you can do")
    st.markdown(
        "- **Symptom Information:** read general information and safe next-step guidance.\n"
        "- **Health Library:** browse common topics and self-care information.\n"
        "- **BMI Calculator:** calculate BMI from height and weight.\n"
        "- **Emergency Guidance:** review warning signs that may require urgent care."
    )
    st.markdown("### How it works")
    st.write(
        "The app uses locally stored educational content and simple predefined rules. "
        "It does not use machine learning to diagnose conditions and does not send information to an external API."
    )
    st.caption("Project type: Healthcare website / rule-based information assistant")

elif page == "Symptom Information":
    st.header("Symptom Information")
    st.write("Choose a symptom category to read general information. This is not a diagnosis.")
    selected = st.selectbox("Select the closest category", list(SYMPTOM_GUIDANCE.keys()))
    details = SYMPTOM_GUIDANCE[selected]
    st.markdown("#### General information")
    st.write(details["info"])
    st.markdown("#### General next steps")
    st.write(details["next"])

    st.markdown("#### Are any urgent warning signs present?")
    urgent_selected = st.multiselect(
        "Select any warning signs that apply",
        URGENT_WARNING_SIGNS,
        help="If a severe emergency is happening, do not wait for this app to respond.",
    )
    if urgent_selected:
        st.error(
            "One or more warning signs have been selected. Seek urgent medical help now. "
            "For an emergency in India, call 112. Do not rely on this app to assess severity."
        )
        for item in urgent_selected:
            st.write(f"- {item}")
    else:
        st.caption("No warning signs selected. This does not prove that a condition is safe or non-urgent.")
    st.warning("If symptoms are severe, new, worsening, or concerning, contact a qualified healthcare professional.")

elif page == "Health Library":
    st.header("Health Library")
    topic = st.selectbox("Choose a topic", list(HEALTH_TOPICS.keys()))
    item = HEALTH_TOPICS[topic]
    st.markdown("#### Overview")
    st.write(item["overview"])
    st.markdown("#### General self-care information")
    for tip in item["self_care"]:
        st.markdown(f"- {tip}")
    st.markdown("#### When to seek help")
    st.write(item["seek_help"])
    st.caption("Information is general and may not apply to every person. A qualified clinician can provide advice tailored to you.")

elif page == "BMI Calculator":
    st.header("BMI Calculator")
    st.write("Enter height and weight to calculate Body Mass Index. You do not need to enter your name.")
    col1, col2 = st.columns(2)
    with col1:
        height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.5)
    with col2:
        weight_kg = st.number_input("Weight (kg)", min_value=10.0, max_value=400.0, value=65.0, step=0.5)

    if st.button("Calculate BMI", type="primary"):
        height_m = height_cm / 100
        bmi = weight_kg / (height_m * height_m)
        st.metric("Your BMI", f"{bmi:.1f}")
        if bmi < 18.5:
            category = "Below the standard adult reference range"
        elif bmi < 25:
            category = "Within the standard adult reference range"
        elif bmi < 30:
            category = "Above the standard adult reference range"
        else:
            category = "Higher than the standard adult reference range"
        st.write(f"**Reference category:** {category}")
        st.caption(
            "These broad adult categories are not a diagnosis. BMI interpretation differs for children and teens, "
            "pregnancy, some older adults, athletes, and other circumstances. Discuss concerns with a clinician."
        )
    st.markdown("Formula: BMI = weight in kilograms ÷ (height in metres × height in metres).")

elif page == "Emergency Guidance":
    st.header("Emergency Guidance")
    st.error("If someone may be experiencing a medical emergency, call local emergency services immediately.")
    st.markdown("### Warning signs that may need urgent help")
    for sign in URGENT_WARNING_SIGNS:
        st.markdown(f"- {sign}")
    st.markdown("### What to do")
    st.markdown(
        "1. Contact emergency services or go to the nearest emergency department.\n"
        "2. Follow instructions from the emergency dispatcher or qualified healthcare staff.\n"
        "3. Do not delay urgent care to use this website."
    )
    st.markdown("**India emergency number: 112**")
    st.caption("This list is not exhaustive. Use your judgement and seek help if you are concerned.")

elif page == "FAQs":
    st.header("Frequently Asked Questions")
    for entry in FAQ:
        with st.expander(entry["question"]):
            st.write(entry["answer"])

st.divider()
st.caption("SmartCare is a student prototype for educational purposes. Content should be reviewed by qualified healthcare professionals before real-world deployment.")
