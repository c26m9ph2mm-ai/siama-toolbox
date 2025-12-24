# Subgroup Management Feature - SAT Step 2

## Overview
The Subgroup Management tool has been added to SAT (Stakeholder Analysis Toolkit) Step 2, allowing you to organize stakeholders into meaningful groups for targeted analysis and strategy development.

## Features

### 1. Create Subgroups
- Define custom subgroups based on your specific needs
- Add descriptions to clarify the purpose of each subgroup
- Examples of subgroups:
  - Local Artisans
  - Urban Buyers
  - Government Partners
  - NGO Collaborators
  - Raw Material Suppliers
  - Wholesale Distributors

### 2. Assign Stakeholders to Subgroups
- Select any stakeholder from your SAT Step 1 data
- Assign them to one or more subgroups
- Easy reassignment and removal functionality
- View all members of each subgroup at a glance

### 3. Subgroup Analysis
The tool automatically calculates and visualizes:

#### Aggregated Metrics
- **Average Power**: Mean power rating across all subgroup members
- **Average Interest**: Mean interest level of the subgroup
- **Average Legitimacy**: Mean legitimacy score
- **Average Urgency**: Mean urgency rating

#### Visual Analysis
- **Radar Chart**: Visual profile showing the subgroup's overall characteristics
- **Member Details Table**: Complete breakdown of individual stakeholder ratings within the subgroup

#### Strategic Recommendations
Automated strategy suggestions based on the subgroup's average scores:
- **High Power, High Interest**: Manage Closely - Key stakeholder group
- **High Power, Low Interest**: Keep Satisfied - Maintain influence
- **Low Power, High Interest**: Keep Informed - Regular updates
- **Low Power, Low Interest**: Monitor - Basic oversight

## How to Use

### Step 1: Navigate to SAT Step 2
1. Go to the SAT - Stakeholder Analysis section
2. Click on "Step 2: Management Tool"
3. Select the "👥 Subgroup Management" tab

### Step 2: Create Subgroups
1. Enter a descriptive name for your subgroup (e.g., "Local Artisans")
2. Add a description explaining the purpose
3. Click "➕ Add Subgroup"
4. Repeat for all needed subgroups

### Step 3: Assign Stakeholders
1. Select a stakeholder from the dropdown
2. Choose the subgroup to assign them to
3. Click "Assign Stakeholder to Subgroup"
4. View assignments in the "Current Assignments" section
5. Remove stakeholders if needed using the "Remove" button

### Step 4: Analyze Subgroups
1. In the "Subgroup Analysis" section, select a subgroup to analyze
2. Review the aggregated metrics (Power, Interest, Legitimacy, Urgency)
3. Examine the radar chart for visual profile
4. Check member details for individual ratings
5. Read the strategic recommendation for engagement strategy

## Use Cases

### 1. Geographic Segmentation
Create subgroups based on location:
- Local/Regional stakeholders
- National stakeholders
- International stakeholders

### 2. Role-Based Grouping
Organize by function in the value chain:
- Suppliers
- Producers
- Refiners
- Marketers
- Buyers

### 3. Priority-Based Segmentation
Group by engagement priority:
- High Priority Partners
- Medium Priority Contacts
- Low Priority Monitors

### 4. Training Program Design
Segment for tailored training:
- Beginners needing foundational skills
- Intermediate artisans
- Advanced practitioners
- Business owners

## Benefits

1. **Targeted Strategy Development**: Design specific engagement strategies for different stakeholder groups
2. **Resource Allocation**: Prioritize resources based on subgroup characteristics
3. **Training Customization**: Create tailored training programs for different subgroups
4. **Clear Communication**: Understand how to communicate with different stakeholder segments
5. **Efficient Management**: Manage large numbers of stakeholders more effectively

## Data Export

All subgroup data is included in the export functionality:
- JSON export includes full subgroup structure and assignments
- Excel export contains subgroup membership and analysis data
- Access via "📊 Summary & Export" menu

## Technical Implementation

The subgroup tool mirrors the functionality from the SIAMA 3 Excel file:
- Uses SUMIFS-style aggregation for subgroup metrics
- Maintains stakeholder-to-subgroup relationships
- Calculates average ratings across subgroup members
- Provides visual analysis through radar charts and tables

## Tips for Effective Use

1. **Start with a clear segmentation strategy**: Decide your grouping criteria before creating subgroups
2. **Use descriptive names**: Make subgroup names clear and meaningful
3. **Review regularly**: Update subgroup assignments as stakeholder roles evolve
4. **Compare subgroups**: Analyze multiple subgroups to identify patterns and differences
5. **Document decisions**: Use the description field to explain why stakeholders are grouped together

## Support

For questions or issues with the subgroup feature, refer to:
- The main SIAMA documentation
- The original SIAMA 3 Excel file for reference
- SAT Step 1 for stakeholder rating methodology
