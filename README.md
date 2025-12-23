# SIAMA Toolbox - Streamlit Application

## Overview

The **SIAMA Toolbox** (Stakeholder Identification, Analysis, and Market Assessment) is an integrated digital platform designed to systematize craft education planning in India. This Streamlit application implements the complete framework developed through comprehensive research with craft trainers, training organizations, and artisans across India.

## Purpose

The SIAMA toolbox addresses the critical question: **"How can trainers and training organizations be aided in studying crafts and artisans to understand their contextually different needs for appropriate training in India?"**

### Two Foundational Questions

1. **What should we teach?**
   - Addressed through market study components and artisan's prior skill, knowledge, and aspirations

2. **Whom should we teach?**
   - Explored via stakeholder identification and analysis tools

## The Three Toolkits

### 1. Stakeholder Identification Toolkit (SIT)
**4 Sequential Steps:**
- **Step 1:** Predefined Roles and Questionnaires Tool
- **Step 2:** Role × Actor Database
- **Step 3:** Role Card Visualization
- **Step 4:** Role Map

**Purpose:** Identifies all individuals, groups, and organizations in the craft value chain (Supplier → Producer → Refiner → Marketer → Buyer)

### 2. Stakeholder Analysis Toolkit (SAT)
**5 Sequential Tools:**
- **Step 1:** Stakeholder Relationship Matrix
- **Step 2:** Stakeholder Management Tool
- **Step 3:** Conflict Resolution Strategy
- **Step 4:** Knowledge and Responsibility Chart
- **Step 5:** Value Exchange Map

**Purpose:** Evaluates stakeholder roles, interests, influences, and develops management strategies based on Power, Interest, Legitimacy, and Urgency

### 3. Market Analysis Toolkit (MAT)
**8 Analysis Tools:**
- PESTEL Analysis
- Gap Analysis
- Behavioral Segmentation
- User Persona
- Customer Journey Map
- Mystery Shopping
- Complaint Data Analysis
- Brand Audit

**Purpose:** Ensures training programs align with market demands and opportunities

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Install required packages:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
streamlit run siama_app.py
```

3. **Access the app:**
   - The application will automatically open in your default web browser
   - Default URL: http://localhost:8501

## How to Use

### Getting Started

1. **Start with the Home Page**
   - Read the overview and understand the three toolkits
   - Review the foundational questions that guide the framework

2. **Navigate Through the Toolkits Sequentially**

### SIT - Stakeholder Identification Workflow

1. **Step 1: Predefined Roles & Questionnaires**
   - Select a role (Supplier, Producer, Refiner, Marketer, Buyer)
   - Answer primary questionnaires
   - Complete secondary questionnaires for deeper insights
   - Save stakeholder data

2. **Step 2: Role × Actor Database**
   - View collected stakeholder data
   - Add detailed actor information (name, location, contact, details)
   - Build your stakeholder database

3. **Step 3: Role Card**
   - Visualize stakeholders clustered by role
   - View distribution of actors across roles
   - Review actor details by role category

4. **Step 4: Role Map**
   - See the complete supply chain visualization
   - Understand flow of products, money, and information
   - Identify gaps in the value chain

### SAT - Stakeholder Analysis Workflow

1. **Step 1: Relationship Matrix**
   - Rate stakeholders on:
     - Power (ability to influence outcomes)
     - Interest (level of concern/stake)
     - Legitimacy (validity of involvement)
     - Urgency (immediacy of demands)
   - Document relationships, tasks, and knowledge sharing

2. **Step 2: Management Tool**
   - Visualize stakeholders on comparison matrices:
     - Power vs Interest
     - Power vs Legitimacy
     - Power vs Urgency
   - Apply appropriate management strategies for each quadrant

3. **Step 3: Conflict Resolution**
   - Assess cooperativeness vs competitiveness
   - Identify potential conflicts
   - Develop resolution strategies (Collaboration, Compromise, Accommodation, etc.)

4. **Step 4: Knowledge & Responsibility Chart**
   - Define knowledge areas for stakeholder groups
   - Map responsibilities
   - Identify required skills

5. **Step 5: Value Exchange Map**
   - Create value proposition canvas
   - Identify pains and gains
   - Develop pain relievers and gain creators
   - Design training-related product-service systems

### MAT - Market Analysis Workflow

Complete one or more tools based on your needs:

1. **PESTEL Analysis**
   - Analyze Political, Economic, Social, Technological, Environmental, Legal factors
   - Use contextual hints (e.g., "PM Vishwakarma scheme offers 15% subsidy")

2. **Gap Analysis**
   - Document current state vs desired future state
   - Identify strengths, weaknesses, opportunities, threats
   - Develop action plans

3. **Behavioral Segmentation**
   - Create customer segments based on behavior
   - Analyze purchase behavior, usage, benefits sought

4. **User Persona**
   - Build detailed customer profiles
   - Include demographics, psychographics, goals, pain points

5. **Customer Journey Map**
   - Map journey from Awareness → Consideration → Purchase → Usage → Loyalty
   - Identify touchpoints, emotions, and opportunities

6. **Mystery Shopping**
   - Evaluate customer experience
   - Rate ambiance, accessibility, service quality
   - Provide improvement recommendations

7. **Complaint Data Analysis**
   - Log and categorize complaints
   - Analyze patterns by category and severity
   - Track resolution status

8. **Brand Audit**
   - Evaluate brand identity (mission, vision, values)
   - Assess brand performance metrics
   - Develop strategic recommendations

### Exporting Your Work

Navigate to **Summary & Export** to:
- View data collection summary
- See completion metrics for all toolkits
- Export data in JSON or Excel format
- Generate training program recommendations

## Key Features

### 🎯 User-Friendly Design
- Intuitive interface with clear navigation
- Step-by-step guided workflow
- Contextual help and hints throughout

### 📊 Interactive Visualizations
- Stakeholder distribution charts
- Power-Interest matrices
- Supply chain flow diagrams
- Complaint analysis graphs

### 💾 Data Persistence
- Session-based data storage
- Progress saved within browsing session
- Export capabilities for long-term storage

### 📥 Export Options
- **JSON Format:** Complete data export for integration with other systems
- **Excel Format:** Multi-sheet workbook with organized data tables

### 🎓 Educational Support
- Integrated examples and hints
- Tool descriptions and purposes
- Best practice recommendations

## Research Background

This toolbox is based on comprehensive research conducted with:
- 31 trainers
- 1 designer cum trainer
- 14 administrative staff
- 195 artisans
- 7 craft training organizations across Eastern and Northeastern India

**Research Team:** Shivram Kumar, Jeevan Jolly, Aditya Pratap Singh, Viknesh Surya, Thanush Mardani, Samhita Lokesh, Amey Karekar, Prajwal Kuwar, Sharmistha Banerjee

**Institution:** Department of Design, Indian Institute of Technology, Guwahati

## Design Principles

The SIAMA toolbox was designed to be:
1. **Non-collaborative or minimally collaborative** - Can be used by individual trainers
2. **Intuitive and lightweight** - Quick to understand and use
3. **Non-technical language** - Accessible regardless of analytical expertise
4. **Quick implementation** - Optimized for time-constrained trainers
5. **Context-specific** - Tailored for India's craft sector

## Target Users

- Craft trainers and instructors
- Training organization administrators
- Curriculum developers
- Craft education policymakers
- NGOs working in craft sector development
- Government vocational training institutions

## Alignment with Policy

The SIAMA toolbox aligns with:
- **India's National Education Policy 2020**
- **Skill India Mission** objectives
- **PM Vishwakarma Scheme** for traditional artisans

## Technical Architecture

### Built With
- **Streamlit:** Web application framework
- **Pandas:** Data manipulation and analysis
- **Plotly:** Interactive visualizations
- **OpenPyXL:** Excel file generation

### Browser Compatibility
- Chrome (Recommended)
- Firefox
- Safari
- Edge

## Data Privacy

- All data is stored locally in the browser session
- No data is transmitted to external servers
- Export files are generated client-side
- Recommended: Save exports regularly to prevent data loss

## Troubleshooting

### Application won't start
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Run with verbose output
streamlit run siama_app.py --logger.level=debug
```

