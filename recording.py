import streamlit as st
import time  # To introduce a slight delay

# Initialize session state to keep track of the sections
if 'sections' not in st.session_state:
    st.session_state.sections = [
        {"title": "Clinical Records", "content": """
        <div class="scrollable-content">
            <ul>
                <li><strong>Homebound Status:</strong>
                    <ul>
                        <li>Justify and mention AD type and level of assistance.</li>
                    </ul>
                </li>
                <li><strong>Living Arrangements:</strong>
                    <ul>
                        <li>Home Safety: Evaluate the safety of the living environment, including the need for adaptive equipment or modifications.</li>
                        <li>Support System: Document available family, friends, and community resources supporting the patient's care.</li>
                        <li>Hazards: May include stairs, cluttered/soiled areas, pets, narrow paths, fire equipment, poor handling, tubing (02, Foley).</li>
                    </ul>
                </li>
                <li><strong>Immunizations:</strong>
                    <ul>
                        <li>List received immunizations and dates:</li>
                        <ol>
                            <li>Pneumonia</li>
                            <li>Flu</li>
                            <li>Tetanus</li>
                            <li>TB</li>
                            <li>Hep B</li>
                            <li>COVID</li>
                        </ol>
                    </ul>
                </li>
            </ul>
        </div>"""},
        
        {"title": "BIMS Summary Score", "content": """
        <div class="scrollable-item">
            <div class="scrollable-content">
                <h3>BIMS Summary Score</h3>
                <p>Repetition of Three Words: Sock, Blue, Bed</p>
                <p>Ask the patient to repeat the words. You can repeat the words up to two more times.</p>
                <ul>
                    <li><strong>Scoring:</strong>
                        <ul>
                            <li>0 Points = No Word</li>
                            <li>1 Point = One Word</li>
                            <li>2 Points = Two Words</li>
                            <li>3 Points = Three Words</li>
                        </ul>
                    </li>
                    <li><strong>Temporal Orientation Year: What year is it right now?</strong>
                        <ul>
                            <li>0 points: Off by 5+ years or no answer</li>
                            <li>1 point: Off by 2-5 years</li>
                            <li>2 points: Off by 1 year</li>
                            <li>3 points: Correct year</li>
                        </ul>
                    </li>
                    <li><strong>Temporal Orientation Month: What month are we in right now?</strong>
                        <ul>
                            <li>0 points: Off by more than one month or no answer.</li>
                            <li>1 point: Off by 6 days to 1 month.</li>
                            <li>2 points: Accurate within 5 days.</li>
                        </ul>
                    </li>
                    <li><strong>Temporal Orientation Day: What day of the week is today?</strong>
                        <ul>
                            <li>0 points: Incorrect or no answer.</li>
                            <li>1 point: Correct.</li>
                        </ul>
                    </li>
                    <li><strong>Recall:</strong>
                        <ul>
                            <li>Ask the patient to recall the three words mentioned earlier (sock, blue, bed).</li>
                        </ul>
                    </li>
                    <li><strong>Scoring:</strong>
                        <ul>
                            <li>0 points: Cannot recall the word.</li>
                            <li>1 point: Recalls after cueing.</li>
                            <li>2 points: Recalls without cueing.</li>
                        </ul>
                    </li>
                    <li><strong>BIMS Summary Score</strong>
                        <ul>
                            <li>Add the scores from the above sections (0-15).</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        """},

        {"title": "CAMS", "content": """
        <div class="scrollable-item">
            <div class="scrollable-content">
                <h3>CAMS</h3>
                <p>CAM: Signs and Symptoms of Delirium</p>
                <ul>
                    <li><strong>Acute onset of Mental Status Change:</strong>
                        <ul>
                            <li>0: No</li>
                            <li>1: Yes</li>
                            <li>Not Assessed/No Information</li>
                        </ul>
                    </li>
                    <li><strong>Inattention:</strong>
                        <ul>
                            <li>Did the patient have difficulty focusing attention, e.g., being easily distractible or having difficulty keeping track of what was being said?</li>
                        </ul>
                    </li>
                    <li><strong>Scale:</strong>
                        <ul>
                            <li>0: Behavior not present</li>
                            <li>1: Behavior continuously present, does not fluctuate</li>
                            <li>2: Behavior present, fluctuates (comes and goes, changes in severity)</li>
                            <li>3: Not Assessed/No Information</li>
                        </ul>
                    </li>
                    <li><strong>Disorganized Thinking:</strong>
                        <ul>
                            <li>Was the patient's thinking disorganized or incoherent (rambling or irrelevant conversation, unclear or illogical flow of ideas, unpredictable switching)?</li>
                            <li>Answer 0, 1, 2 or 3</li>
                        </ul>
                    </li>
                    <li><strong>Altered Level of Consciousness:</strong>
                        <ul>
                            <li>Did the patient have an altered level of consciousness, as indicated by:</li>
                            <li>Vigilant: Startled easily</li>
                            <li>Lethargic: Repeatedly dozed off when asked questions, but responded to voice or touch</li>
                            <li>Stuporous: Very difficult to arouse and keep aroused for the interview</li>
                            <li>Comatose: Could not be aroused</li>
                            <li>Answer 0, 1, 2 or 3</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        """},

        {"title": "PHQ", "content": """
        <div class="scrollable-item">
            <div class="scrollable-content">
                <h3>PHQ</h3>
                <p>Patient Health Questionnaire (PHQ-2 & PHQ-9)</p>
                <ul>
                    <ol>
                        <li>During the past two weeks, have you often been bothered by little interest or pleasure in doing things? (Yes/No)</li>
                        <li>During the past two weeks, have you often been bothered by feeling down, depressed, or hopeless? (Yes/No)</li>
                    </ol>
                </ul>
            </div>
        </div>
        """},

        {"title": "Physical Assessment", "content": """
        <div class="scrollable-item">
            <div class="scrollable-content">
                <h3>Physical Assessment</h3>
                <ul>
                    <li><strong>Vital Signs:</strong>
                        <ul>
                            <li>Blood pressure, pulse, respiration, SPO2, temperature</li>
                            <li>Pain Level: (1-10 scale, site, duration, what makes it worse/better, medication use, effectiveness)</li>
                        </ul>
                    </li>
                    <li><strong>Height and Weight</strong></li>
                    <li><strong>Neurological Assessment:</strong>
                        <ul>
                            <li>Evaluate mental status, orientation, and ability to understand/follow directions - any comments in addition to BIMS, CAM, and PHQ</li>
                        </ul>
                    </li>
                    <li><strong>Cardiopulmonary Status:</strong>
                        <ul>
                            <li>Assess: Heart, lungs, respiratory rate, rhythm</li>
                            <li>DOE: Severity rating/Oxygen use/Leg edema</li>
                        </ul>
                    </li>
                    <li><strong>Integumentary Assessment:</strong>
                        <ul>
                            <li>Inspect skin for wounds, surgical sites, pressure ulcers</li>
                            <li>Complete Wound Care Worksheet for all open wounds</li>
                        </ul>
                    </li>
                    <li><strong>Endocrine:</strong>
                        <ul>
                            <li>DM: Yes/No. If Yes, include insulin (Yes/No), oral meds (Yes/No), RBS #</li>
                        </ul>
                    </li>
                    <li><strong>Elimination Status:</strong>
                        <ul>
                            <li>Recent UTI, incontinence (Bowel and/or Bladder)</li>
                            <li>Catheter: Yes/No (if Yes, provide care details)</li>
                            <li>Ostomy: Yes/No (if Yes, provide care details)</li>
                            <li>Any other symptoms noted</li>
                        </ul>
                    </li>
                    <li><strong>Nutrition:</strong>
                        <ul>
                            <li>Ordered Diet, Appetite</li>
                        </ul>
                    </li>
                    <li><strong>Mobility and Strength:</strong>
                        <ul>
                            <li>Evaluate the ability to move independently or with assistance</li>
                            <li>Assistive Devices: Mention with /without assistance</li>
                            <li>Activities permitted</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        """},

        {"title": "Range of Motion, Special Treatments & Service Requested", "content": """
        <div class="scrollable-item">
            <div class="scrollable-content">
                <h3>Range of Motion, Special Treatments & Service Requested</h3>
                <ul>
                    <li><strong>ROM/Strength:</strong>
                        <ul>
                            <li>Example-MMT BUE and BLE grossly 3+/5. L side weaker than R. ROM of extremities WFL</li>
                        </ul>
                    </li>
                    <li><strong>Additional Comments:</strong>
                        <ul>
                            <li>Example-paralysis, weakness, unsteady gait, antalgic gait, balance defect, limited ROM, fall risk</li>
                        </ul>
                    </li>
                    <li><strong>Special Treatments</strong>
                        <ul>
                            <li>Respiratory Therapies</li>
                            <li>IV Medications / .IV Access: PICC lines (Yes/No)</li>
                            <li>Dialysis: (Yes/No)</li>
                        </ul>
                    </li>
                    <li><strong>Service requested for the following disciplines along with the frequency</strong>
                        <ul>
                            <li>SN / PT / OT / HHA / MSW / ST</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        """},

        {"title": "Clinical Summary & Medical Supplies Needed", "content": """
        <div class="scrollable-item">
            <div class="scrollable-content">
                <h3>Clinical Summary & Medical Supplies Needed</h3>
                <ul>
                    <li><strong>Clinical Summary:</strong>
                        <ul>
                            <li>State the skills need for Home Health Services</li>
                            <li>Spoke with ____@ Dr. ____office on ____</li>
                            <li>If there are any additional SOC findings not noted above in the systems review, add that here.</li>
                        </ul>
                    </li>
                    <li><strong>Medical Supplies Needed:</strong>
                        <ul>
                            <li>List any supplies needed to carry out Patient care</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        """},

        {"title": "Goals and Interventions", "content": """
        <div class="scrollable-item">
            <div class="scrollable-content">
                <h3>Goals and Interventions</h3>
                <p>What other Goals & Interventions besides the required high-risk medications, hospitalization risk, fall/home safety, emergency disaster planning, and review of systems are needed? See examples below:</p>
                <ul>
                    <li><strong>DM</strong></li>
                    <li><strong>Skin: wound care: location specific with treatment plan (freq and dressing should be matched with mentioned in WC sheet)</strong></li>
                    <li><strong>Symptoms (Pain, issues with vital signs, etc.): pain G/I</strong></li>
                    <li><strong>Picc line G/I for CT (only to assess site for S/S of infection and arm circumference)</strong></li>
                    <li><strong>Ostomy G/I</strong></li>
                    <li><strong>Catheter use G/I</strong></li>
                    <li><strong>Lab orders G/I</strong></li>
                    <li><strong>Skin breakdown/pressure relieving G/I in WC/BEDBOUND</strong></li>
                    <li><strong>Infections G/I</strong></li>
                    <li><strong>Therapy G/I</strong></li>
                    <li><strong>Any other G/I you want added to POC</strong></li>
                </ul>
            </div>
        </div>
        """},

    ]
    st.session_state.current_index = 0

