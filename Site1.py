import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import folium
import pydeck as pdk
import plotly.express as px
import openpyxl

st.set_page_config(layout="wide")

# Define functions for each page
def home():
   
    st.markdown("<h1 style='text-align: center;'>Welcome!</h1>", unsafe_allow_html=True)
    username = st.text_input("Please enter your Name:")
    if username:
        st.session_state.username = username
        cybersecurity_description = """
        <p style='text-align: Center; font-size: 18px;'>
        <i>Welcome to our website dedicated to CyberSecurity education! 🌟
        <br>Explore real-life case studies and captivating videos to deepen
        your understanding of CyberSecurity dilemmas. 
        <br>Test your knowledge with
          interactive quizzes on every page, and track your progress with
           the cumulative score displayed in the sidebar.
        <br>Join us on a journey of critical thinking and reflection.
         Let's navigate the complexities of today's world together, armed with
          knowledge and amazing insight. Welcome! 🚀</i>
    </p>
    """
        st.balloons()
        st.markdown(f"<h4 style='text-align: center;'>Hello {username}!</h1>", unsafe_allow_html=True)
        st.markdown(f"{cybersecurity_description}" ,unsafe_allow_html=True)
    

##############################################################  WHAT IS CyberSecurity ###################################################################

def what_is_cybersecurity():
    

    st.markdown("<h2 style='text-align: center;'>What is <span style='color:#336699;'>Cybersecurity</span>?</h2>", unsafe_allow_html=True)
    cybersecurity_description = """
        <p style='text-align: justify; font-size: 18px;'>
        "<i>Cybersecurity is the practice of protecting computer systems,
        networks, and data from digital attacks. It encompasses a range of
        technologies, processes, and practices designed to safeguard against
        unauthorized access, data breaches, identity theft, and other cyber 
        threats. The importance of cybersecurity has grown exponentially as 
        our reliance on digital technology has increased.</i>"
    </p>
    """
    st.markdown(cybersecurity_description, unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")
    st.write("   ")

    

    # Define column widths
    column_widths = [10,1,10]  # Column 1 will be twice as wide as Column 2

    # Create columns with specified widths
    col1, col2 , col3 = st.columns(column_widths)

    with col1:

        st.markdown("<h3 style='text-align: center;'>Importance of <span style='color: #336699;'>Cybersecurity</span></h3>", unsafe_allow_html=True)
        Importance = """
            <p style='text-align: justify; font-size: 17px;'>
            <br><br><span style='color: #336699;'><strong>Protecting Data:</strong></span></h3> With the digitalization of personal, financial, and organizational data, cybersecurity is essential for safeguarding sensitive information from theft or manipulation.
            <br><br><span style='color: #336699;'><strong>Preserving Privacy:</strong></span></h3> Individuals and organizations have a right to privacy, and cybersecurity measures help ensure that personal and proprietary information remains confidential.
            <br><br><span style='color: #336699;'><strong>Maintaining Trust:</strong></span></h3> Trust is fundamental in digital interactions. Effective cybersecurity practices build trust among users, customers, and partners by demonstrating a commitment to protecting their data and privacy.
            <br><br><span style='color: #336699;'><strong>Safeguarding Infrastructure:</strong></span></h3> Critical infrastructure, such as power grids, transportation systems, and healthcare facilities, relies on interconnected digital systems. Cybersecurity is crucial for protecting these systems from disruption and damage.
            <br><br><span style='color: #336699;'><strong>Preventing Financial Loss:</strong></span></h3> Cyberattacks can result in significant financial losses for individuals and organizations through theft, fraud, or disruption of operations. Strong cybersecurity measures can help mitigate these risks.
        </p>
        """

        st.markdown(Importance, unsafe_allow_html=True)

    with col3:
        st.markdown("<h3 style='text-align: center;'>Evolution of <span style='color: #336699;'>Cyber Threats</span></h3>", unsafe_allow_html=True)
        Evolution = """
            <p style='text-align: justify; font-size: 17px;'>
            <br><br><span style='color: #336699;'><strong>Traditional Threats:</strong></span></h3> In the early days of computing, cyber threats were often limited to viruses, worms, and other forms of malware spread through infected files or networks. These threats primarily targeted individual devices or networks.
            <br><br><span style='color: #336699;'><strong>Sophisticated Attacks:</strong></span></h3> As technology advanced, so did cyber threats. Today, cybercriminals employ sophisticated techniques such as phishing, ransomware, and social engineering to exploit human vulnerabilities and gain unauthorized access to systems and data.
            <br><br><span style='color: #336699;'><strong>Nation-State Actors:</strong></span></h3> Governments and state-sponsored groups engage in cyber espionage, sabotage, and warfare to steal sensitive information, disrupt infrastructure, or achieve geopolitical objectives. These attacks can have far-reaching consequences for national security and international relations.
            <br><br><span style='color: #336699;'><strong>Emerging Threats:</strong></span></h3> As new technologies like artificial intelligence (AI), Internet of Things (IoT), and cloud computing proliferate, so do the risks associated with them. Cyber threats are constantly evolving, requiring ongoing vigilance and adaptation to stay ahead of adversaries.
        </p>
        """
        st.markdown(Evolution, unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")

    st.markdown("<h3 style='text-align: center;'><span style='color: #336699;'>Cyber Security</span></h3>", unsafe_allow_html=True)

    video_url = 'https://www.youtube.com/embed/inWWhr5tnEA'
    video_html = f'<div style="display: flex; justify-content: center;"><iframe width="640" height="360" src="{video_url}" frameborder="0" allowfullscreen></iframe></div>'
    st.markdown(video_html, unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")
    st.markdown("Explor Further: https://www.techtarget.com/searchsecurity/definition/cybersecurity#:~:text=Cybersecurity%20is%20the%20practice%20of,centers%20and%20other%20computerized%20systems.", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write("   ")

    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h4>", unsafe_allow_html=True)

    questions = [
    {
        "question": "What is the primary focus of cybersecurity?",
        "options": [" Protecting computer systems, networks, and data from digital attacks ", "Ensuring the privacy of individuals and organizations", "Safeguarding critical infrastructure", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Which type of cyber threat has evolved from traditional malware to more sophisticated techniques like phishing and social engineering?",
        "options": ["Traditional threats", "Sophisticated attacks", "Nation-state actors", "Emerging threats"],
        "answer": "Sophisticated attacks"
    },
    {
        "question": "Which of the following is NOT a key reason for the importance of cybersecurity",
        "options": ["Protecting sensitive data", "Maintaining transparency in digital interactions", "Preventing financial loss", "Eliminating the need for privacy"],
        "answer": "Eliminating the need for privacy"
    },
    {
        "question": "Which of the following is an example of a nation-state actor engaging in cyber-related activities?",
        "options": ["Stealing sensitive information", "Disrupting critical infrastructure", "Achieving geopolitical objectives", "All of the above "],
        "answer": "All of the above "
    },
    {
        "question": "How have the advancements in technologies like AI and IoT impacted the evolution of cyber threats?",
        "options": ["They have reduced the risks associated with cybersecurity", "They have not had a significant impact on cyber threats", "They have led to the emergence of new cyber threats", "They have made cybersecurity a less important concern"],
        "answer": "They have led to the emergence of new cyber threats"
    }
 ]

    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken' not in st.session_state:
            st.session_state['quiz_taken'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Foundations of Cybersecurity in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")
        

##############################################################  Cyber Security ###################################################################

def foundations_of_cybersecurity():
    

    st.markdown("<h2 style='text-align: center;'>Foundations of <span style='color: #336699;'>Cybersecurity</span></h2>", unsafe_allow_html=True)

    

    foundations_of_cybersecurity = """
        <p style='text-align: justify; font-size: 17px;'>
        <strong>Introduction:</strong> The core principles of cybersecurity focus on protecting systems, networks, and data from digital attacks and unauthorized access.
    <br><br>Firstly, let's talk about privacy. It's like protecting someone's secret diary; you wouldn't want it to fall into the wrong hands. Similarly, in data analytics, we must safeguard personal information and follow the rules laid out by privacy laws.
    </p>
    """

    st.markdown(foundations_of_cybersecurity, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("<h2 style='text-align: center;'>Principles of <span style='color: #336699;'>Cybersecurity</span></h2>", unsafe_allow_html=True)

    st.write("")

    col1,col2,col3 = st.columns([2,5,2])

    with col2:
        st.image("principles.png", use_column_width=True)

    principles = """
        <p style='text-align: justify; font-size: 17px;'>
        <strong><span style='color: #336699;'>Confidentiality:</span></strong>  Ensuring that sensitive information is accessible only to authorized individuals or entities. This involves measures such as encryption, access controls, and data classification.
    <br><br><strong><span style='color: #336699;'>Integrity:</span></strong>  Guaranteeing the accuracy and trustworthiness of data and systems. Integrity controls detect and prevent unauthorized modifications, alterations, or deletions of data.
    <br><br><strong><span style='color: #336699;'>Availability:</span></strong>  Ensuring that information and resources are accessible and usable when needed. This involves measures to prevent and mitigate disruptions, such as redundancy, backups, and disaster recovery planning.
    <br><br><strong><span style='color: #336699;'>Authentication:</span></strong>  Verifying the identity of users, systems, and devices to ensure that only authorized entities are granted access to resources. Authentication mechanisms include passwords, biometrics, and multi-factor authentication.
    <br><br><strong><span style='color: #336699;'>Authorization:</span></strong>  Granting or restricting access to resources based on the permissions assigned to individual users or roles. Authorization controls enforce the principle of least privilege, ensuring that users have access only to the resources necessary to perform their tasks.
    <br><br><strong><span style='color: #336699;'>Non-repudiation:</span></strong>  Ensuring that the origin and integrity of digital transactions or communications cannot be denied by the parties involved. Non-repudiation mechanisms, such as digital signatures and audit trails, provide evidence of actions taken.
    </p>
        """
    st.markdown(principles, unsafe_allow_html=True)

    st.write("")
    st.write("")
    
    
    st.markdown("<h2 style='text-align: center;'>Frameworks and Standards related to <span style='color: #336699;'>Cybersecurity</span></h2>", unsafe_allow_html=True)
    frameworks = """
        <p style='text-align: justify; font-size: 17px;'>
        <strong><span style='color: #336699;'>NIST Cybersecurity Framework:</span></strong>  Developed by the National Institute of Standards and Technology (NIST), this framework provides guidance for organizations to assess and improve their cybersecurity posture. It consists of five core functions: Identify, Protect, Detect, Respond, and Recover.
    <br><br><strong><span style='color: #336699;'>ISO/IEC 27001:</span></strong>  This international standard outlines requirements for establishing, implementing, maintaining, and continuously improving an information security management system (ISMS). It provides a systematic approach to managing sensitive information and mitigating security risks.
    <br><br><strong><span style='color: #336699;'>PCI DSS:</span></strong>  The Payment Card Industry Data Security Standard (PCI DSS) is a set of security standards designed to ensure the secure processing, storage, and transmission of credit card data. It applies to organizations that handle payment card transactions.
    <br><br><strong><span style='color: #336699;'>COBIT:</span></strong>  Control Objectives for Information and Related Technologies (COBIT) is a framework developed by ISACA for governing and managing enterprise IT. It provides guidelines and best practices for aligning IT with business objectives, including cybersecurity.
    <br><br><strong><span style='color: #336699;'>CIS Controls::</span></strong>  The Center for Internet Security (CIS) Controls is a set of best practices for securing IT systems and data. It consists of 20 controls organized into three categories: Basic, Foundational, and Organizational. These controls help organizations prioritize and implement effective cybersecurity measures.
    </p>
        """
    
    st.markdown(frameworks, unsafe_allow_html=True)
    
    data = {
        'country': ['United States', 'European Union', 'United Kingdom', 'Australia', 'China', 'Russia', 'Bangladesh', 'Singapore', 'South Korea', 'Mexico', 'Philippines', 'India'],

        'law': ['Cybersecurity Information Sharing Act (CISA)', 'Network and Information Security (NIS) Directive', 'National Cyber Security Strategy', 'Notifiable Data Breaches (NDB) Scheme', 'Cybersecurity Law of the Peoples Republic of China', 'Cybersecurity Law of 2017', 'Digital Security Act', 'Cybersecurity Act', 'Cyber Security Law', 'Cybersecurity Law (Ley de Ciberseguridad)', 'Cybercrime Prevention Act', 'Information Technology (IT) Act'],

        'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Values for coloring countries
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Streamlit app
    st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>CyberSecurity Laws</span> Across Countries</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 10, 1])

    with col2:
        # Select theme
        st.markdown("""
        <style>
            body {
                color: white;
                background-color: #0E1117;
            }
        </style>
        """, unsafe_allow_html=True)

        fig = px.choropleth(df, 
                        locations="country", 
                        color="value",
                        hover_name="country",
                        hover_data={"value": False, "law": True},
                        locationmode='country names',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        labels={'law': 'Law'},
                        template='plotly_dark')

        fig.update_layout(
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font=dict(
                color="white"
            ),
            geo=dict(
                showframe=False,  # Hide frame around map
                projection_type='natural earth'  # Choose projection
            ),
            coloraxis_colorbar=dict(
                title="",
                tickvals=[]  # Hide tick values
            )
        )

        st.plotly_chart(fig)
        
    st.write("   ")
    st.write("   ")    
    st.markdown("Explore Further: https://www.knowledgehut.com/blog/security/principles-of-cyber-security", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")

    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)

    questions = [
    {
    "question": "Which of the following is NOT a core principle of cybersecurity?",
    "options": [
    "Confidentiality",
    "Integrity",
    "Availability",
    "Profitability"
    ],
    "answer": "Profitability"
    },
    {
    "question": "Which cybersecurity framework provides guidance for organizations to assess and improve their cybersecurity posture?",
    "options": [
    "ISO/IEC 27001",
    "PCI DSS",
    "COBIT",
    "NIST Cybersecurity Framework"
    ],
    "answer": "NIST Cybersecurity Framework"
    },
    {
    "question": "Which country has implemented the 'Cybersecurity Law of the People's Republic of China'?",
    "options": [
    "United States",
    "European Union",
    "China",
    "Russia"
    ],
    "answer": "China"
    },
    {
    "question": "Which cybersecurity standard outlines requirements for establishing, implementing, and maintaining an information security management system?",
    "options": [
    "NIST Cybersecurity Framework",
    "CIS Controls",
    "ISO/IEC 27001",
    "PCI DSS"
    ],
    "answer": "ISO/IEC 27001"
    },
    {
    "question": "Which country has implemented the 'Cybersecurity Act' as part of its cybersecurity legislation?",
    "options": [
    "United Kingdom",
    "Singapore",
    "Australia",
    "India"
    ],
    "answer": "Singapore"
    }
    ]


    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken2' not in st.session_state:
            st.session_state['quiz_taken2'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken2:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Data Privacy in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken2 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")


##############################################################  DATA PRIVACY ###################################################################


def cyber_threats():
    

    st.markdown("<h2 style='text-align: Center;'>What is a <span style='color: #336699;'>Cyber Threats</span> ?</h2>", unsafe_allow_html=True)

    cyber_threats = """
        <p style='text-align: justify; font-size: 17px;'>
        <span style='color: #336699;'><strong>Cyber Threats</span></strong> refer to any malicious activities or attacks targeting digital systems, networks, and data. These threats can come from a variety of sources, including cybercriminals, nation-states, hacktivists, and even insiders.
    </p>
    """

    st.markdown(cyber_threats, unsafe_allow_html=True)

    

    st.write("")
    st.write("")
    st.write("")

    st.markdown("<h3 style='text-align: Center;'>Types of Cyber Threats</h3>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    col1,col2,col3 = st.columns([2,10,2])

    with col2:
        st.image("types.png", use_column_width=True)

    importance = """
        <p style='text-align: justify; font-size: 17px;'>
    <br><strong><span style='color: #336699;'>Malware:</span></strong> Malicious software designed to damage or disrupt systems, steal data, or gain unauthorized access. Examples include viruses, worms, trojans, ransomware, and spyware.
    <br><br><strong><span style='color: #336699;'>Phishing:</span></strong> Fraudulent attempts to obtain sensitive information, such as usernames, passwords, and financial details, by posing as a trustworthy entity in electronic communication. Phishing attacks often use email, social media, or text messages to deceive victims.
    <br><br><strong><span style='color: #336699;'>Denial of Service (DoS) / Distributed Denial of Service (DDoS):</span></strong> Attacks that aim to disrupt or overload a network, server, or service, making it unavailable to legitimate users. DoS attacks involve a single source, while DDoS attacks use multiple compromised devices (botnets) to amplify the impact.
    <br><br><strong><span style='color: #336699;'>Man-in-the-Middle (MitM):</span></strong> Attacks where an attacker intercepts and possibly alters communication between two parties without their knowledge. MitM attacks can occur in various scenarios, such as Wi-Fi eavesdropping, session hijacking, and SSL stripping.
    <br><br><strong><span style='color: #336699;'>SQL Injection:</span></strong> Exploiting vulnerabilities in web applications to execute malicious SQL queries and gain unauthorized access to databases. SQL injection attacks can result in data theft, manipulation, or destruction.
    <br><br><strong><span style='color: #336699;'>Zero-Day Exploits:</span></strong> Attacks that target previously unknown vulnerabilities (zero-day vulnerabilities) in software or hardware before a patch or fix is available. Zero-day exploits pose significant risks as they give attackers the advantage of surprise.
    <br><br><strong><span style='color: #336699;'>Insider Threats:</span></strong> Malicious or unintentional actions by individuals within an organization, such as employees, contractors, or partners, that compromise security. Insider threats may involve data theft, sabotage, or negligence.
    </p>
    """

    st.markdown(importance, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Common</span> Cyber Attack Techniques</h3>", unsafe_allow_html=True)

    best_practices = """
        <p style='text-align: justify; font-size: 17px;'>
    <br><strong><span style='color: #336699;'>Social Engineering:</span></strong> Manipulating individuals to divulge sensitive information or perform actions that compromise security. Techniques include pretexting, baiting, phishing, and spear-phishing.
    <br><br><strong><span style='color: #336699;'>Exploiting Vulnerabilities:</span></strong> Leveraging weaknesses in software, hardware, or network configurations to gain unauthorized access or execute malicious actions. Attackers exploit vulnerabilities through techniques such as code injection, buffer overflows, and privilege escalation.
    <br><br><strong><span style='color: #336699;'>Brute Force Attacks:</span></strong> Attempting to guess passwords or encryption keys through trial and error. Brute force attacks rely on automated tools to systematically try every possible combination until the correct one is found.
    <br><br><strong><span style='color: #336699;'>Watering Hole Attacks:</span></strong> Compromising legitimate websites frequented by a target group to infect visitors with malware. Watering hole attacks exploit trust in popular websites to distribute malicious code.
    <br><br><strong><span style='color: #336699;'>Drive-by Downloads:</span></strong> Automatically downloading malware onto a user's device without their consent or knowledge when they visit a compromised website or click on a malicious link.
    <br><br><strong><span style='color: #336699;'>Credential Stuffing:</span></strong> Using stolen usernames and passwords obtained from data breaches to gain unauthorized access to other accounts or services. Attackers automate the process of trying combinations of credentials across multiple platforms.
    <br><br><strong><span style='color: #336699;'>IoT Exploitation:</span></strong> Targeting vulnerabilities in Internet of Things (IoT) devices to gain control over them or use them as entry points into larger networks. IoT exploitation can lead to data theft, surveillance, or disruption of services.    </p>
    """
    
    st.markdown(best_practices, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Measures </span> to Avoid Attacks / Best Practices</h3>", unsafe_allow_html=True)

    measures = """
        <p style='text-align: justify; font-size: 17px;'>
    <br><strong><span style='color: #336699;'>Regular Software Updates:</span></strong> Keep all software, operating systems, and firmware up to date to patch known vulnerabilities and protect against exploits.
    <br><br><strong><span style='color: #336699;'>Strong Authentication:</span></strong> Use strong, unique passwords or passphrases for all accounts and enable multi-factor authentication (MFA) wherever possible to add an extra layer of security.
    <br><br><strong><span style='color: #336699;'>Employee Training:</span></strong> Educate employees about cybersecurity best practices, including how to recognize phishing attempts, avoid social engineering tactics, and report suspicious activity.
    <br><br><strong><span style='color: #336699;'>Firewalls and Antivirus Software:</span></strong> Deploy firewalls to monitor and control incoming and outgoing network traffic and use reputable antivirus/antimalware solutions to detect and remove malicious software.
    <br><br><strong><span style='color: #336699;'>Data Encryption:</span></strong> Encrypt sensitive data both in transit and at rest to protect it from unauthorized access, interception, or theft.
    <br><br><strong><span style='color: #336699;'>Backup and Recovery:</span></strong> Regularly back up critical data and systems and store backups in a secure location. Test backups periodically to ensure they can be restored in the event of a cyber incident.
    <br><br><strong><span style='color: #336699;'>Access Control:</span></strong> Implement least privilege access controls to restrict user permissions and limit access to sensitive information and systems based on job roles and responsibilities.
    <br><br><strong><span style='color: #336699;'>Incident Response Plan:</span></strong> Develop and regularly test an incident response plan to quickly detect, respond to, and recover from cyber incidents. Clearly define roles and responsibilities, establish communication channels, and document procedures for incident handling.
    </p>
    """

    st.markdown(measures, unsafe_allow_html=True)  

    st.write("")
    st.write("")

    video_url = 'https://www.youtube.com/embed/awhqnSskWjU' 
    video_html = f'<div style="display: flex; justify-content: center;"><iframe width="640" height="360" src="{video_url}" frameborder="0" allowfullscreen></iframe></div>'
    st.markdown(video_html, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.write("   ")
    st.write("   ")
    st.markdown("Explore further:  https://www.upguard.com/blog/cyber-threat-landscape", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")


    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)

    questions = [
    {
    "question": "Which of the following is NOT a type of malware?",
    "options": [
    "Virus",
    "Worm",
    "Trojan",
    "Keylogger"
    ],
    "answer": "Keylogger"
    },
    {
    "question": "What is the main objective of a Denial of Service (DoS) or Distributed Denial of Service (DDoS) attack?",
    "options": [
    "To gain unauthorized access to a system",
    "To steal sensitive data",
    "To disrupt or overload a network, server, or service",
    "To spread malware to other devices"
    ],
    "answer": "To disrupt or overload a network, server, or service"
    },
    {
    "question": "Which attack technique involves manipulating individuals to divulge sensitive information or perform actions that compromise security?",
    "options": [
    "Exploiting Vulnerabilities",
    "Brute Force Attacks",
    "Social Engineering",
    "Credential Stuffing"
    ],
    "answer": "Social Engineering"
    },
    {
    "question": "What is the purpose of implementing multi-factor authentication (MFA) as a cybersecurity best practice?",
    "options": [
    "To make it easier for users to access their accounts",
    "To add an extra layer of security to user accounts",
    "To reduce the need for strong passwords",
    "To bypass firewalls and antivirus software"
    ],
    "answer": "To add an extra layer of security to user accounts"
    },
    {
    "question": "Which of the following is NOT a recommended measure to avoid cyber attacks?",
    "options": [
    "Regular Software Updates",
    "Disabling Firewalls and Antivirus Software",
    "Employee Training",
    "Incident Response Plan"
    ],
    "answer": "Disabling Firewalls and Antivirus Software"
    }
    ]


    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken3' not in st.session_state:
            st.session_state['quiz_taken3'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken3:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Case Studies in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken3 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")



##############################################################  CASE STUDY ###################################################################

def sbi_case_study():
   st.markdown("<h2 style='text-align: Center;'>SBI Case Study</h2>", unsafe_allow_html=True)
   
   col1,col2,col3 = st.columns([10,5,10])

   with col2:
    st.image("sbi.png", use_column_width=True)

   st.markdown("<h3 style='text-align: left;'>Introduction to SBI</h3>", unsafe_allow_html=True)
   st.write("State Bank of India (SBI) is the largest public sector bank in India. It was established in 1955 and is headquartered in Mumbai, India. SBI has a vast network of over 22,000 branches and more than 58,000 ATMs across the country, making it one of the largest banking networks in the world. SBI offers a wide range of banking services, including deposits, loans, credit cards, insurance, and wealth management, catering to both individual and corporate customers.")

   importance = """
    - <span style='color: #336699;'><strong>Data Protection:</strong></span> Banks handle vast amounts of sensitive customer data, which must be safeguarded from breaches and unauthorized access.
    - <span style='color: #336699;'><strong>Secure Transactions:</strong></span> Robust cybersecurity measures are essential to prevent disruptions and ensure the integrity of financial transactions.
    - <span style='color: #336699;'><strong>Regulatory Compliance:</strong></span> Banks must comply with strict cybersecurity regulations to avoid penalties and reputational damage.
    - <span style='color: #336699;'><strong>Preventing Cyber Attacks:</strong></span> Banks are prime targets for cybercriminals, and effective cybersecurity is crucial to mitigate the risks of cyberattacks.
    
       """
   st.markdown("<h3 style='text-align: left;'>Importance of Cybersecurity for Banks</h3>", unsafe_allow_html=True)
   st.markdown(importance, unsafe_allow_html=True)


   st.write("")
   st.write("")


   st.markdown("<h5 style='text-align: left;'>Steps taken by SBI to ensure online security:</h5>", unsafe_allow_html=True)
   with st.expander("Secure Platform"):
       st.write("- Strong authentication & authorization controls are implemented for all our digital banking applications for your secure access.")
       st.write("- We follow the 'security by design' approach to provide you secure access and a protected platform to perform financial transactions.")

   with st.expander("Session Layer Security"):
       st.write("- Secure channel of communication is implemented on all our banking services to prevent unauthorized interception of your activity on our digital platform.")
       st.write("- 256 bit encryption is implemented on all traffic to secure the transactions performed over the internet.")
       st.write("- Customer's login session is logged out after some idle time to protect against misuse.")

   with st.expander("Login Security"):
       st.write("- Captcha is implemented to prevent you from Brute Force Attacks/Botnet attacks.")
       st.write("- One Time Password (OTP) is sent to your Registered Mobile Number (RMN) as a 2nd Factor of Authentication (2FA) for login to Internet Banking (INB) application.")
       st.write("- Virtual Keyboard is provided for logging to your net banking in order to prevent from keylogger attacks.")

   with st.expander("Profile Security"):
       st.write("- Access to privileged pages for carrying out privileged activities such as Adding Beneficiary, changing user profile etc. is controlled through a Profile Password.")
       st.write("- Alerts are sent every time you access your profile section.")

   with st.expander("Transfer Security"):
       st.write("- All NEFT/ RTGS transactions other than quick transfer are performed only after addition of beneficiary and within the transaction limit defined by you.")
       st.write("- Transfer to a newly added beneficiary can be performed after a cooling period of up to 4 hours.")

   with st.expander("Notification"):
       st.write("- OTP is sent to RMN as a 2FA for transactions carried out through the Internet Banking site/YONO.")
       st.write("- Text messages over Short Message Service (SMS) are sent for transactions carried out in the account through INB/YONO.")
       st.write("- All activities happening in your account are promptly notified to you through SMS or Email alerts.")

   with st.expander("Mobile Security"):
       st.write("- SIM binding and device binding has been enabled on YONO and YONO Lite apps.")
       st.write("- Anti-tampering is implemented to prevent unauthorized changes to mobile apps.")

   with st.expander("End To End Security"):
       st.write("- End to End encryption is implemented to keep your data confidential and invisible to everyone within the Bank as well.")
       st.write("- Your credentials are hashed and protected with industry standard encryption to maintain secrecy.")

   with st.expander("Transaction Monitoring"):
       st.write("- Robust solutions, systems, and processes are deployed to monitor the safety of your accounts.")
       st.write("- Our security team is deployed 24/7 to monitor, analyze and detect any abnormal activity, indicating a potential breach, security incident or malicious attempts to the system.")

   with st.expander("Customer Care"):
       st.write("- 24*7 customer services are provided to customers to raise any issues and get quick redressal.")

   st.write("")
   st.write("")

   st.markdown("<h5 style='text-align: left;'>Your role in ensuring your digital security:</h5>", unsafe_allow_html=True)
   with st.expander("Login Security"):
       st.write("- Use unique and complex passwords.")
       st.write("- Remember to change passwords frequently.")
       st.write("- Never disclose, store or write down your user ID, passwords or PIN. Remember, Bank never asks for your user ID/passwords/Card No/PIN/Passwords/CVV.")
       st.write("- Disable 'Auto Save' or 'Remember' function in your device to avoid storing of user ID and passwords.")

   with st.expander("Internet Security"):
       st.write("- Always look for 'https' in the address bar of our banking site.")
       st.write("- Do not perform online banking transactions at public places using public / open Wi-Fi networks.")
       st.write("- Always logout and close the browser when you are done with your work.")

   with st.expander("UPI Security"):
       st.write("- Keep your Mobile PIN and UPI PIN different and random.")
       st.write("- Do not respond to any unknown UPI requests.")
       st.write("- Report suspicious requests.")
       st.write("- Always remember that a PIN is needed only for transferring amounts, not for receiving.")
       st.write("- Instantly disable UPI service on your account if any transaction has happened without you doing it.")

   with st.expander("Debit/Credit Card Security"):
       st.write("- Beware of your surroundings while performing ATM transactions through ATM machines or POS devices. Cover the keypad while entering the PIN.")
       st.write("- Always verify the authenticity of e-commerce websites before performing the transactions.")
       st.write("- Manage your debit card transactions through online Banking. Set a limit for card transactions at e-commerce platforms, POS and ATM both for domestic and international transactions.")

   with st.expander("Mobile Banking Security"):
       st.write("- Strong passwords/ Biometric permission should be enabled on your phone, tablets.")
       st.write("- Do not share your Mobile PIN with anyone, Use biometric authentication wherever feasible.")
       st.write("- Do not download any unknown app suggested by strangers.")
       st.write("- Applications should be downloaded only through official stores.")
       st.write("- Regularly monitor the permissions of critical apps installed in your mobile and keep a track of unnecessary and unused apps.")
       st.write("- Avoid connecting phones to public wireless networks.")

   with st.expander("Social Media Security"):
       st.write("- Confirm the identity of the person you are interacting with.")
       st.write("- Do not share your personal/financial information on any social media platform.")
       st.write("- Do not discuss confidential information in public places.")


   st.markdown("<h4 style='text-align: left;'>To report cyber incident:</h4>", unsafe_allow_html=True)
   st.write("report.phishing@sbi.co.in or call cyber crime helpline number 1930.")


def case_study_1():
    
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Google and Facebook Business Email Compromise (2017-2018) </span></h2>", unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns([2,5,2])

    with col2:

        st.image("5.jpg")

    #Background section
    st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Background</span></h3>", unsafe_allow_html=True)
    background_content = """
    <p style='text-align: justify; font-size: 16px;'>
    In 2017 and 2018, Google and Facebook were targeted by a sophisticated business email compromise (BEC) scam. 
    The perpetrators, based in Lithuania, managed to trick the companies' employees into sending millions of dollars to fraudulent bank accounts, posing as legitimate suppliers and partners.
    </p>
    """
    st.markdown(background_content, unsafe_allow_html=True)


    col1,col2 = st.columns([2,2])

    with col1:

        # Ethical Issues section
        st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Ethical Issues</span></h3>", unsafe_allow_html=True)
        ethical_issues_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The BEC scam against Google and Facebook raised ethical concerns about the companies' internal controls and the vulnerabilities in their financial processes. 
        The incident highlighted the need for stronger authentication measures, employee training, and vigilance against social engineering attacks targeting corporate email accounts.
        </p>
        """
        st.markdown(ethical_issues_content, unsafe_allow_html=True)

    with col2:

        # Consequences section
        st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Consequences</span></h3>", unsafe_allow_html=True)
        consequences_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The BEC scam resulted in significant financial losses for Google and Facebook, with estimates ranging from $100 million to over $120 million. 
        The incident also raised questions about the companies' responsibility to protect their assets and the potential vulnerabilities in their supply chain management
        </p>
        """
        st.markdown(consequences_content, unsafe_allow_html=True)

    # Lessons Learned section
    st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Lessons Learned</span></h3>", unsafe_allow_html=True)
    lessons_learned_content = """
    <p style='text-align: justify; font-size: 16px;'>
    The Google and Facebook BEC case emphasizes the importance of implementing robust email security protocols, including multi-factor authentication, vendor verification processes, and comprehensive employee training on recognizing and reporting suspicious activities. It also highlights the need for companies to maintain tight control over their financial processes and to be vigilant against emerging fraud tactics.
    </p>
    """
    st.markdown(lessons_learned_content, unsafe_allow_html=True)


    col1,col2,col3 = st.columns([2,10,2])

    with col2:
        # Embed YouTube video
        st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Video</span></h3>", unsafe_allow_html=True)
        video_link = "https://www.youtube.com/embed/smVmctelJCo"
        st.markdown(f'<iframe width="560" height="315" src="{video_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)


    st.write("   ")
    st.write("   ")
    st.markdown("Reading: https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/google-and-facebook-fraudster-pleads-guilty-to-100-million-scam", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")


    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)


    questions = [
    {
    "question": "What was the primary tactic used by the perpetrators in the BEC scam against Google and Facebook?",
    "options": [
    "Hacking into the companies' internal systems",
    "Exploiting software vulnerabilities", 
    "Impersonating legitimate suppliers and partners",
    "Conducting a distributed denial-of-service (DDoS) attack"
    ],
    "answer": "Impersonating legitimate suppliers and partners"
    },
    {
    "question": "What was the primary lesson learned from this incident for organizations?",
    "options": [
    "Strengthening physical security measures",
    "Implementing stronger employee background checks",
    "Focusing on cybersecurity awareness training for executives",
    "Enhancing email security protocols and vendor verification processes"
    ],
    "answer": "Enhancing email security protocols and vendor verification processes"
    }
    ]


    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken4' not in st.session_state:
            st.session_state['quiz_taken4'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken4:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Case Studies in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken4 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")

def case_study_2():

    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Edward Snowden's NSA Leaks (2013)</span></h2>", unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns([1,5,1])

    with col2:

        st.image("8.jpg")


    # Background section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Background</span></h2>", unsafe_allow_html=True)
    background_content = """
    <p style='text-align: justify; font-size: 16px;'>
    In 2013, former National Security Agency (NSA) contractor Edward Snowden leaked a trove of classified documents detailing the NSA's extensive surveillance programs, including the collection of personal data from internet and telecommunication companies.
    </p>
    """
    st.markdown(background_content, unsafe_allow_html=True)


    col1,col2 = st.columns([1,1])

    with col1:

        # Ethical Issues section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Ethical Issues</span></h2>", unsafe_allow_html=True)
        ethical_issues_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The Snowden leaks raised significant ethical concerns about the NSA's mass surveillance practices and the balance between national security and individual privacy. The revelations sparked a global debate about the appropriate use of government surveillance, the scope of intelligence gathering, and the need for stronger oversight and accountability.
        </p>
        """
        st.markdown(ethical_issues_content, unsafe_allow_html=True)

    with col2:

        # Consequences section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Consequences</span></h2>", unsafe_allow_html=True)
        consequences_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The Snowden leaks had far-reaching consequences, including damaging the reputation of the U.S. government and intelligence agencies, straining international relations, and prompting reforms to surveillance laws and regulations. The incident also had a chilling effect on journalism and whistleblowing activities, as it highlighted the risks that individuals face when exposing government secrets.
        </p>
        """
        st.markdown(consequences_content, unsafe_allow_html=True)

    # Lessons Learned section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Lessons Learned</span></h2>", unsafe_allow_html=True)
    lessons_learned_content = """
    <p style='text-align: justify; font-size: 16px;'>
    The Snowden case underscores the importance of striking a balance between national security and civil liberties, as well as the need for robust oversight and transparency in government surveillance programs. It also emphasizes the ethical dilemmas faced by whistleblowers and the need to protect those who expose wrongdoing in the public interest.
    </p>
    """
    st.markdown(lessons_learned_content, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([2,10,2])

    with col2:

        # Embed YouTube video
        st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Video</span></h3>", unsafe_allow_html=True)
        video_link = "https://www.youtube.com/embed/46UmxpxuEA4"
        st.markdown(f'<iframe width="560" height="315" src="{video_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")
    st.markdown("Reading: https://www.theguardian.com/world/2013/jun/09/edward-snowden-nsa-whistleblower-surveillance", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")
    
    
    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)


    questions = [
    {
    "question": "What was the primary issue raised by the Snowden leaks regarding the NSA's surveillance programs?",
    "options": [
    "The legality of the surveillance activities",
    "The lack of funding for the NSA's operations",
    "The ineffectiveness of the NSA's intelligence gathering",
    "The invasion of individual privacy"
    ],
    "answer": "The invasion of individual privacy"
    },
    {
    "question": "What was a key consequence of the Snowden leaks?",
    "options": [
    "Increased public trust in the U.S. government",
    "Improved international relations for the United States",
    "Strengthening of whistleblower protection laws",
    "Damage to the reputation of the U.S. government and intelligence agencies"
    ],
    "answer": "Damage to the reputation of the U.S. government and intelligence agencies"
    }
    ]



    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken5' not in st.session_state:
            st.session_state['quiz_taken5'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken5:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Case Studies in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken5 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")

def case_study_3():
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Equifax Data Breach (2017)</span></h2>", unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns([1,5,1])

    with col2:

        st.image("6.jpg")


    # Background section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Background</span></h2>", unsafe_allow_html=True)
    background_content = """
    <p style='text-align: justify; font-size: 16px;'>
    In 2017, the credit reporting agency Equifax suffered a massive data breach that exposed the personal information of over 147 million individuals, including names, social security numbers, birth dates, and credit card numbers. The breach was caused by a vulnerability in the company's web application software that went unpatched for several months.

    </p>
    """
    st.markdown(background_content, unsafe_allow_html=True)


    col1,col2 = st.columns([1,1])

    with col1:

        # Ethical Issues section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Ethical Issues</span></h2>", unsafe_allow_html=True)
        ethical_issues_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The Equifax data breach raised significant ethical concerns related to the company's failure to protect sensitive customer data, as well as its response to the incident. Equifax's delayed disclosure and perceived mishandling of the breach eroded public trust and highlighted the need for stronger data security practices and transparency among organizations that handle large amounts of personal information.

        </p>
        """
        st.markdown(ethical_issues_content, unsafe_allow_html=True)

    with col2:

        # Consequences section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Consequences</span></h2>", unsafe_allow_html=True)
        consequences_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The Equifax data breach resulted in substantial financial and reputational consequences for the company. It faced numerous lawsuits, government investigations, and fines from regulatory bodies, including a $700 million settlement with the Federal Trade Commission. The breach also had a significant impact on the affected individuals, who were at increased risk of identity theft and financial fraud.
        </p>
        """
        st.markdown(consequences_content, unsafe_allow_html=True)

    # Lessons Learned section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Lessons Learned</span></h2>", unsafe_allow_html=True)
    lessons_learned_content = """
    <p style='text-align: justify; font-size: 16px;'>
    The Equifax case underscores the importance of robust patch management, regular vulnerability assessments, and comprehensive data protection measures. It also emphasizes the need for organizations to have robust incident response plans and to prioritize transparency and accountability when data breaches occur.
    </p>
    """
    st.markdown(lessons_learned_content, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([2,10,2])

    with col2:

        # Embed YouTube video
        st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Video</span></h3>", unsafe_allow_html=True)
        video_link = "https://www.youtube.com/embed/g6sb6LhO0U4"
        st.markdown(f'<iframe width="560" height="315" src="{video_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")
    st.markdown("Reading: https://en.wikipedia.org/wiki/2017_Equifax_data_breach#:~:text=Information%20accessed%20in%20the%20breach,British%20residents%20was%20also%20compromised.", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")
    
    
    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)


    questions = [
    {
    "question": "What was the primary cause of the Equifax data breach in 2017?",
    "options": [
    "Hacking into Equifax's internal systems",
    "Phishing attacks targeting Equifax employees",
    "Failure to patch a known vulnerability in the company's web application software",
    "Insider threat from a disgruntled Equifax employee"
    ],
    "answer": "Failure to patch a known vulnerability in the company's web application software"
    },
    {
    "question": "What was a key consequence of the Equifax data breach?",
    "options": [
    "Improved public trust in Equifax's data security practices",
    "Increased revenue and profitability for the company",
    "Lawsuits, government investigations, and substantial fines for Equifax",
    "No significant impact on the affected individuals"
    ],
    "answer": "Lawsuits, government investigations, and substantial fines for Equifax"
    }
    ]



    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken6' not in st.session_state:
            st.session_state['quiz_taken6'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken6:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Case Studies in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken6 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")

def case_study_4():
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>GitHub Data Recovery (2018)</span></h2>", unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns([3,5,1])

    with col2:

        st.image("7.jpg")


    # Background section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Background</span></h2>", unsafe_allow_html=True)
    background_content = """
    <p style='text-align: justify; font-size: 16px;'>
    In 2018, GitHub, a popular code hosting and collaboration platform, experienced a data recovery incident that led to the accidental deletion of a significant amount of user data. The incident was caused by a failed data migration process, which resulted in the unintentional loss of code repositories, commit histories, and other user content.
    </p>
    """
    st.markdown(background_content, unsafe_allow_html=True)


    col1,col2 = st.columns([1,1])

    with col1:

        # Ethical Issues section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Ethical Issues</span></h2>", unsafe_allow_html=True)
        ethical_issues_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The GitHub data recovery incident raised ethical concerns about the company's data management practices and its responsibility to safeguard the digital assets of its users. The incident highlighted the need for robust data backup and recovery protocols, as well as transparent communication with affected users.
        </p>
        """
        st.markdown(ethical_issues_content, unsafe_allow_html=True)

    with col2:

        # Consequences section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Consequences</span></h2>", unsafe_allow_html=True)
        consequences_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The GitHub data recovery incident resulted in significant disruption to the platform's users, who were unable to access their content for an extended period. The incident also raised concerns about the reliability and trustworthiness of GitHub as a platform for hosting and collaborating on software projects.
        </p>
        """
        st.markdown(consequences_content, unsafe_allow_html=True)

    # Lessons Learned section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Lessons Learned</span></h2>", unsafe_allow_html=True)
    lessons_learned_content = """
    <p style='text-align: justify; font-size: 16px;'>
    The GitHub case emphasizes the importance of implementing comprehensive data backup and recovery strategies, as well as rigorous testing and validation of critical data migration processes. It also underscores the need for organizations to prioritize transparent communication and accountability when dealing with incidents that impact their users.
    </p>
    """
    st.markdown(lessons_learned_content, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([2,10,2])

    with col2:

        # Embed YouTube video
        st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Video</span></h3>", unsafe_allow_html=True)
        video_link = "https://www.youtube.com/embed/dsHyUgGMht0"
        st.markdown(f'<iframe width="560" height="315" src="{video_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")
    st.markdown("Reading:  https://www.linkedin.com/pulse/how-githubs-database-self-destructed-43-seconds-david-furman", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")
    
    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)


    questions = [
    {
    "question": "What was the primary cause of the data recovery incident that affected GitHub in 2018?",
    "options": [
    "A cyberattack targeting GitHub's systems",
    "A hardware failure in GitHub's data centers",
    "A failed data migration process that led to accidental data deletion",
    "A disgruntled GitHub employee intentionally deleting user data"
    ],
    "answer": "A failed data migration process that led to accidental data deletion"
    },
    {
    "question": "What was a key consequence of the GitHub data recovery incident?",
    "options": [
    "Increased user trust and confidence in the platform",
    "Improved data management and backup protocols at GitHub",
    "Disruption to users' access to their code repositories and content",
    "No significant impact on GitHub's operations or reputation"
    ],
    "answer": "Disruption to users' access to their code repositories and content"
    }
    ]



    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken7' not in st.session_state:
            st.session_state['quiz_taken7'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken7:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Case Studies in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken7 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")

def case_study_5():
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Stuxnet Worm (2010)</span></h2>", unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns([1,5,1])

    with col2:

        st.image("9.jpg")


    # Background section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Background</span></h2>", unsafe_allow_html=True)
    background_content = """
    <p style='text-align: justify; font-size: 16px;'>
    Stuxnet was a highly sophisticated piece of malware discovered in 2010, which specifically targeted and damaged industrial control systems used in uranium enrichment facilities in Iran. The worm was believed to be a joint effort between the United States and Israel, and it was considered one of the first examples of a cyberweapon used for military and political purposes.
    </p>
    """
    st.markdown(background_content, unsafe_allow_html=True)


    col1,col2 = st.columns([1,1])

    with col1:

        # Ethical Issues section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Ethical Issues</span></h2>", unsafe_allow_html=True)
        ethical_issues_content = """
        The Stuxnet incident raised significant ethical concerns about the use of cyber warfare tactics and the potential for such attacks to cause unintended consequences. The targeting of critical infrastructure, such as nuclear facilities, highlighted the need for international agreements and norms governing the use of cyber weapons.

        </p>
        """
        st.markdown(ethical_issues_content, unsafe_allow_html=True)

    with col2:

        # Consequences section
        st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Consequences</span></h2>", unsafe_allow_html=True)
        consequences_content = """
        <p style='text-align: justify; font-size: 16px;'>
        The Stuxnet worm caused substantial damage to Iran's nuclear program, setting back their uranium enrichment efforts. However, the incident also raised concerns about the potential for such attacks to cause collateral damage and escalate tensions between nations. The Stuxnet case demonstrated the growing threat of state-sponsored cyber warfare and the urgent need for robust international cooperation to address these challenges.

        </p>
        """
        st.markdown(consequences_content, unsafe_allow_html=True)

    # Lessons Learned section
    st.markdown("<h2 style='text-align: Center;'><span style='color: #336699;'>Lessons Learned</span></h2>", unsafe_allow_html=True)
    lessons_learned_content = """
    <p style='text-align: justify; font-size: 16px;'>
    The Stuxnet case underscores the importance of strengthening the security of industrial control systems and critical infrastructure, as well as the need for international agreements and norms to govern the use of cyber weapons. It also highlights the potential for unintended consequences and the need for a nuanced, ethical approach to the development and deployment of such technologies.
    </p>
    """
    st.markdown(lessons_learned_content, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([2,10,2])

    with col2:

        # Embed YouTube video
        st.markdown("<h3 style='text-align: Center;'><span style='color: #336699;'>Video</span></h3>", unsafe_allow_html=True)
        video_link = "https://www.youtube.com/embed/q1SNqjvOBYU"
        st.markdown(f'<iframe width="560" height="315" src="{video_link}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

    st.write("   ")
    st.write("   ")
    st.markdown("Reading: http://large.stanford.edu/courses/2015/ph241/holloway1/", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")
    
    st.markdown("<h4 style='text-align: Center;'>Quiz Section</h5>", unsafe_allow_html=True)


    questions = [
    {
    "question": "What was the primary target of the Stuxnet malware?",
    "options": [
    "The financial systems of major corporations",
    "The control systems of nuclear power plants in the United States",
    "The uranium enrichment facilities in Iran",
    "The personal computers of government officials in various countries"
    ],
    "answer": "The uranium enrichment facilities in Iran"
    },
    {
    "question": "What was a key ethical concern raised by the Stuxnet incident?",
    "options": [
    "The potential for unintended consequences from the use of cyber weapons",
    "The lack of international cooperation in addressing cyber threats",
    "The disproportionate impact of the attack on the Iranian people",
    "The violation of Iranian sovereignty by the United States and Israel"
    ],
    "answer": "The potential for unintended consequences from the use of cyber weapons"
    }
    ]



    # Initialize score
    score = 0

    # Get or create user session state
    def get_session():
        if 'quiz_taken8' not in st.session_state:
            st.session_state['quiz_taken8'] = False

    # Get session state
    get_session()

    if not st.session_state.quiz_taken8:
        # Store user answers
        user_answers = {}

        # Render questions
        for i, q in enumerate(questions):
            st.markdown(f"<h3 style='font-size:20px'>Question {i+1}: {q['question']}</h3>", unsafe_allow_html=True)
            user_answers[i] = st.radio("", q["options"], index=None, key=i)
            st.write("") 
            st.write("") 

        # Submit button
        
        col1, col2 , col3 = st.columns([12,10,1])
        with col2:
            if st.button("Submit"):
                # Calculate score
                for i, q in enumerate(questions):
                    if user_answers[i] == q["answer"]:
                        score += 1

                st.toast(f"Your score is: {score}/{len(questions)}, Please click on Case Studies in the sidebar for the next section")

                # Update session state
                st.session_state.quiz_taken8 = True
                st.session_state.score = st.session_state.score + score
    else:
        st.warning("You have already taken the quiz. You can only take it once.")




    ############################################## MAIN #############################################################

##############################################################  leaderboard ###################################################################

def leaderboard():
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>Leader<span style='color: #336699;'>board</Span></h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    # Read the leaderboard data from the Excel file
    leaderboard_df = pd.read_excel(r"C:\Users\edwin\Downloads\leaderboard.xlsx", engine='openpyxl')

    # Sort the leaderboard in descending order of scores
    leaderboard_df = leaderboard_df.sort_values(by='Score', ascending=False)

    # Add a Rank column
    leaderboard_df['Rank'] = leaderboard_df['Score'].rank(ascending=False, method='dense').astype(int)

    # Style the table
    table_html = leaderboard_df[['Rank', 'Username', 'Score']].style.format({
        "Score": "{:.2f}",
        "Rank": "{:d}"
    }).set_table_styles([
        {"selector": "th", "props": [("text-align", "center"), ("font-weight", "bold"), ("background-color", "#2a2a2a"), ("color", "#ffffff"), ("padding", "12px")]},
        {"selector": "td", "props": [("text-align", "center"), ("color", "#ffffff"), ("padding", "12px")]},
        {"selector": "tr:nth-child(even)", "props": [("background-color", "#333333")]},
        {"selector": "tr:hover", "props": [("background-color", "#444444")]},
        {"selector": "table", "props": [("margin", "0 auto"), ("width", "auto"), ("max-width", "100%")]},  # Added this line
    ]).set_table_attributes('border="1" class="dataframe"').to_html()



    col1,col2,col3 = st.columns([5,3,6])

    with col2:
        # Display the leaderboard table
        st.markdown(table_html, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Display the current user's rank
    if 'username' in st.session_state and st.session_state.username:
        current_user_score = leaderboard_df[leaderboard_df['Username'] == st.session_state.username]
        if not current_user_score.empty:
            rank = current_user_score['Rank'].values[0]
            st.markdown(f"<h3 style='text-align: center; color: #ffffff;'>YOUR <span style='color: #336699;'>RANK</span>: {int(rank)}</h3>", unsafe_allow_html=True)


# Define the sidebar navigation menu
def main():
    with st.sidebar:
        if 'username' in st.session_state:
            menu_title = f"{st.session_state.username}"

            
        else:
            menu_title = None
        selected = option_menu(
            menu_title=menu_title,
            options=["Home", "What is Cybersecurity?", "Foundations", "Cyber Threats","SBI case study" ,"Case Studies","Leaderboard"],
            icons=["house", "book", "list-task", "lock","bank", "highlighter","trophy"],
            default_index=0,
        )

        if 'score' in st.session_state:
            score_html = f"""
            <div style="background-color: #121212; color: #FFFFFF; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.1), 0 6px 20px 0 rgba(255, 255, 255, 0.07); text-align: center;">
                <p style="font-weight: bold; font-size: 16px; margin-bottom: 10px;">Score</p>
                <p style="font-size: 24px; color: #4CAF50; margin: 0;">{st.session_state.score}</p>
            </div>
            """
            st.markdown(score_html, unsafe_allow_html=True)

            st.write("")
            st.write("")
            
            col1,col2,col3 = st.columns([1,2,1])

            with col2:

                if st.button("Submit Score") and not st.session_state.get('score_submitted', False):

                    leaderboard_df = pd.read_excel(r"C:\Users\edwin\Downloads\leaderboard.xlsx", engine='openpyxl')
                    new_entry = pd.DataFrame({'Username': [st.session_state.username], 'Score': [st.session_state.score]})
                    leaderboard_df = pd.concat([leaderboard_df, new_entry], ignore_index=True)
                    leaderboard_df.to_excel(r"C:\Users\edwin\Downloads\leaderboard.xlsx", index=False, engine='openpyxl')
                    st.session_state.score_submitted = True  # Set score_submitted to True
                    st.success(f"Score submitted successfully! Your score: {st.session_state.score}")
                elif st.session_state.get('score_submitted', False):
                    st.warning("Score already submitted!")
        else:
            st.session_state.score = 0

            

    if selected == "Home":
         home()
    elif selected == "What is Cybersecurity?":
         what_is_cybersecurity()
    elif selected == "Foundations":
        foundations_of_cybersecurity()
    elif selected == "Cyber Threats":
        cyber_threats()
    elif selected == "SBI case study":
        sbi_case_study()
    elif selected == "Case Studies":
            case_study_submenu = st.selectbox("Select a Case Study", ["Google and Facebook Business Email Compromise", "Edward Snowden's NSA Leaks", "Equifax Data Breach", "GitHub Data Recovery", "Stuxnet Worm"])
            if case_study_submenu == "Google and Facebook Business Email Compromise":
                case_study_1()
            elif case_study_submenu == "Edward Snowden's NSA Leaks":
                case_study_2()
            elif case_study_submenu == "Equifax Data Breach":
                case_study_3()
            elif case_study_submenu == "GitHub Data Recovery":
                case_study_4()
            elif case_study_submenu == "Stuxnet Worm":
                case_study_5()
    elif selected  == "Leaderboard":
        leaderboard()



if __name__ == "__main__":
    main()

