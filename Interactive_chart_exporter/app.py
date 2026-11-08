import streamlit as st
import pandas as pd
st.set_page_config(page_title="Interactive Chart Exporter", layout="wide")
st.title("📊 Interactive Chart Exporter")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv","txt","data","tsv","dat","table","xls","xlsx","xlsm","xlsb","odf","ods","odt"])
if uploaded_file is not None:
   df = pd.read_csv(uploaded_file , sep=None, engine='python')
   st.success("✅ File uploaded successfully!")
   st.subheader("📋 Data Preview")
   st.dataframe(df.head(10))
   st.subheader("📑 Dataset Report")
   if st.button("Generate Report"):
       report = f"Dataset Report:\n\n"
       report += f"Number of Rows: {df.shape[0]}\n"
       report += f"Number of Columns: {df.shape[1]}\n\n"
       report += f"Column Details:\n{', '.join(df.columns)}\n\n"
       report += f"Data Types:\n{df.dtypes}\n\n"
       report += f"Descriptive Statistics:\n{df.describe()}\n"
       st.text(report)
       st.download_button(
           label="Download Report",
           data=report,
           file_name="dataset_report.txt",
           mime="text/plain"
       )
   st.subheader("📈 Dataset Chart")
   chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"],index=0)
   numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
   selected_columns = st.multiselect("Select Columns for Chart", numeric_columns)
   if chart_type and selected_columns:
       cols = st.columns(3)
       col_index = 0
       if "Histogram" in chart_type:
           with cols[col_index]:
               st.write(f"### Histogram for {', '.join(selected_columns)}")
               st.bar_chart(df[selected_columns])
           col_index += 1
       if "Line Chart" in chart_type:
           with cols[col_index]:
               st.write(f"### 📉  Line Chart for {', '.join(selected_columns)}")
               st.line_chart(df[selected_columns])
           col_index += 1
       if "Bar Chart" in chart_type:
           with cols[col_index]:
               st.write(f"### 📊  Bar Chart for {', '.join(selected_columns)}")
               st.bar_chart(df[selected_columns])
           col_index += 1
       if "Scatter Plot" in chart_type:
           with cols[col_index]:
               st.write(f"### 📈  Scatter Plot for {', '.join(selected_columns)}")
               st.scatter_chart(df[selected_columns])
           col_index += 1

       

else:
    st.info("Please upload a CSV file to visualize and export charts.")





# import streamlit as st
# import pandas as pd

# # -------------------------------------
# # Page Config
# # -------------------------------------
# st.set_page_config(
#     page_title="Interactive Chart Exporter",
#     layout="wide"
# )

# st.title("📊 Interactive Chart Exporter")

# # -------------------------------------
# # File Upload
# # -------------------------------------
# uploaded_file = st.file_uploader(
#     "Upload your CSV file",
#     type=["csv"]
# )

# if uploaded_file is not None:

#     # Read CSV
#     df = pd.read_csv(uploaded_file)

#     st.success("✅ File uploaded successfully!")

#     # -------------------------------------
#     # Data Preview
#     # -------------------------------------
#     st.subheader("📋 Data Preview")
#     st.dataframe(df.head(10), use_container_width=True)

#     # -------------------------------------
#     # Dataset Information
#     # -------------------------------------
#     st.subheader("📑 Dataset Report")

#     if st.button("Generate Report"):

#         report = f"""
# DATASET REPORT

# Number of Rows: {df.shape[0]}
# Number of Columns: {df.shape[1]}

# Columns:
# {', '.join(df.columns)}

# Data Types:
# {df.dtypes}

# Descriptive Statistics:
# {df.describe()}
# """

#         st.text(report)

#         st.download_button(
#             label="⬇ Download Report",
#             data=report,
#             file_name="dataset_report.txt",
#             mime="text/plain"
#         )

#     # -------------------------------------
#     # Charts Section
#     # -------------------------------------
#     st.subheader("📈 Charts")

#     chart_types = st.multiselect(
#         "Select Chart Types",
#         [
#             "Line Chart",
#             "Bar Chart",
#             "Scatter Plot",
#             "Histogram"
#         ],
#         default=["Line Chart"]
#     )

#     numeric_columns = df.select_dtypes(
#         include=["int64", "float64"]
#     ).columns.tolist()

#     if len(numeric_columns) == 0:
#         st.warning("No numeric columns found in dataset.")
#         st.stop()

#     selected_columns = st.multiselect(
#         "Select Numeric Columns",
#         numeric_columns,
#         default=numeric_columns[:1]
#     )

#     if selected_columns:

#         # -----------------------------
#         # Line Chart
#         # -----------------------------
#         if "Line Chart" in chart_types:

#             st.markdown("---")
#             st.subheader("📉 Line Chart")

#             st.line_chart(
#                 df[selected_columns],
#                 use_container_width=True
#             )

#         # -----------------------------
#         # Bar Chart
#         # -----------------------------
#         if "Bar Chart" in chart_types:

#             st.markdown("---")
#             st.subheader("📊 Bar Chart")

#             st.bar_chart(
#                 df[selected_columns],
#                 use_container_width=True
#             )

#         # -----------------------------
#         # Scatter Plot
#         # -----------------------------
#         if "Scatter Plot" in chart_types:

#             st.markdown("---")
#             st.subheader("🔵 Scatter Plot")

#             if len(selected_columns) >= 2:

#                 scatter_df = df[
#                     [selected_columns[0], selected_columns[1]]
#                 ]

#                 st.scatter_chart(
#                     scatter_df,
#                     x=selected_columns[0],
#                     y=selected_columns[1],
#                     use_container_width=True
#                 )

#             else:
#                 st.warning(
#                     "Scatter Plot requires at least 2 columns."
#                 )

#         # -----------------------------
#         # Histogram
#         # -----------------------------
#         if "Histogram" in chart_types:

#             st.markdown("---")
#             st.subheader("📊 Histogram")

#             for col in selected_columns:

#                 st.write(f"Histogram of **{col}**")

#                 histogram_data = (
#                     df[col]
#                     .value_counts()
#                     .sort_index()
#                 )

#                 st.bar_chart(
#                     histogram_data,
#                     use_container_width=True
#                 )

# else:
#     st.info(
#         "Please upload a CSV file to visualize and export charts."
#     )