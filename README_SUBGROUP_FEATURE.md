# Subgroup Feature for SIAMA SAT Step 2

## Overview
A comprehensive subgroup management tool has been successfully integrated into the SIAMA Streamlit application, specifically within **SAT (Stakeholder Analysis Toolkit) Step 2**. This feature replicates and enhances the subgroup functionality from the SIAMA 3 Excel file.

## What's New

### Location
**SAT → Step 2: Management Tool → Subgroup Management Tab**

### Core Features
1. **Subgroup Creation** - Define custom stakeholder groups
2. **Member Assignment** - Organize stakeholders into subgroups
3. **Aggregated Analysis** - Automatic calculation of group metrics
4. **Visual Profiles** - Radar charts showing subgroup characteristics
5. **Strategic Recommendations** - AI-driven engagement strategies

## Quick Access

### Files Created
- `siama_app.py` (modified) - Main application with subgroup feature
- `SUBGROUP_FEATURE_GUIDE.md` - Complete feature documentation
- `QUICKSTART_SUBGROUPS.md` - 5-minute tutorial
- `IMPLEMENTATION_SUMMARY.md` - Technical implementation details
- `README_SUBGROUP_FEATURE.md` - This file

### Running the Application
```bash
cd /Users/sharmisthabanerjee/Desktop/siama
streamlit run siama_app.py
```

## Key Capabilities

### 1. Flexible Grouping
Organize stakeholders by:
- Geographic location (Local/Regional/National)
- Functional role (Suppliers/Producers/Buyers)
- Priority level (High/Medium/Low)
- Training needs (Beginner/Intermediate/Advanced)
- Or any custom criteria

### 2. Automated Analytics
For each subgroup, automatically calculate:
- Average Power rating
- Average Interest level
- Average Legitimacy score
- Average Urgency rating

### 3. Visual Analysis
- **Radar Charts**: Visual profile of subgroup characteristics
- **Data Tables**: Detailed member information
- **Summary Cards**: Quick metrics overview

### 4. Strategic Insights
Automated recommendations based on:
- **High Power + High Interest** → Manage Closely
- **High Power + Low Interest** → Keep Satisfied
- **Low Power + High Interest** → Keep Informed
- **Low Power + Low Interest** → Monitor

## How It Works

### User Workflow
```
1. Create Subgroups
   Enter name and description → Click Add

2. Assign Stakeholders
   Select stakeholder → Choose subgroup → Assign

3. Analyze Results
   Select subgroup → View metrics, charts, and recommendations

4. Export Data
   All subgroup data included in JSON/Excel exports
```

### Data Flow
```
SAT Step 1 (Rating) → SAT Step 2 (Grouping) → Analysis → Strategy
```

## Comparison: Excel vs Streamlit

| Feature | Excel (SIAMA 3) | Streamlit (New) |
|---------|----------------|-----------------|
| Subgroup Creation | Manual column entry | User-friendly interface |
| Naming | Numbers (1,2,3...) | Descriptive names |
| Assignment | Enter numbers | Click-based selection |
| Calculation | SUMIFS formulas | Automatic pandas |
| Visualization | Limited charts | Interactive Plotly |
| Flexibility | Fixed structure | Dynamic creation |
| User Experience | Formula knowledge needed | No technical skills required |

## Benefits

### For Trainers
- Design targeted training programs for specific stakeholder groups
- Allocate resources based on group priorities
- Customize content for different skill levels

### For Researchers
- Segment stakeholders for analysis
- Compare group characteristics
- Identify patterns and trends

### For Organizations
- Strategic stakeholder engagement
- Priority-based resource allocation
- Clear communication strategies

## Example Use Cases

### Case 1: Craft Training Program
**Subgroups:**
- Rural Artisans (High Interest, Low Power)
- Urban Retailers (High Power, High Interest)
- Raw Material Suppliers (Medium Power, Low Interest)
- Government Partners (High Power, Medium Interest)

**Strategy:**
- Intensive training for Rural Artisans
- Partnership development with Urban Retailers
- Basic engagement with Suppliers
- Regular updates to Government Partners

### Case 2: Market Expansion
**Subgroups:**
- Local Market (Direct sales focus)
- Regional Market (Distribution channels)
- National Market (E-commerce platforms)
- International Market (Export standards)

**Analysis:**
- Compare power/interest across markets
- Prioritize high-potential segments
- Tailor marketing strategies

## Technical Details

### Implementation
- **Framework**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Plotly
- **State Management**: Streamlit session state

### Integration Points
- Reads from SAT Step 1 stakeholder ratings
- Stores data in session state
- Exports via Summary & Export module
- Compatible with existing SIAMA workflow

### Code Structure
```python
st.session_state.sat_data = {
    'relationship_data': [...],  # From Step 1
    'subgroups': {
        'Subgroup Name': {
            'description': '...',
            'members': [...]
        }
    },
    'subgroup_assignments': {
        'Stakeholder': 'Subgroup'
    }
}
```

## Documentation

### For Users
- **QUICKSTART_SUBGROUPS.md** - 5-minute tutorial
- **SUBGROUP_FEATURE_GUIDE.md** - Complete user guide

### For Developers
- **IMPLEMENTATION_SUMMARY.md** - Technical implementation
- **siama_app.py:417-659** - Source code

## Future Enhancements

Potential additions:
- Bulk assignment (multiple stakeholders at once)
- Subgroup comparison dashboard
- Predefined subgroup templates
- Import/export subgroup definitions
- Historical tracking of subgroup changes
- Cross-subgroup relationship mapping

## Support & Resources

### Getting Help
1. Read the QuickStart guide
2. Check the Feature Guide for detailed instructions
3. Review the Implementation Summary for technical details
4. Refer to SIAMA 3 Excel file for original concept

### Feedback
If you encounter issues or have suggestions:
- Document the issue
- Note the steps to reproduce
- Include screenshots if applicable
- Share your use case for context

## Conclusion

The subgroup management feature successfully brings the Excel-based subgroup functionality into the Streamlit SIAMA application with significant improvements in usability, flexibility, and visual analysis. Users can now easily segment stakeholders, analyze group characteristics, and develop targeted strategies for craft education planning.

---

**Version**: 1.0
**Date**: December 2024
**Status**: ✅ Complete and Ready for Use
**Framework**: Streamlit + Pandas + Plotly
**Location**: SAT Step 2 - Subgroup Management Tab
