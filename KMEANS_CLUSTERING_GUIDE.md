# K-Means Clustering for Stakeholder Subgrouping

## Overview
The SIAMA SAT Step 2 now includes **automatic k-means clustering** functionality that uses machine learning to intelligently group stakeholders based on their Power, Interest, Legitimacy, and Urgency ratings.

## What is K-Means Clustering?

K-means clustering is a machine learning algorithm that automatically groups similar data points together. In the context of stakeholder analysis:

- **Analyzes** stakeholder ratings across multiple dimensions
- **Identifies** natural groupings based on similarity
- **Creates** balanced, meaningful subgroups automatically
- **Eliminates** manual bias in grouping decisions

## How to Use

### Step 1: Navigate to K-Means Clustering
1. Go to **SAT → Step 2: Management Tool**
2. Click on **👥 Subgroup Management** tab
3. Select the **🤖 Automatic Clustering** tab

### Step 2: Configure Clustering Parameters

#### Number of Clusters
- Use the slider to select how many groups you want (2-8 clusters)
- **Recommendation**:
  - 3 clusters: Simple high/medium/low priority grouping
  - 4 clusters: Classic power-interest matrix quadrants
  - 5-6 clusters: More nuanced segmentation

#### Features for Clustering
Select which stakeholder attributes to consider:
- **Power**: Ability to influence outcomes
- **Interest**: Level of concern/stake
- **Legitimacy**: Validity of involvement
- **Urgency**: Immediacy of demands

**Recommended Combinations**:
- Power + Interest (classic approach)
- All four features (comprehensive analysis)
- Power + Legitimacy + Urgency (influence-focused)

### Step 3: Generate Clusters
1. Click the **🤖 Generate Clusters** button
2. The algorithm will:
   - Standardize the data (normalize scales)
   - Apply k-means clustering
   - Assign each stakeholder to a cluster
   - Generate meaningful cluster names
   - Create subgroups automatically

### Step 4: Review Results

The system provides multiple visualizations:

#### 3D Cluster Visualization
- Interactive 3D scatter plot
- Axes: Power, Interest, Legitimacy
- Color-coded by cluster
- Hover to see stakeholder details

#### 2D Projections
- **Power vs Interest**: Classic stakeholder matrix
- **Legitimacy vs Urgency**: Additional perspective
- Quadrant lines for reference

#### Cluster Statistics Table
- Member count per cluster
- Average ratings for each dimension
- Quick comparison across clusters

## Automatic Cluster Naming

The system automatically names clusters based on their characteristics:

### Power-Interest Based Naming

| Avg Power | Avg Interest | Cluster Name | Strategy |
|-----------|--------------|--------------|----------|
| High (>6.5) | High (>6.5) | **Key Players** | Manage Closely |
| High (>6.5) | Lower (≤6.5) | **Keep Satisfied** | Maintain Satisfaction |
| Lower (≤6.5) | High (>6.5) | **Keep Informed** | Regular Updates |
| Lower (≤6.5) | Lower (≤6.5) | **Monitor** | Basic Oversight |

Example: "Key Players (Cluster 1)", "Keep Satisfied (Cluster 2)"

## Use Cases

### 1. Initial Stakeholder Segmentation
**Scenario**: You have 25 stakeholders and need to organize them quickly

**Approach**:
- Use 4 clusters
- Select all four features
- Generate clusters
- Review and adjust if needed

**Benefit**: Quick, unbiased initial grouping

### 2. Training Program Design
**Scenario**: Create targeted training groups based on engagement levels

**Approach**:
- Use 3 clusters
- Focus on Interest + Legitimacy
- High cluster → Advanced training
- Medium cluster → Intermediate training
- Low cluster → Awareness programs

### 3. Resource Allocation Planning
**Scenario**: Prioritize limited resources across stakeholders

**Approach**:
- Use 5 clusters with all features
- Analyze cluster statistics
- Allocate resources proportionally

### 4. Identifying Hidden Patterns
**Scenario**: Discover non-obvious stakeholder groupings

**Approach**:
- Try different cluster numbers (3, 4, 5)
- Compare results
- Look for unexpected groupings
- Use insights to refine strategy

## Technical Details

### Algorithm
- **Method**: K-means clustering with k-means++ initialization
- **Standardization**: StandardScaler (zero mean, unit variance)
- **Random State**: 42 (for reproducibility)
- **Iterations**: Maximum 300 (default)

### Data Processing
1. Extract selected features from stakeholder ratings
2. Standardize features to same scale
3. Apply k-means algorithm
4. Transform cluster centers back to original scale
5. Assign descriptive names based on characteristics

### Distance Metric
- Uses Euclidean distance in standardized space
- Ensures equal weight for all selected features

## Advantages of K-Means Clustering

### vs. Manual Grouping

| Aspect | Manual Grouping | K-Means Clustering |
|--------|----------------|-------------------|
| Speed | Slow for many stakeholders | Instant results |
| Bias | Subject to human bias | Data-driven, objective |
| Consistency | May vary between users | Consistent results |
| Complexity | Hard with 4+ dimensions | Handles multiple features |
| Scalability | Difficult with 20+ stakeholders | Scales easily |

### Benefits
1. **Objectivity**: Based on data, not assumptions
2. **Speed**: Instant grouping of any number of stakeholders
3. **Multi-dimensional**: Considers all four attributes simultaneously
4. **Reproducible**: Same inputs = same outputs
5. **Balanced**: Creates roughly equal-sized groups
6. **Exploratory**: Discover patterns you might miss manually

## Best Practices

