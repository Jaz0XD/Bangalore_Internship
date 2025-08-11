import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def get_missing_value_graph(df):
    missing_df = pd.DataFrame(df.iloc[:, 1:].isna().sum()).T
    fig, ax = plt.subplots(figsize=(22,5))
    sns.heatmap(missing_df, annot= True,cmap=sns.dark_palette('gray', as_cmap=True),  linecolor = 'silver', linewidth=1, ax=ax)
    return fig

def categorical_graph(df, col_name):
    fig, axes = plt.subplots(1, 2, figsize=(14,6), facecolor = 'silver')
    sns.countplot(data=df, x=col_name,hue='Married', palette='Set2',ax = axes[0])

    gender_count = df[col_name].value_counts()
    axes[1].pie(gender_count.values, labels = gender_count.index, autopct = '%1.2f%%', shadow = True, colors = sns.color_palette('Set2'), startangle=90)

    # Setting title and label For Graph 0
    axes[0].set_title('CountPlot for Marriage')
    axes[0].set_xlabel('Married')
    axes[0].set_ylabel('Count')


    # Setting title and label For Graph 1
    axes[1].set_title('Pie Chart for Gender')

    return fig

def get_histogram(df):
    cont_columns = df.select_dtypes(include=['int64','float64']).columns.tolist()
    fig, axes = plt.subplots(1,3, figsize = (14,4), facecolor = 'silver')
    sns.histplot(data = df,x = cont_columns[0],kde=True, ax = axes[0])
    sns.histplot(data = df,x = cont_columns[1],kde=True, ax = axes[1])
    sns.histplot(data = df,x = cont_columns[2],kde=True, ax = axes[2])
    return fig

def kde_plot(df):
    cont_columns = df.select_dtypes(include=['int64','float64']).columns.tolist()
    fig, axes = plt.subplots(1,3, figsize = (14,4), facecolor = 'silver')
    col_one = cont_columns[0]
    sns.kdeplot(data = df[col_one], fill = True, ax= axes[0])
    col_two = cont_columns[1]
    sns.kdeplot(data = df[col_two], fill = True, ax= axes[1])
    col_three = cont_columns[2]
    sns.kdeplot(data = df[col_three], fill = True, ax= axes[2])
    return fig

def fill_na(df, fill_type):
    for col in df.columns:
        if df[col].isnull().sum().tolist()>0:
            if df[col].dtype == object:
                mode = df[col].mode()[0]
                df[col] = df[col].fillna(mode)
            else:
                if fill_type == 'Mean':
                    mean_value = df[col].mean()
                    df[col] = df[col].fillna(mean_value)
                elif fill_type == 'Median':
                    median_value = df[col].median()
                    df[col] = df[col].fillna(median_value)
                else:
                    mode_value = df[col].mode()
                    df[col] = df[col].fillna(mode_value)
    return df

def get_map(df, col_name):
    mapp = {}
    temp_list = df[col_name].unique().tolist()
    for index, val in enumerate(temp_list):
        mapp[val] = index
    return mapp

def categorical_encoding(df, cat_cols):
    for col in cat_cols:
        temp_map = get_map(df, col)
        df[col] = df[col].map(temp_map)
    return df