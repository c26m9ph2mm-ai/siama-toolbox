import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="SIAMA Toolbox",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #f0f8ff 0%, #e6f3ff 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .toolkit-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .step-header {
        color: #2c5aa0;
        font-weight: bold;
        font-size: 1.2rem;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'sit_data' not in st.session_state:
    st.session_state.sit_data = {'stakeholders': [], 'roles': {}}
if 'sat_data' not in st.session_state:
    st.session_state.sat_data = {'relationship_matrix': pd.DataFrame()}
if 'mat_data' not in st.session_state:
    st.session_state.mat_data = {}

# Navigation
st.sidebar.title("🎨 SIAMA Toolbox")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "1️⃣ SIT - Stakeholder Identification", "2️⃣ SAT - Stakeholder Analysis", 
     "3️⃣ MAT - Market Analysis", "📊 Summary & Export"]
)

# Home Page
if menu == "🏠 Home":
    st.markdown('<div class="main-header">SIAMA Toolbox</div>', unsafe_allow_html=True)
    st.markdown("### Stakeholder Identification, Analysis, and Market Assessment")
    
    st.markdown("""
    <div class="toolkit-card">
    <h3>🎯 Purpose</h3>
    The SIAMA toolbox is a comprehensive framework designed to help craft trainers and training organizations 
    systematically plan craft education programs by understanding contextually different needs of artisans in India.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="toolkit-card">
        <h3>❓ What should we teach?</h3>
        Addressed through:
        <ul>
        <li>Market study components (MAT)</li>
        <li>Artisan's prior skill, knowledge, and aspirations (SIT, SAT)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="toolkit-card">
        <h3>👥 Whom should we teach?</h3>
        Addressed through:
        <ul>
        <li>Stakeholder identification (SIT)</li>
        <li>Stakeholder analysis (SAT)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📦 The Three Toolkits")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **1. Stakeholder Identification Toolkit (SIT)**
        - 4 Sequential Steps
        - Identifies craft value chain actors
        - Maps stakeholder relationships
        - Visualizes supply chain
        """)
    
    with col2:
        st.markdown("""
        **2. Stakeholder Analysis Toolkit (SAT)**
        - 5 Sequential Tools
        - Analyzes power, interest, legitimacy
        - Conflict resolution strategies
        - Knowledge & responsibility mapping
        """)
    
    with col3:
        st.markdown("""
        **3. Market Analysis Toolkit (MAT)**
        - 8 Analysis Tools
        - Industry understanding
        - Customer insights
        - Brand assessment
        """)
    
    st.info("👈 Use the sidebar to navigate through each toolkit")

