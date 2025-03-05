import os
from dotenv import load_dotenv
import openai
import streamlit as st  # ✅ Ensure Streamlit is imported

# Load environment variables
load_dotenv()

# Retrieve the API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

# Title of the app
st.title('MissionSync: Aligning AI with Organizational Values')

st.markdown("""
### **MissionSync: Aligning AI with Organizational Values**

**MissionSync** is a dynamic tool designed to leverage **Gen AI** to align user queries with the mission and values of an organization. By integrating **OpenAI's GPT-4o Mini** model, this app takes organizational missions and applies them to modify and enhance user inquiries, ensuring that the answers reflect the core principles of the organization.""")

# Suggest sample questions but allow users to enter their own query
st.markdown("""
### *Sample Questions (Suggested):*

Here are a few example questions you might try:

- *What role does education play in preparing students for their future careers, and how should a university approach this responsibility?*
- *What role does diversity play in a university's educational approach, and how should diversity be managed in the academic environment?*
- *What responsibility does the university hold in correcting historical wrongdoings, such as racial discrimination and the legacies of slavery?*

            Note: Responses may take 10-30 seconds to generate
""", unsafe_allow_html=True)

# User input field for the query (allowing free text input)
query = st.text_input('Enter your query here:')

# Define organizational values and missions
org_a_mission = """
We are committed to training students in the context of a Biblical worldview, 
with an emphasis on the inerrancy and sufficiency of Scripture. Our educational philosophy integrates the 
study of truth, culture, and the divine mandate to glorify God in all we do. We aim to prepare students for 
life and service in God's kingdom, providing them with academic excellence, spiritual development, and a 
Christ-centered worldview.
"""

org_b_mission = """
We are dedicated to fostering global citizens who are committed to creating a 
better society. Our educational approach encourages critical thinking, intellectual growth, and a 
commitment to social justice. We emphasize the development of the whole person—mind, body, and spirit— 
through academic rigor, community service, and a deep respect for human dignity. Our core values are rooted 
in peace, sustainability, and the development of compassionate, visionary leaders who can work for a better 
world.
"""

# Modify query based on organizational values
if query:
    # Modify the query based on each organization's mission
    prompt_a = f"{org_a_mission} Modify the following query based on the organizational values of Organization A: {query}"
    prompt_b = f"{org_b_mission} Modify the following query based on the organizational values of Organization B: {query}"

    # Function to get AI response using OpenAI API
    def get_ai_response(prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # Specify the model you want to use
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},  # System message
                    {"role": "user", "content": prompt}  # User's input prompt
                ],
                max_tokens=1000  # Limit the response to 1000 tokens
            )
            return response['choices'][0]['message']['content'].strip()
        except openai.error.OpenAIError as e:
            st.write(f"Error during API call: {e}")
            return f"Error: {e}"

    # Get responses for both modified prompts (These are prompt_a and prompt_b)
    response_a = get_ai_response(prompt_a)
    response_b = get_ai_response(prompt_b)

    # Now use response_a and response_b as new prompts to get response_c and response_d
    response_c = get_ai_response(response_a)  # Use response_a as a new prompt (modified query)
    response_d = get_ai_response(response_b)  # Use response_b as a new prompt (modified query)

    # Log the responses for debugging (you can remove this if you don't need to log it)
    # st.write(f"Response A: {response_a}")
    # st.write(f"Response B: {response_b}")
    # st.write(f"Response C: {response_c}")
    # st.write(f"Response D: {response_d}")

    # Display the responses side-by-side using Streamlit's columns
    col1, col2 = st.columns(2)

    # Display response_c in col1 (linked to Organization A)
    with col1:
        st.subheader("Response for Southern Christian Liberal Arts College:")
        st.write(response_c)  # Displaying response_c below response_a

    # Display response_d in col2 (linked to Organization B)
    with col2:
        st.subheader("Response for West Coast Cosmopolitan Liberal Arts College:")
        st.write(response_d)  # Displaying response_d below response_b

# break
st.markdown("---")

# Explanation with blue font and correct styles
st.markdown("""
    <style>
        .blue-text {
            color: blue;
            font-family: Arial, sans-serif;
        }
    </style>

    <div class="blue-text">
        <h3><em>How MissionSync Works:</em></h3>
        <ol>
            <li><em>User Input:</em>
                <ul>
                    <li>The app allows the user to enter a query (e.g., "What role does education play in preparing students for their future careers?").</li>
                </ul>
            </li>
            <li><em>Query Modification Based on Organizational Values:</em>
                <ul>
                    <li>The app modifies the user's query based on the <em>organizational values</em> embedded in the mission statements of two different organizations (e.g., a university with a <em>Biblical worldview</em> or a university focused on <em>social justice</em> and <em>global citizenship</em>).</li>
                </ul>
            </li>
            <li><em>AI Response Generation:</em>
                <ul>
                    <li>These modified queries are sent to OpenAI's GPT-4o Mini model to generate tailored responses.</li>
                    <li>The responses reflect how each organization would approach and answer the query based on their respective missions.</li>
                </ul>
            </li>
            <li><em>Displaying Results:</em>
                <ul>
                    <li>The app displays the responses side by side, illustrating how each organization's values influence its answers.</li>
                </ul>
            </li>
            <li><em>Purpose:</em>
                <ul>
                    <li>The purpose of <strong>MissionSync</strong> isis to demonstrate how AI can align with organizational values and how those values can shape responses to queries.</li>
                </ul>
            </li>
            <li><em>Applications:</em>
                <ul>
                    <li><strong>Educational Institutions:</strong> Align responses with the institution's educational philosophy, worldview, and core values.</li>
                    <li><strong>Corporate Social Responsibility (CSR):</strong> Ensure that responses reflect a company's ethical stance or sustainability mission.</li>
                    <li><strong>Nonprofits and NGOs:</strong> Align responses related to social issues, diversity, and community development with the organization's mission and goals.</li>
                </ul>
        </ol>
    </div>
""", unsafe_allow_html=True)

