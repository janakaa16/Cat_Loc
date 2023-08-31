import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache
def load_data():
    return pd.read_excel('Jun-AugOffline2023.xlsx')
# Load your DataFrame (assuming it's named 'df')
df = load_data()

# Set Streamlit options
st.set_option('deprecation.showPyplotGlobalUse', False)

# Set background color and title
st.markdown('<style>body{background-color: LightGray;}</style>', unsafe_allow_html=True)
st.title("Penjualan Terbaik per-Kategori")

# Create a dropdown for selecting 'Kategori'
kategori_options = ['All'] + list(df['Kategori'].unique())
selected_kategori = st.selectbox("Choose a Kategori", kategori_options)

# Filter data based on the selected 'Kategori'
if selected_kategori == 'All':
    selected_data = df
else:
    selected_data = df[df['Kategori'] == selected_kategori]

# Create and display the count plot using Seaborn
plt.figure(figsize=(10, 5))
ax = sns.countplot(data=selected_data, x='Outlet', order=selected_data['Outlet'].value_counts().head(10).index)
plt.xticks(size=8)
plt.title(f"Count Plot for Outlet in {selected_kategori if selected_kategori != 'All' else 'All Kategori'}")
plt.tight_layout()

# Annotate the bars with count values
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='gray', xytext=(0, 5),
                textcoords='offset points')

# Display the plot using st.pyplot
st.pyplot()
