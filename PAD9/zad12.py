import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.formula.api as statsmodels
import plotly.express as plot

if __name__ == '__main__':
    dataframe = pd.read_csv('PAD_09_PD.csv', sep=";")

    # zad1
    male = dataframe.loc[dataframe['Gender'] == 'Male']['Annual Income (k$)']
    # print(male)
    female = dataframe.loc[dataframe['Gender'] == 'Female']['Annual Income (k$)']
    # print(female)

    print("Male var: ", np.var(male), "Female var: ", np.var(female))

    # przeprowadzamy T-test
    print(stats.ttest_ind(a=male, b=female))
    # pvalue jest większy od przyjętego poziomu istotności (0.05) więc nie można odrzucić hipotezy zerowej

    # zad2
    dataframe.rename(columns={'Spending Score (1-100)': 'SpendingScore',
                              'Annual Income (k$)': 'AnnualIncome'},
                     inplace=True)
    model = statsmodels.ols(formula="SpendingScore ~ Gender + Age + AnnualIncome",
                            data=dataframe).fit()
    print(model.pvalues.values)
    print(model.bse.values)
    print(model.params)

    plot.scatter(dataframe, "Age", "AnnualIncome", "Gender").show()
    plot.scatter(dataframe, "AnnualIncome", "SpendingScore", "Gender").show()
    plot.scatter(dataframe, "SpendingScore", "AnnualIncome", "Age").show()

    # najmniejszy wpływ ma Gender?
    model = statsmodels.ols(formula="SpendingScore ~ Age + AnnualIncome", data= dataframe).fit()
    print(model.summary())