# SIT - Stakeholder Identification Toolkit
elif menu == "1️⃣ SIT - Stakeholder Identification":
    st.markdown('<div class="main-header">SIT - Stakeholder Identification Toolkit</div>', unsafe_allow_html=True)
    
    st.markdown("""
    SIT helps understand a craft's value chain by recognizing all individuals, groups, and organizations 
    that have a direct or indirect impact on it.
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Step 1: Predefined Roles & Questionnaires",
        "Step 2: Role × Actor Database",
        "Step 3: Role Card",
        "Step 4: Role Map"
    ])
    
    with tab1:
        st.markdown('<p class="step-header">Step 1: Predefined Roles and Questionnaires</p>', unsafe_allow_html=True)
        st.info("This tool provides predefined roles relevant to craft supply chains with structured questionnaires.")
        
        roles = ["Supplier", "Producer", "Refiner", "Marketer", "Buyer"]
        
        selected_role = st.selectbox("Select Role to Interview", roles)
        
        st.subheader(f"Primary Questionnaire for {selected_role}")
        
        questionnaires = {
            "Supplier": [
                "Who provides the raw materials?",
                "Where do they source materials from?",
                "What is their relationship with producers?"
            ],
            "Producer": [
                "Who creates the craft products?",
                "What skills do they possess?",
                "How long have they been practicing?"
            ],
            "Refiner": [
                "Who adds value to the basic product?",
                "What refinement processes are used?",
                "What expertise do they bring?"
            ],
            "Marketer": [
                "Who promotes the products?",
                "What channels do they use?",
                "What is their reach?"
            ],
            "Buyer": [
                "Who are the end consumers?",
                "What are their preferences?",
                "What price points do they prefer?"
            ]
        }
        
        responses = {}
        for q in questionnaires[selected_role]:
            responses[q] = st.text_area(q, key=f"q_{selected_role}_{q}")
        
        st.subheader("Secondary Questionnaire (Deep Dive)")
        secondary_questions = [
            "How frequently do they interact?",
            "What are the payment terms?",
            "Are there any challenges in this relationship?"
        ]
        
        for sq in secondary_questions:
            responses[sq] = st.text_area(sq, key=f"sq_{selected_role}_{sq}")
        
        if st.button("Save Stakeholder Data"):
            stakeholder_entry = {
                "role": selected_role,
                "responses": responses,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.sit_data['stakeholders'].append(stakeholder_entry)
            st.success(f"✅ Data saved for {selected_role}")
    
    with tab2:
        st.markdown('<p class="step-header">Step 2: Role × Actor Database</p>', unsafe_allow_html=True)
        st.info("Record structured information about identified stakeholders.")
        
        if len(st.session_state.sit_data['stakeholders']) > 0:
            # Create a dataframe from stakeholders
            data_for_df = []
            for s in st.session_state.sit_data['stakeholders']:
                row = {"Role": s['role'], "Timestamp": s['timestamp']}
                for q, a in s['responses'].items():
                    row[q[:30]] = a[:50] if a else ""
                data_for_df.append(row)
            
            df = pd.DataFrame(data_for_df)
            st.dataframe(df, use_container_width=True)
            
            # Edit/Add actors
            st.subheader("Add Actor Details")
            col1, col2 = st.columns(2)
            with col1:
                actor_name = st.text_input("Actor Name")
                actor_role = st.selectbox("Role", ["Supplier", "Producer", "Refiner", "Marketer", "Buyer"])
            with col2:
                actor_location = st.text_input("Location")
                actor_contact = st.text_input("Contact Information")
            
            actor_details = st.text_area("Additional Details")
            
            if st.button("Add Actor"):
                if actor_name:
                    if actor_role not in st.session_state.sit_data['roles']:
                        st.session_state.sit_data['roles'][actor_role] = []
                    
                    st.session_state.sit_data['roles'][actor_role].append({
                        "name": actor_name,
                        "location": actor_location,
                        "contact": actor_contact,
                        "details": actor_details
                    })
                    st.success(f"✅ Actor {actor_name} added to {actor_role}")
        else:
            st.warning("⚠️ Please complete Step 1 first to collect stakeholder data.")
    
    with tab3:
        st.markdown('<p class="step-header">Step 3: Role Card Visualization</p>', unsafe_allow_html=True)
        st.info("Visualize stakeholders clustered around specific roles in the supply chain.")
        
        if st.session_state.sit_data['roles']:
            for role, actors in st.session_state.sit_data['roles'].items():
                with st.expander(f"📋 {role} ({len(actors)} actors)"):
                    for i, actor in enumerate(actors, 1):
                        st.markdown(f"""
                        **{i}. {actor['name']}**
                        - Location: {actor['location']}
                        - Contact: {actor['contact']}
                        - Details: {actor['details']}
                        """)
            
            # Simple visualization
            role_counts = {role: len(actors) for role, actors in st.session_state.sit_data['roles'].items()}
            fig = px.bar(
                x=list(role_counts.keys()),
                y=list(role_counts.values()),
                labels={'x': 'Role', 'y': 'Number of Actors'},
                title='Stakeholder Distribution by Role'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ Please add actors in Step 2 first.")
    
    with tab4:
        st.markdown('<p class="step-header">Step 4: Role Map</p>', unsafe_allow_html=True)
        st.info("Visualize the entire supply chain with flow markers showing how resources move.")
        
        if st.session_state.sit_data['roles']:
            st.subheader("Supply Chain Flow")
            
            # Create a network diagram
            fig = go.Figure()
            
            roles = ["Supplier", "Producer", "Refiner", "Marketer", "Buyer"]
            x_pos = [i for i in range(len(roles))]
            
            # Add nodes
            for i, role in enumerate(roles):
                actor_count = len(st.session_state.sit_data['roles'].get(role, []))
                fig.add_trace(go.Scatter(
                    x=[i], y=[0],
                    mode='markers+text',
                    marker=dict(size=40 + actor_count*10, color='lightblue'),
                    text=f"{role}<br>({actor_count})",
                    textposition="top center",
                    name=role
                ))
            
            # Add arrows
            for i in range(len(roles)-1):
                fig.add_annotation(
                    x=i+0.5, y=0,
                    ax=i, ay=0,
                    xref='x', yref='y',
                    axref='x', ayref='y',
                    text='',
                    showarrow=True,
                    arrowhead=2,
                    arrowsize=1.5,
                    arrowwidth=2,
                    arrowcolor='gray'
                )
            
            fig.update_layout(
                title='Craft Value Chain Flow',
                showlegend=False,
                height=400,
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("### Flow Indicators")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Product Flow", "→", delta="Supplier to Buyer")
            with col2:
                st.metric("Money Flow", "←", delta="Buyer to Supplier")
            with col3:
                st.metric("Information Flow", "↔", delta="Bidirectional")
        else:
            st.warning("⚠️ Please complete previous steps to visualize the role map.")

# SAT - Stakeholder Analysis Toolkit
elif menu == "2️⃣ SAT - Stakeholder Analysis":
    st.markdown('<div class="main-header">SAT - Stakeholder Analysis Toolkit</div>', unsafe_allow_html=True)
    
    st.markdown("""
    SAT evaluates the roles, interests, and influences of identified stakeholders to tailor training programs effectively.
    """)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Step 1: Relationship Matrix",
        "Step 2: Management Tool",
        "Step 3: Conflict Resolution",
        "Step 4: Knowledge & Responsibility",
        "Step 5: Value Exchange Map"
    ])
    
    with tab1:
        st.markdown('<p class="step-header">Step 1: Stakeholder Relationship Matrix</p>', unsafe_allow_html=True)
        st.info("Rate each stakeholder on Power, Interest, Legitimacy, and Urgency.")
        
        if st.session_state.sit_data['roles']:
            # Get all stakeholders
            all_stakeholders = []
            for role, actors in st.session_state.sit_data['roles'].items():
                for actor in actors:
                    all_stakeholders.append(f"{actor['name']} ({role})")
            
            if all_stakeholders:
                st.subheader("Rate Stakeholders")
                
                selected_stakeholder = st.selectbox("Select Stakeholder to Rate", all_stakeholders)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    power = st.slider("Power (ability to influence outcomes)", 1, 10, 5)
                    interest = st.slider("Interest (level of concern/stake)", 1, 10, 5)
                
                with col2:
                    legitimacy = st.slider("Legitimacy (validity of involvement)", 1, 10, 5)
                    urgency = st.slider("Urgency (immediacy of demands)", 1, 10, 5)
                
                st.subheader("Relationship Details")
                interactions = st.text_area("How do they interact with others?")
                tasks = st.text_area("What tasks do they perform?")
                knowledge = st.text_area("What knowledge/skills do they share?")
                
                if st.button("Save Rating"):
                    if 'relationship_data' not in st.session_state.sat_data:
                        st.session_state.sat_data['relationship_data'] = []
                    
                    st.session_state.sat_data['relationship_data'].append({
                        'stakeholder': selected_stakeholder,
                        'power': power,
                        'interest': interest,
                        'legitimacy': legitimacy,
                        'urgency': urgency,
                        'interactions': interactions,
                        'tasks': tasks,
                        'knowledge': knowledge
                    })
                    st.success("✅ Rating saved!")
                
                # Display existing ratings
                if 'relationship_data' in st.session_state.sat_data and st.session_state.sat_data['relationship_data']:
                    st.subheader("Current Ratings")
                    df = pd.DataFrame(st.session_state.sat_data['relationship_data'])
                    st.dataframe(df, use_container_width=True)
        else:
            st.warning("⚠️ Please complete SIT first to identify stakeholders.")
    
    with tab2:
        st.markdown('<p class="step-header">Step 2: Stakeholder Management Tool</p>', unsafe_allow_html=True)
        st.info("Visualize stakeholders on Power vs Interest, Power vs Legitimacy, and Power vs Urgency.")
        
        if 'relationship_data' in st.session_state.sat_data and st.session_state.sat_data['relationship_data']:
            df = pd.DataFrame(st.session_state.sat_data['relationship_data'])
            
            chart_type = st.selectbox("Select Comparison", 
                                     ["Power vs Interest", "Power vs Legitimacy", "Power vs Urgency"])
            
            if chart_type == "Power vs Interest":
                fig = px.scatter(df, x='power', y='interest', 
                               text='stakeholder',
                               title='Power vs Interest Matrix')
            elif chart_type == "Power vs Legitimacy":
                fig = px.scatter(df, x='power', y='legitimacy',
                               text='stakeholder',
                               title='Power vs Legitimacy Matrix')
            else:
                fig = px.scatter(df, x='power', y='urgency',
                               text='stakeholder',
                               title='Power vs Urgency Matrix')
            
            fig.update_traces(textposition='top center')
            fig.update_layout(height=500)
            
            # Add quadrant lines
            fig.add_hline(y=5, line_dash="dash", line_color="gray")
            fig.add_vline(x=5, line_dash="dash", line_color="gray")
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Strategy recommendations
            st.subheader("Management Strategies")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **High Power, High Interest:**
                - Manage Closely
                - Key Players
                """)
                st.markdown("""
                **High Power, Low Interest:**
                - Keep Satisfied
                - Important but passive
                """)
            
            with col2:
                st.markdown("""
                **Low Power, High Interest:**
                - Keep Informed
                - Show consideration
                """)
                st.markdown("""
                **Low Power, Low Interest:**
                - Monitor
                - Minimal effort
                """)
        else:
            st.warning("⚠️ Please complete Step 1 to rate stakeholders.")
    
    with tab3:
        st.markdown('<p class="step-header">Step 3: Conflict Resolution Strategy</p>', unsafe_allow_html=True)
        st.info("Identify conflict resolution approaches based on cooperativeness vs competition.")
        
        if 'relationship_data' in st.session_state.sat_data and st.session_state.sat_data['relationship_data']:
            st.subheader("Identify Stakeholder Conflicts")
            
            stakeholders = [item['stakeholder'] for item in st.session_state.sat_data['relationship_data']]
            
            selected_sh = st.selectbox("Select Stakeholder for Conflict Analysis", stakeholders)
            
            cooperativeness = st.slider("Cooperativeness Level", 1, 10, 5)
            competitiveness = st.slider("Competitiveness Level", 1, 10, 5)
            
            conflict_description = st.text_area("Describe potential conflicts")
            
            if st.button("Add Conflict Strategy"):
                if 'conflict_data' not in st.session_state.sat_data:
                    st.session_state.sat_data['conflict_data'] = []
                
                st.session_state.sat_data['conflict_data'].append({
                    'stakeholder': selected_sh,
                    'cooperativeness': cooperativeness,
                    'competitiveness': competitiveness,
                    'description': conflict_description
                })
                st.success("✅ Conflict strategy added!")
            
            # Show conflict matrix
            if 'conflict_data' in st.session_state.sat_data and st.session_state.sat_data['conflict_data']:
                df_conflict = pd.DataFrame(st.session_state.sat_data['conflict_data'])
                
                fig = px.scatter(df_conflict, x='competitiveness', y='cooperativeness',
                               text='stakeholder',
                               title='Conflict Resolution Matrix')
                fig.update_traces(textposition='top center')
                fig.add_hline(y=5, line_dash="dash", line_color="gray")
                fig.add_vline(x=5, line_dash="dash", line_color="gray")
                st.plotly_chart(fig, use_container_width=True)
                
                st.markdown("""
                **Strategies:**
                - **High Cooperativeness, Low Competition:** Accommodation
                - **High Cooperativeness, High Competition:** Collaboration
                - **Low Cooperativeness, Low Competition:** Avoidance
                - **Low Cooperativeness, High Competition:** Competition
                - **Moderate Both:** Compromise
                """)
        else:
            st.warning("⚠️ Please complete Step 1 first.")
    
    with tab4:
        st.markdown('<p class="step-header">Step 4: Knowledge and Responsibility Chart</p>', unsafe_allow_html=True)
        st.info("Map knowledge, skills, and responsibilities for each stakeholder group.")
        
        if 'relationship_data' in st.session_state.sat_data and st.session_state.sat_data['relationship_data']:
            st.subheader("Define Knowledge and Responsibilities")
            
            stakeholder_groups = st.multiselect(
                "Select Stakeholder Group",
                ["Key Players", "Keep Satisfied", "Keep Informed", "Monitor"],
                default=["Key Players"]
            )
            
            for group in stakeholder_groups:
                with st.expander(f"📚 {group}"):
                    knowledge_areas = st.text_area(f"Knowledge Areas for {group}", key=f"know_{group}")
                    responsibilities = st.text_area(f"Responsibilities for {group}", key=f"resp_{group}")
                    skills_needed = st.text_area(f"Skills Needed for {group}", key=f"skill_{group}")
                    
                    if st.button(f"Save {group} Data", key=f"btn_{group}"):
                        if 'knowledge_data' not in st.session_state.sat_data:
                            st.session_state.sat_data['knowledge_data'] = {}
                        
                        st.session_state.sat_data['knowledge_data'][group] = {
                            'knowledge': knowledge_areas,
                            'responsibilities': responsibilities,
                            'skills': skills_needed
                        }
                        st.success(f"✅ Data saved for {group}")
            
            # Display summary
            if 'knowledge_data' in st.session_state.sat_data:
                st.subheader("Knowledge & Responsibility Summary")
                for group, data in st.session_state.sat_data['knowledge_data'].items():
                    st.markdown(f"**{group}:**")
                    st.write(f"- Knowledge: {data['knowledge']}")
                    st.write(f"- Responsibilities: {data['responsibilities']}")
                    st.write(f"- Skills: {data['skills']}")
        else:
            st.warning("⚠️ Please complete Step 1 first.")
    
    with tab5:
        st.markdown('<p class="step-header">Step 5: Value Exchange Map</p>', unsafe_allow_html=True)
        st.info("Identify pains, gains, and strategies for training-related product-service systems.")
        
        if 'relationship_data' in st.session_state.sat_data and st.session_state.sat_data['relationship_data']:
            st.subheader("Value Proposition Canvas")
            
            stakeholder = st.selectbox(
                "Select Stakeholder for Value Mapping",
                [item['stakeholder'] for item in st.session_state.sat_data['relationship_data']]
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### Customer Profile")
                pains = st.text_area("Pains (problems, challenges)")
                gains = st.text_area("Gains (desired outcomes, benefits)")
                jobs = st.text_area("Jobs to be Done")
            
            with col2:
                st.markdown("### Value Map")
                pain_relievers = st.text_area("Pain Relievers (how training helps)")
                gain_creators = st.text_area("Gain Creators (benefits provided)")
                products_services = st.text_area("Training Products & Services")
            
            if st.button("Save Value Map"):
                if 'value_map' not in st.session_state.sat_data:
                    st.session_state.sat_data['value_map'] = []
                
                st.session_state.sat_data['value_map'].append({
                    'stakeholder': stakeholder,
                    'pains': pains,
                    'gains': gains,
                    'jobs': jobs,
                    'pain_relievers': pain_relievers,
                    'gain_creators': gain_creators,
                    'products_services': products_services
                })
                st.success("✅ Value map saved!")
            
            # Display existing value maps
            if 'value_map' in st.session_state.sat_data and st.session_state.sat_data['value_map']:
                st.subheader("Saved Value Maps")
                for vm in st.session_state.sat_data['value_map']:
                    with st.expander(f"📊 {vm['stakeholder']}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("**Customer Profile:**")
                            st.write(f"Pains: {vm['pains']}")
                            st.write(f"Gains: {vm['gains']}")
                            st.write(f"Jobs: {vm['jobs']}")
                        with col2:
                            st.markdown("**Value Map:**")
                            st.write(f"Pain Relievers: {vm['pain_relievers']}")
                            st.write(f"Gain Creators: {vm['gain_creators']}")
                            st.write(f"Products/Services: {vm['products_services']}")
        else:
            st.warning("⚠️ Please complete Step 1 first.")

# MAT - Market Analysis Toolkit
elif menu == "3️⃣ MAT - Market Analysis":
    st.markdown('<div class="main-header">MAT - Market Analysis Toolkit</div>', unsafe_allow_html=True)
    
    st.markdown("""
    MAT ensures that training programs align with market demands and opportunities through comprehensive market analysis.
    """)
    
    mat_tools = st.selectbox("Select Analysis Tool", [
        "PESTEL Analysis",
        "Gap Analysis",
        "Behavioral Segmentation",
        "User Persona",
        "Customer Journey Map",
        "Mystery Shopping",
        "Complaint Data Analysis",
        "Brand Audit"
    ])
    
    if mat_tools == "PESTEL Analysis":
        st.subheader("PESTEL Analysis")
        st.info("Analyze Political, Economic, Social, Technological, Environmental, and Legal factors.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            political = st.text_area(
                "Political Factors",
                placeholder="e.g., PM Vishwakarma scheme offers 15% subsidy on raw materials"
            )
            economic = st.text_area(
                "Economic Factors",
                placeholder="e.g., Rising demand for handmade products in urban markets"
            )
            social = st.text_area(
                "Social Factors",
                placeholder="e.g., Growing appreciation for traditional crafts among youth"
            )
        
        with col2:
            technological = st.text_area(
                "Technological Factors",
                placeholder="e.g., E-commerce platforms enabling direct sales"
            )
            environmental = st.text_area(
                "Environmental Factors",
                placeholder="e.g., Preference for sustainable, eco-friendly products"
            )
            legal = st.text_area(
                "Legal Factors",
                placeholder="e.g., GI tag protection for regional crafts"
            )
        
        if st.button("Save PESTEL Analysis"):
            st.session_state.mat_data['pestel'] = {
                'political': political,
                'economic': economic,
                'social': social,
                'technological': technological,
                'environmental': environmental,
                'legal': legal,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.success("✅ PESTEL Analysis saved!")
    
    elif mat_tools == "Gap Analysis":
        st.subheader("Gap Analysis")
        st.info("Identify the gap between current state and desired future state.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            current_state = st.text_area(
                "Current State",
                placeholder="e.g., Market for handmade wedding invitations sees very seasonal demand"
            )
            current_strengths = st.text_area("Current Strengths")
            current_weaknesses = st.text_area("Current Weaknesses")
        
        with col2:
            desired_state = st.text_area(
                "Desired Future State",
                placeholder="e.g., Year-round consistent demand with diversified product line"
            )
            opportunities = st.text_area("Opportunities")
            threats = st.text_area("Threats")
        
        action_plan = st.text_area("Action Plan to Bridge the Gap")
        
        if st.button("Save Gap Analysis"):
            st.session_state.mat_data['gap'] = {
                'current_state': current_state,
                'current_strengths': current_strengths,
                'current_weaknesses': current_weaknesses,
                'desired_state': desired_state,
                'opportunities': opportunities,
                'threats': threats,
                'action_plan': action_plan,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.success("✅ Gap Analysis saved!")
    
    elif mat_tools == "Behavioral Segmentation":
        st.subheader("Behavioral Segmentation")
        st.info("Segment customers based on purchasing behavior, usage, and benefits sought.")
        
        segment_name = st.text_input("Segment Name")
        
        col1, col2 = st.columns(2)
        
        with col1:
            purchase_behavior = st.text_area("Purchase Behavior")
            usage_rate = st.text_area("Usage Rate")
        
        with col2:
            benefits_sought = st.text_area("Benefits Sought")
            loyalty_status = st.text_area("Loyalty Status")
        
        occasion = st.text_area("Purchase Occasion")
        
        if st.button("Add Segment"):
            if 'behavioral_segments' not in st.session_state.mat_data:
                st.session_state.mat_data['behavioral_segments'] = []
            
            st.session_state.mat_data['behavioral_segments'].append({
                'name': segment_name,
                'purchase_behavior': purchase_behavior,
                'usage_rate': usage_rate,
                'benefits_sought': benefits_sought,
                'loyalty_status': loyalty_status,
                'occasion': occasion
            })
            st.success(f"✅ Segment '{segment_name}' added!")
        
        # Display segments
        if 'behavioral_segments' in st.session_state.mat_data:
            st.subheader("Customer Segments")
            for seg in st.session_state.mat_data['behavioral_segments']:
                with st.expander(f"👥 {seg['name']}"):
                    st.write(f"**Purchase Behavior:** {seg['purchase_behavior']}")
                    st.write(f"**Usage Rate:** {seg['usage_rate']}")
                    st.write(f"**Benefits Sought:** {seg['benefits_sought']}")
                    st.write(f"**Loyalty Status:** {seg['loyalty_status']}")
                    st.write(f"**Occasion:** {seg['occasion']}")
    
    elif mat_tools == "User Persona":
        st.subheader("User Persona")
        st.info("Create detailed profiles of typical customers.")
        
        persona_name = st.text_input("Persona Name")
        
        col1, col2 = st.columns(2)
        
        with col1:
            age_range = st.text_input("Age Range")
            occupation = st.text_input("Occupation")
            location = st.text_input("Location")
            income_level = st.text_input("Income Level")
        
        with col2:
            education = st.text_input("Education Level")
            family_status = st.text_input("Family Status")
            lifestyle = st.text_input("Lifestyle")
        
        goals = st.text_area("Goals & Motivations")
        pain_points = st.text_area("Pain Points & Frustrations")
        shopping_habits = st.text_area("Shopping Habits")
        
        if st.button("Save Persona"):
            if 'personas' not in st.session_state.mat_data:
                st.session_state.mat_data['personas'] = []
            
            st.session_state.mat_data['personas'].append({
                'name': persona_name,
                'age_range': age_range,
                'occupation': occupation,
                'location': location,
                'income_level': income_level,
                'education': education,
                'family_status': family_status,
                'lifestyle': lifestyle,
                'goals': goals,
                'pain_points': pain_points,
                'shopping_habits': shopping_habits
            })
            st.success(f"✅ Persona '{persona_name}' created!")
        
        # Display personas
        if 'personas' in st.session_state.mat_data:
            st.subheader("Created Personas")
            for persona in st.session_state.mat_data['personas']:
                with st.expander(f"👤 {persona['name']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Demographics:**")
                        st.write(f"- Age: {persona['age_range']}")
                        st.write(f"- Occupation: {persona['occupation']}")
                        st.write(f"- Location: {persona['location']}")
                        st.write(f"- Income: {persona['income_level']}")
                    with col2:
                        st.write(f"**Psychographics:**")
                        st.write(f"- Education: {persona['education']}")
                        st.write(f"- Family: {persona['family_status']}")
                        st.write(f"- Lifestyle: {persona['lifestyle']}")
                    st.write(f"**Goals:** {persona['goals']}")
                    st.write(f"**Pain Points:** {persona['pain_points']}")
                    st.write(f"**Shopping Habits:** {persona['shopping_habits']}")
    
    elif mat_tools == "Customer Journey Map":
        st.subheader("Customer Journey Map")
        st.info("Map the customer's experience from awareness to post-purchase.")
        
        stages = ["Awareness", "Consideration", "Purchase", "Usage", "Loyalty"]
        
        journey_data = {}
        for stage in stages:
            with st.expander(f"📍 {stage}"):
                journey_data[stage] = {
                    'touchpoints': st.text_area(f"Touchpoints in {stage}", key=f"tp_{stage}"),
                    'actions': st.text_area(f"Customer Actions", key=f"act_{stage}"),
                    'emotions': st.text_area(f"Emotions/Thoughts", key=f"emo_{stage}"),
                    'pain_points': st.text_area(f"Pain Points", key=f"pain_{stage}"),
                    'opportunities': st.text_area(f"Opportunities for Improvement", key=f"opp_{stage}")
                }
        
        if st.button("Save Customer Journey"):
            st.session_state.mat_data['customer_journey'] = journey_data
            st.success("✅ Customer Journey Map saved!")
    
    elif mat_tools == "Mystery Shopping":
        st.subheader("Mystery Shopping")
        st.info("Evaluate customer experience by acting as a customer.")
        
        location = st.text_input("Location Evaluated")
        date = st.date_input("Date of Visit")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Store/Online Experience:**")
            ambiance = st.slider("Ambiance/Interface", 1, 10, 5)
            accessibility = st.slider("Accessibility", 1, 10, 5)
            product_display = st.slider("Product Display", 1, 10, 5)
        
        with col2:
            st.markdown("**Service Quality:**")
            staff_behavior = st.slider("Staff Behavior", 1, 10, 5)
            product_knowledge = st.slider("Product Knowledge", 1, 10, 5)
            response_time = st.slider("Response Time", 1, 10, 5)
        
        observations = st.text_area("Detailed Observations")
        recommendations = st.text_area("Recommendations for Improvement")
        
        if st.button("Save Mystery Shopping Report"):
            if 'mystery_shopping' not in st.session_state.mat_data:
                st.session_state.mat_data['mystery_shopping'] = []
            
            st.session_state.mat_data['mystery_shopping'].append({
                'location': location,
                'date': str(date),
                'ambiance': ambiance,
                'accessibility': accessibility,
                'product_display': product_display,
                'staff_behavior': staff_behavior,
                'product_knowledge': product_knowledge,
                'response_time': response_time,
                'observations': observations,
                'recommendations': recommendations
            })
            st.success("✅ Mystery Shopping Report saved!")
    
    elif mat_tools == "Complaint Data Analysis":
        st.subheader("Complaint Data Analysis")
        st.info("Analyze customer complaints to identify patterns and improvement areas.")
        
        complaint_source = st.text_input("Complaint Source")
        complaint_date = st.date_input("Date Received")
        
        complaint_category = st.selectbox(
            "Complaint Category",
            ["Product Quality", "Service", "Delivery", "Pricing", "Communication", "Other"]
        )
        
        complaint_description = st.text_area("Complaint Description")
        severity = st.select_slider("Severity", options=["Low", "Medium", "High", "Critical"])
        
        resolution_status = st.selectbox("Resolution Status", 
                                        ["Pending", "In Progress", "Resolved", "Closed"])
        resolution_details = st.text_area("Resolution Details")
        
        if st.button("Add Complaint"):
            if 'complaints' not in st.session_state.mat_data:
                st.session_state.mat_data['complaints'] = []
            
            st.session_state.mat_data['complaints'].append({
                'source': complaint_source,
                'date': str(complaint_date),
                'category': complaint_category,
                'description': complaint_description,
                'severity': severity,
                'status': resolution_status,
                'resolution': resolution_details
            })
            st.success("✅ Complaint logged!")
        
        # Analysis
        if 'complaints' in st.session_state.mat_data and st.session_state.mat_data['complaints']:
            st.subheader("Complaint Analysis")
            
            df_complaints = pd.DataFrame(st.session_state.mat_data['complaints'])
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Category distribution
                category_counts = df_complaints['category'].value_counts()
                fig_cat = px.pie(values=category_counts.values, 
                               names=category_counts.index,
                               title="Complaints by Category")
                st.plotly_chart(fig_cat, use_container_width=True)
            
            with col2:
                # Severity distribution
                severity_counts = df_complaints['severity'].value_counts()
                fig_sev = px.bar(x=severity_counts.index, 
                               y=severity_counts.values,
                               title="Complaints by Severity")
                st.plotly_chart(fig_sev, use_container_width=True)
    
    elif mat_tools == "Brand Audit":
        st.subheader("Brand Audit")
        st.info("Evaluate brand perception, positioning, and performance.")
        
        st.markdown("### Brand Identity")
        col1, col2 = st.columns(2)
        
        with col1:
            brand_mission = st.text_area("Brand Mission")
            brand_vision = st.text_area("Brand Vision")
            brand_values = st.text_area("Brand Values")
        
        with col2:
            unique_selling_proposition = st.text_area("Unique Selling Proposition")
            brand_personality = st.text_area("Brand Personality")
            brand_promise = st.text_area("Brand Promise")
        
        st.markdown("### Brand Performance")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            brand_awareness = st.slider("Brand Awareness", 1, 10, 5)
            brand_recognition = st.slider("Brand Recognition", 1, 10, 5)
        
        with col2:
            brand_loyalty = st.slider("Brand Loyalty", 1, 10, 5)
            customer_satisfaction = st.slider("Customer Satisfaction", 1, 10, 5)
        
        with col3:
            market_position = st.slider("Market Position", 1, 10, 5)
            brand_consistency = st.slider("Brand Consistency", 1, 10, 5)
        
        strengths = st.text_area("Brand Strengths")
        weaknesses = st.text_area("Brand Weaknesses")
        recommendations = st.text_area("Strategic Recommendations")
        
        if st.button("Save Brand Audit"):
            st.session_state.mat_data['brand_audit'] = {
                'brand_mission': brand_mission,
                'brand_vision': brand_vision,
                'brand_values': brand_values,
                'usp': unique_selling_proposition,
                'personality': brand_personality,
                'promise': brand_promise,
                'awareness': brand_awareness,
                'recognition': brand_recognition,
                'loyalty': brand_loyalty,
                'satisfaction': customer_satisfaction,
                'position': market_position,
                'consistency': brand_consistency,
                'strengths': strengths,
                'weaknesses': weaknesses,
                'recommendations': recommendations,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.success("✅ Brand Audit saved!")

# Summary & Export
elif menu == "📊 Summary & Export":
    st.markdown('<div class="main-header">Summary & Export</div>', unsafe_allow_html=True)
    
    st.subheader("📋 Data Collection Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("SIT - Stakeholders Identified", 
                 len(st.session_state.sit_data.get('stakeholders', [])))
        if st.session_state.sit_data.get('roles'):
            total_actors = sum(len(actors) for actors in st.session_state.sit_data['roles'].values())
            st.metric("Total Actors Mapped", total_actors)
    
    with col2:
        sat_metrics = 0
        if 'relationship_data' in st.session_state.sat_data:
            sat_metrics = len(st.session_state.sat_data['relationship_data'])
        st.metric("SAT - Stakeholders Analyzed", sat_metrics)
        
        value_maps = 0
        if 'value_map' in st.session_state.sat_data:
            value_maps = len(st.session_state.sat_data['value_map'])
        st.metric("Value Maps Created", value_maps)
    
    with col3:
        mat_tools_completed = len(st.session_state.mat_data)
        st.metric("MAT - Tools Completed", mat_tools_completed)
    
    st.markdown("---")
    
    # Export options
    st.subheader("📥 Export Data")
    
    export_format = st.radio("Select Export Format", ["JSON", "Excel"])
    
    if st.button("Generate Export File"):
        if export_format == "JSON":
            # Prepare data for JSON export
            export_data = {
                'sit_data': st.session_state.sit_data,
                'sat_data': st.session_state.sat_data,
                'mat_data': st.session_state.mat_data,
                'export_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Convert to JSON string
            json_str = json.dumps(export_data, indent=2, default=str)
            
            st.download_button(
                label="📥 Download JSON",
                data=json_str,
                file_name=f"siama_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
        
        elif export_format == "Excel":
            # Create Excel file with multiple sheets
            try:
                import io
                from openpyxl import Workbook
                from openpyxl.styles import Font, PatternFill
                
                wb = Workbook()
                
                # SIT Sheet
                ws_sit = wb.active
                ws_sit.title = "SIT Data"
                ws_sit['A1'] = "Stakeholder Identification Data"
                ws_sit['A1'].font = Font(bold=True, size=14)
                
                row = 3
                ws_sit[f'A{row}'] = "Role"
                ws_sit[f'B{row}'] = "Actor Name"
                ws_sit[f'C{row}'] = "Location"
                ws_sit[f'D{row}'] = "Contact"
                
                row += 1
                for role, actors in st.session_state.sit_data.get('roles', {}).items():
                    for actor in actors:
                        ws_sit[f'A{row}'] = role
                        ws_sit[f'B{row}'] = actor.get('name', '')
                        ws_sit[f'C{row}'] = actor.get('location', '')
                        ws_sit[f'D{row}'] = actor.get('contact', '')
                        row += 1
                
                # SAT Sheet
                if 'relationship_data' in st.session_state.sat_data:
                    ws_sat = wb.create_sheet("SAT Data")
                    ws_sat['A1'] = "Stakeholder Analysis Data"
                    ws_sat['A1'].font = Font(bold=True, size=14)
                    
                    df_sat = pd.DataFrame(st.session_state.sat_data['relationship_data'])
                    
                    for r_idx, row in enumerate(df_sat.values, start=3):
                        for c_idx, value in enumerate(row, start=1):
                            ws_sat.cell(row=r_idx, column=c_idx, value=str(value))
                
                # MAT Sheet
                ws_mat = wb.create_sheet("MAT Data")
                ws_mat['A1'] = "Market Analysis Data"
                ws_mat['A1'].font = Font(bold=True, size=14)
                
                row = 3
                for tool, data in st.session_state.mat_data.items():
                    ws_mat[f'A{row}'] = tool
                    ws_mat[f'A{row}'].font = Font(bold=True)
                    row += 1
                    
                    if isinstance(data, dict):
                        for key, value in data.items():
                            ws_mat[f'A{row}'] = str(key)
                            ws_mat[f'B{row}'] = str(value)
                            row += 1
                    row += 1
                
                # Save to BytesIO
                excel_buffer = io.BytesIO()
                wb.save(excel_buffer)
                excel_buffer.seek(0)
                
                st.download_button(
                    label="📥 Download Excel",
                    data=excel_buffer,
                    file_name=f"siama_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            except Exception as e:
                st.error(f"Error creating Excel file: {e}")
    
    st.markdown("---")
    
    # Training Recommendations
    st.subheader("🎯 Training Program Recommendations")
    
    if st.button("Generate Recommendations"):
        st.markdown("""
        ### Based on Your SIAMA Analysis:
        
        #### **Key Findings:**
        """)
        
        # SIT findings
        if st.session_state.sit_data.get('roles'):
            st.markdown("**Stakeholder Landscape:**")
            for role, actors in st.session_state.sit_data['roles'].items():
                st.write(f"- {role}: {len(actors)} actors identified")
        
        # SAT findings
        if 'relationship_data' in st.session_state.sat_data:
            st.markdown("**Stakeholder Analysis:**")
            df = pd.DataFrame(st.session_state.sat_data['relationship_data'])
            high_power_high_interest = len(df[(df['power'] > 5) & (df['interest'] > 5)])
            st.write(f"- {high_power_high_interest} key stakeholders requiring close management")
        
        # MAT findings
        if st.session_state.mat_data:
            st.markdown("**Market Insights:**")
            st.write(f"- {len(st.session_state.mat_data)} market analysis tools completed")
        
        st.markdown("""
        #### **Recommended Training Focus Areas:**
        
        1. **Technical Skills Development**
           - Based on identified gaps in producer capabilities
           - Focus on quality improvement and efficiency
        
        2. **Business & Entrepreneurship**
           - Market understanding and customer engagement
           - Pricing strategies and financial management
        
        3. **Digital Literacy**
           - E-commerce platform usage
           - Social media marketing
           - Digital payment systems
        
        4. **Stakeholder Collaboration**
           - Building effective supplier relationships
           - Customer relationship management
           - Networking with marketers and buyers
        
        5. **Design & Innovation**
           - Contemporary market trends
           - Product diversification
           - Maintaining cultural authenticity while innovating
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>SIAMA Toolbox v1.0 | Developed for Craft Education Planning in India</p>
    <p>Based on research by Kumar et al., IIT Guwahati</p>
</div>
""", unsafe_allow_html=True)