def next_section():
    if st.session_state.current_index < len(st.session_state.sections) - 1:
        st.session_state.current_index += 1
        time.sleep(0.1)  # Introduce a slight delay
        st.experimental_rerun()  # Force a rerun to update the UI

def prev_section():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        time.sleep(0.1)  # Introduce a slight delay
        st.experimental_rerun()  # Force a rerun to update the UI

# Define the HTML content with CSS and JavaScript for scrollable sections
scrollable_content = f"""
  <style>
  .scrollable-container {{
    display: flex;
    overflow: hidden;
    width: 350px; /* Adjust to the width of one section */
    height: 400px; /* Adjust to the height of one section */
    position: relative;
  }}
  
  .scrollable-item {{
    min-width: 100%;
    max-width: 100%; /* Ensure items don't exceed container width */
    height: 100%;
    transition: transform 0.5s ease-in-out; /* Smooth transition for sliding effect */
    position: absolute;
    top: 0;
    left: 0;
  }}
  
  .scrollable-content {{
    background-color: #f0f0f0;
    padding: 10px;
    border-radius: 5px;
    box-sizing: border-box; /* Include padding and border in the element's total width and height */
    height: 100%;
    margin-right: 10px; /* Adjust margin between items */
    overflow-y: auto; /* Enable vertical scrolling */
  }}
  </style>
  
  <div class="scrollable-container" id="scroll-container">
    {" ".join([f'''
    <div class="scrollable-item" id="item-{i}" style="transform: translateX({100 * (i - st.session_state.current_index)}%);">
      <div class="scrollable-content">
        <h3>{section['title']}</h3>
        <div>{section['content']}</div>
      </div>
    </div>
    ''' for i, section in enumerate(st.session_state.sections)])}
  </div>
  
  <script>
  function updateItems() {{
    var currentIndex = {st.session_state.current_index};
    var items = document.getElementsByClassName('scrollable-item');
    for (var i = 0; i < items.length; i++) {{
      items[i].style.transform = 'translateX(' + (100 * (i - currentIndex)) + '%)';
    }}
  }}
  setTimeout(updateItems, 100);  // Ensure updateItems is called after a slight delay
  </script>
"""

# Render the scrollable content using st.markdown
st.markdown(scrollable_content, unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.write("")  # Placeholder to enforce button on the left side
    if st.button("Previous <"):
        prev_section()

with col2:
    st.write("")  # Placeholder to enforce button on the right side
    if st.button("Next >"):
        next_section()

st.write('''<style>
    [data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
    [data-testid="column"]:first-child {
    margin-right: 141px; /* Adjust the margin-right to increase or decrease the space between columns */
}
</style>''', unsafe_allow_html=True)
