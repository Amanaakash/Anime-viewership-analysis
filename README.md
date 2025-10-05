# 🎌 Anime Viewership Growth Analysis

A data analysis project exploring the growth of anime viewership globally and in India using Python, Pandas, and Matplotlib.

## 📖 About This Project

After binge-watching **Demon Slayer: Infinity Castle** and **Chainsaw Man: Reze Arc**, I decided to put my newly learned Python skills to use! This project analyzes a dataset of 10,000 anime watchers from Kaggle to understand how the anime community has grown over the years.

## 🎯 Objectives

- Analyze global anime viewership trends over time
- Examine India-specific viewership growth patterns
- Practice data manipulation and visualization using Pandas and Matplotlib
- Document findings for the anime and data science community

## 📊 Dataset

- **Source**: Kaggle
- **Size**: 10,000 anime watchers
- **File**: `anime_watchers_dataset_10000.csv`
- **Key Columns Used**:
  - `Watcher_ID`: Unique identifier for each viewer
  - `Country`: Viewer's country
  - `Start_Year_Watching`: Year the viewer started watching anime

## 🛠️ Tech Stack

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization

## 📁 Project Structure

```
.
├── anime_watchers_dataset_10000.csv    # Dataset
├── anime research.txt                   # Analysis code
├── README.md                            # Project documentation
└── (graphs)                             # Generated visualizations
```

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Install required packages**
   ```bash
   pip install pandas matplotlib
   ```

3. **Run the analysis**
   ```bash
   python "anime research.txt"
   ```
   
   Or run the code sections individually in your preferred IDE/Jupyter Notebook.

## 📈 Analysis Breakdown

### Global Viewership Analysis

```python
# Group by year and count viewers
group = df.groupby("Start_Year_Watching")
yearly_viewers = group["Watcher_ID"].count()
```

**Key Technique**: Using `groupby()` to aggregate data by year and track growth trends.

### India-Specific Analysis

```python
# Multi-level grouping by country and year
countryWise = df.groupby(["Country", "Start_Year_Watching"]).size()
India_viewers = countryWise.xs("India")
```

**Key Technique**: Multi-index grouping with `.xs()` (cross-section) to extract country-specific data.

## 🔍 Key Findings

- Clear upward trend in global anime viewership, especially in recent years
- Anime's transition from niche to mainstream entertainment is evident in the data
- India shows significant growth in anime viewership
- [Add your specific insights here after running the analysis]

## 📚 What I Learned

- Data cleaning and preprocessing with Pandas
- Grouping and aggregating data using `groupby()`
- Working with multi-index DataFrames
- Creating clear, readable visualizations with Matplotlib
- Combining passion (anime) with technical skills (Python)

## 🎨 Visualizations

The project generates two main plots:
1. **Global Anime Viewership Growth Over the Years**
2. **Anime Viewership Growth in India**

Both visualizations show year-over-year trends with clear markers and gridlines for readability.

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:
- Open an issue for discussions
- Submit a pull request with enhancements
- Share your own analysis ideas

## 📝 Future Enhancements

Potential areas to explore:
- Genre preference analysis by country
- Viewing habits and patterns
- Favorite character analysis
- Device usage trends
- Age group correlations

## 📬 Connect

If you're interested in anime, data science, or both - let's connect!

[Your Twitter/X] | [Your LinkedIn] | [Your Portfolio]

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This project was created as part of my Python learning journey. The dataset is used for educational and analytical purposes only.

## 🙏 Acknowledgments

- Kaggle for providing the dataset
- The anime community for the inspiration
- Demon Slayer and Chainsaw Man for the motivation! 🔥