### 1. Start with All Features
- Begin with all four features (Power, Interest, Legitimacy, Urgency)
- Provides most comprehensive grouping
- Can refine later if needed

### 2. Try Multiple Cluster Numbers
- Generate 3 clusters, review
- Generate 4 clusters, compare
- Choose the number that makes most sense for your context

### 3. Validate Results
- Check if cluster assignments make intuitive sense
- Review stakeholders within each cluster
- Ensure no obvious misassignments

### 4. Combine with Manual Adjustments
- Use clustering as starting point
- Manually reassign specific stakeholders if needed
- Document reasons for manual changes

### 5. Use Visualizations
- Always review the 3D and 2D plots
- Look for clear separation between clusters
- Check for outliers

## Interpreting Results

### Good Clustering Indicators
- ✅ Clear separation in visualizations
- ✅ Similar stakeholders grouped together
- ✅ Balanced cluster sizes
- ✅ Distinct average characteristics per cluster

### Potential Issues
- ⚠️ Overlapping clusters in visualizations
- ⚠️ Very unbalanced cluster sizes (e.g., 1 vs 20)
- ⚠️ Similar average ratings across all clusters
- ⚠️ Unexpected stakeholder assignments

### Solutions
- Try different number of clusters
- Select different feature combinations
- Use manual grouping for edge cases
- Combine automatic + manual approaches

## Integration with Manual Grouping

K-means clustering **complements** manual grouping:

1. **Start Automatic**: Generate clusters first
2. **Review**: Examine assignments
3. **Refine Manually**: Adjust specific assignments
4. **Add Custom Groups**: Create additional manual groups for special cases
5. **Mix Approaches**: Use clustering for majority, manual for exceptions

## Example Workflow

### Scenario: Craft Education Program with 18 Stakeholders

**Step 1: Generate Initial Clusters**
- Select 4 clusters
- Use all four features
- Generate clusters

**Result**:
- Cluster 1: Key Players (5 stakeholders)
- Cluster 2: Keep Satisfied (4 stakeholders)
- Cluster 3: Keep Informed (6 stakeholders)
- Cluster 4: Monitor (3 stakeholders)

**Step 2: Review Assignments**
- Check 3D visualization
- Verify cluster makes sense
- Identify any questionable assignments

**Step 3: Manual Refinements**
- Move 1 stakeholder from "Monitor" to "Keep Informed"
- Reason: Recent increase in engagement (not reflected in original ratings)

**Step 4: Create Additional Manual Group**
- Create "VIP Partners" group
- Manually select 3 key stakeholders from "Key Players"
- For special intensive collaboration

**Step 5: Develop Strategies**
- Key Players → Weekly meetings, direct involvement
- Keep Satisfied → Monthly updates, consultation
- Keep Informed → Quarterly newsletters
- Monitor → Annual check-ins
- VIP Partners → Co-design training curriculum

## Troubleshooting

**Q: Clustering results don't make sense**
- Try different number of clusters
- Check if data is too uniform (all similar ratings)
- Consider using fewer features

**Q: All stakeholders in one cluster**
- Ratings may be too similar
- Try manual grouping instead
- Or create artificial distinctions based on other criteria

**Q: Too many small clusters**
- Reduce number of clusters
- Combine similar clusters manually

**Q: Stakeholder assigned to wrong cluster**
- Use manual reassignment
- Document the reason
- Consider if ratings need updating

## Advanced Tips

### 1. Optimal Cluster Number
Try the "elbow method":
- Generate 2, 3, 4, 5, 6 clusters
- Review cluster statistics for each
- Look for natural breakpoints

### 2. Feature Selection Strategy
- **Power + Interest**: For prioritization
- **All Four**: For comprehensive analysis
- **Legitimacy + Urgency**: For compliance/risk focus

### 3. Iterative Refinement
- Generate clusters
- Update stakeholder ratings based on new insights
- Re-run clustering
- Compare before/after

### 4. Temporal Analysis
- Cluster stakeholders at different time points
- Track how stakeholders move between clusters
- Identify trends and shifts

## Limitations

K-means clustering has some limitations to be aware of:

1. **Assumes Spherical Clusters**: May not capture complex patterns
2. **Requires Numeric Data**: Can only use the four rating dimensions
3. **Number Must Be Specified**: You need to choose k in advance
4. **Sensitive to Outliers**: Extreme values can affect results
5. **Local Optima**: May not find globally optimal solution

**Mitigation**: Use clustering as a tool, not the final answer. Combine with human judgment.

## Comparison with Excel Approach

| Feature | Excel (Manual) | Streamlit (K-Means) |
|---------|---------------|---------------------|
| Method | Manual column entry (1,2,3...) | Automatic algorithm |
| Basis | User judgment | Data similarity |
| Time | Minutes to hours | Seconds |
| Dimensions | Usually 1-2 | Up to 4 simultaneously |
| Visualization | Limited | 3D + 2D interactive |
| Reproducibility | Varies | Consistent |
| Learning Curve | Low | Medium |

## Conclusion

K-means clustering provides a powerful, data-driven approach to stakeholder subgrouping. It's best used as a starting point that can be refined with manual adjustments based on context-specific knowledge.

**Recommended Workflow**:
1. Use k-means for initial grouping (80% solution)
2. Review and validate assignments (quality check)
3. Make manual refinements (final 20%)
4. Develop targeted strategies per group
5. Re-cluster periodically as situations change

---

**Next Steps**: After clustering, proceed to the Subgroup Analysis section to review aggregated metrics and strategic recommendations for each cluster.
