import streamlit as st
import pandas as pd
from itertools import product
import base64

# Function to generate combinations
def generate_combinations(lists, use_separator, separator):
    combinations = list(product(*lists))
    if use_separator:
        combinations = [' '.join(map(str, item)) for item in combinations]
        combinations = [item.replace(" ", separator) for item in combinations]
    else:
        combinations = [', '.join(map(str, item)) for item in combinations]
    return combinations

# Main function
def main():
    st.title("👹The Permutator👹")

    # Number of lists input
    num_lists = st.number_input("Select the number of lists, comma seperated please :)", min_value=1, value=3)

    # Input boxes for each list
    #create lists of list ':)
    lists = []
    #for each of the lists
    for i in range(num_lists):
        #make a textbox
        list_name = st.text_input(f"List {chr(65 + i)}", "")
        if list_name:
            #for the list strip out the items from the list using , as as seperator
            lists.append([item.strip() for item in list_name.split(',')])
    
    # Checkbox for separator
    use_separator = st.checkbox("Use Separator")
    if use_separator:
        separator = st.text_input("Enter the separator (e.g., '_')", "_")
    else:
        separator = ""

    # Generate button
    if st.button("Generate"):
        #if we dont have lists tell the user
        if not lists:
            st.warning("Please enter at least one list.")
        else:
            # Generate combinations
            combinations = generate_combinations(lists, use_separator, separator)

            # Display as DataFrame
            #df = pd.DataFrame(combinations, columns=[f"Item_{chr(65 + i)}" for i in range(num_lists)])
            df = pd.DataFrame(combinations, columns=["Combinations"])
            st.dataframe(df)

            # Download as CSV
            st.markdown(get_table_download_link(df), unsafe_allow_html=True)


# Function to create a download link for a DataFrame as a CSV file
def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="combinations.csv">Download CSV</a>'
    return href

#the thing that does the thing
if __name__ == "__main__":
    main()