### Data not saving
- Ensure you click "Save" buttons after data entry
- Do not refresh the browser without exporting data
- Use Export feature regularly to backup progress

### Visualizations not displaying
- Update Plotly: `pip install plotly --upgrade`
- Clear browser cache
- Try a different browser

## Future Enhancements

Based on testing feedback, future versions will include:
- Further simplification of SAT tools
- Condensation of MAT into fewer integrated tools
- Cloud-based data storage
- Multi-user collaboration features
- Automated curriculum generation
- Integration with existing training management systems

## Support & Feedback

For questions, issues, or suggestions:
- Contact the research team at IIT Guwahati, Department of Design
- Report issues through your organizational channels

## Citation

If you use this toolbox in your research or training programs, please cite:

```
Kumar, S., Jolly, J., Singh, A.P., Surya, V., Mardani, T., Lokesh, S., 
Karekar, A., Kuwar, P., & Banerjee, S. (2024). SIAMA Toolbox: A Systematic 
Approach for Strategizing Craft Education. Department of Design, Indian 
Institute of Technology, Guwahati.
```

## License

This toolbox is developed for educational and research purposes to support craft education in India.

## Acknowledgments

We are grateful to:
- Upendra Maharathi Shilpa Anushandhan Sansthan (UMSAS)
- Northeast Cane and Bamboo Development Council (NECBDC)
- North Eastern Handicrafts & Handlooms Development Corporation Limited (NEHHDC)
- Indian Institute of Entrepreneurship (IIE)
- Khadi & Village Industries Commission (KVIC)
- Antaran Artisan Connect
- Innovate Change Collaborate (ICCO)
- 195 participating artisans
- Expert reviewers and trainers

## Version History

**v1.0 (Current)**
- Initial release with all three toolkits
- SIT: 4-step stakeholder identification
- SAT: 5-step stakeholder analysis
- MAT: 8 market analysis tools
- Export functionality (JSON & Excel)
- Interactive visualizations
- Training recommendations generator

---

**For more information about craft education research at IIT Guwahati, visit the Department of Design website.**
