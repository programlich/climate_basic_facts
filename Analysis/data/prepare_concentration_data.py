import pandas as pd

ghg_observed = pd.read_csv("/home/matthias/Python/Klimadashboard/Analysis/data/raw/table_A3.1_historical_abundances.csv", skiprows=37, skipfooter=1,encoding="unicode_escape", usecols=["YYYY", "CO2", "CH4", "N2O"], engine="python")
ghg_observed.rename(columns={"YYYY":"year","CO2":"gemessen","CH4":"ch4","N2O":"n2o"}, inplace=True)

co2_projections = pd.read_excel("/home/matthias/Python/Klimadashboard/Analysis/data/raw/IPCC_AR6_AnnexIII_Tab2_future_co2_concentration.xlsx")
co2_projections.rename(columns={"co2_ssp119":"ssp119","co2_ssp126":"ssp126","co2_ssp245":"ssp245","co2_ssp370":"ssp370","co2_ssp585":"ssp585"},inplace=True)

co2_concentration_total = pd.merge(left=ghg_observed,right=co2_projections,on="year",how="outer")
co2_concentration_total.loc[co2_concentration_total["year"]==2020,"gemessen"] = 414

co2_concentration_total.to_csv("/home/matthias/Python/Klimadashboard/Analysis/data/co2_concentration_total.csv")
