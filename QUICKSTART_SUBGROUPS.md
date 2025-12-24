# Quick Start Guide: Subgroup Management

## Getting Started

### Prerequisites
Before using the subgroup feature, you must:
1. Complete **SIT (Stakeholder Identification Toolkit)** - identify your stakeholders
2. Complete **SAT Step 1** - rate stakeholders on Power, Interest, Legitimacy, and Urgency

### Launching the App
```bash
streamlit run siama_app.py
```

## 5-Minute Tutorial

### Step 1: Navigate to Subgroup Management (30 seconds)
1. Click on "2️⃣ SAT - Stakeholder Analysis" in the sidebar
2. Go to "Step 2: Management Tool" tab
3. Click on the "👥 Subgroup Management" sub-tab

### Step 2: Create Your First Subgroup (1 minute)
```
Example:
Name: Local Artisans
Description: Traditional craftspeople working in rural areas
```
Click "➕ Add Subgroup"

### Step 3: Create Additional Subgroups (1 minute)
Suggested subgroups for craft education:
- **Local Artisans** - Rural traditional craftspeople
- **Urban Buyers** - City-based customers
- **Raw Material Suppliers** - Material providers
- **Training Organizations** - Education partners

### Step 4: Assign Stakeholders (2 minutes)
1. Select a stakeholder from the dropdown
2. Choose appropriate subgroup
3. Click "Assign Stakeholder to Subgroup"
4. Repeat for all stakeholders

### Step 5: Analyze Subgroups (1 minute)
1. Scroll to "Subgroup Analysis" section
2. Select a subgroup to analyze
3. View:
   - Average scores (Power, Interest, Legitimacy, Urgency)
   - Radar chart showing subgroup profile
   - Member details table
   - Strategic recommendation

## Example Workflow

### Scenario: Craft Training Program Planning

**Stakeholders Identified:**
- Ram (Local Potter)
- Sita (Clay Supplier)
- Urban Store Owner
- Government Official
- NGO Representative
- Online Marketplace

**Subgroups Created:**
1. **Producers** (Ram, other artisans)
2. **Supply Chain** (Sita, suppliers)
3. **Market Partners** (Store Owner, Marketplace)
4. **Support Organizations** (Government, NGO)

**Analysis Results:**
- **Producers**: High Interest (8.5), Medium Power (5.2) → Keep Informed
- **Supply Chain**: Medium Power (6.1), Low Interest (3.8) → Monitor
- **Market Partners**: High Power (7.8), High Interest (8.2) → Manage Closely
- **Support Organizations**: High Power (8.9), Medium Interest (5.5) → Keep Satisfied

**Action Plan:**
- Focus training on Producers (high interest group)
- Collaborate closely with Market Partners for curriculum design
- Keep Support Organizations informed for funding/resources
- Basic engagement with Supply Chain stakeholders

## Tips for Success

### 1. Choose Meaningful Groupings
- Geographic: Local/Regional/National
- Functional: Suppliers/Producers/Buyers
- Priority: High/Medium/Low engagement
- Training needs: Beginner/Intermediate/Advanced

### 2. Keep Subgroups Manageable
- 3-6 subgroups is usually optimal
- Too many subgroups = complexity
- Too few = lack of nuance

### 3. Use Descriptive Names
❌ Bad: "Group 1", "Group 2"
✅ Good: "Rural Artisans", "Urban Retail Partners"

### 4. Review and Update Regularly
- Stakeholder roles can change
- Reassign as needed
- Update descriptions to reflect current purpose

### 5. Compare Subgroups
- Analyze multiple subgroups
- Look for patterns and differences
- Identify which groups need most attention

## Common Use Cases

### Training Program Design
**Subgroups by Skill Level:**
- Beginners → Foundational skills training
- Intermediate → Advanced techniques
- Masters → Business and marketing skills

### Resource Allocation
**Subgroups by Priority:**
- High Priority → Direct engagement, regular meetings
- Medium Priority → Quarterly updates
- Low Priority → Annual check-ins

### Market Segmentation
**Subgroups by Customer Type:**
- Direct Consumers → Product quality focus
- Retailers → Business terms and supply
- Exporters → International standards

### Geographic Strategy
**Subgroups by Location:**
- Local (0-50km) → In-person workshops
- Regional (50-200km) → Monthly visits
- National → Online training programs

## Troubleshooting

**Q: I don't see any stakeholders to assign**
A: Complete SAT Step 1 first to rate stakeholders

**Q: Subgroup analysis shows no data**
A: Ensure you've assigned at least one stakeholder to the subgroup

**Q: How do I delete a subgroup?**
A: Currently, remove all members from a subgroup to effectively deactivate it

**Q: Can a stakeholder be in multiple subgroups?**
A: Currently one subgroup per stakeholder; reassign to move between groups

**Q: Where is my subgroup data saved?**
A: In session state; use Export feature to save permanently

## Next Steps

After creating and analyzing subgroups:
1. Proceed to **SAT Step 3** - Conflict Resolution
2. Use **SAT Step 4** - Knowledge & Responsibility mapping
3. Complete **SAT Step 5** - Value Exchange mapping
4. Export all data via **Summary & Export** menu

## Need Help?

Refer to:
- `SUBGROUP_FEATURE_GUIDE.md` - Detailed feature documentation
- `IMPLEMENTATION_SUMMARY.md` - Technical details
- SIAMA 3 Excel file - Original subgroup tool reference
