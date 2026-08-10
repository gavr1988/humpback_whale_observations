"""Generate the project visualisations as a standalone script.

This script loads the cleaned whale observations dataset, recreates the
exploratory charts from the notebook, and saves each figure into a local
`figures/` directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parent
FIGURE_DIR = PROJECT_ROOT / "figures"
SEASON_ORDER = ["Winter", "Spring", "Summer", "Autumn"]


def load_cleaned_data() -> pd.DataFrame:
    """Load the cleaned whale dataset from the project root."""

    candidate_paths = [
        PROJECT_ROOT / "whale_data_cleaned.csv",
        PROJECT_ROOT / "jupyter_notebooks" / "whale_data_cleaned.csv",
    ]

    for csv_path in candidate_paths:
        if csv_path.exists():
            df = pd.read_csv(csv_path)
            df["eventDate"] = pd.to_datetime(df["eventDate"], errors="coerce", utc=True)

            for column in ["date_year", "month", "decimalLatitude", "decimalLongitude", "sst", "sss", "coordinateUncertaintyInMeters"]:
                if column in df.columns:
                    df[column] = pd.to_numeric(df[column], errors="coerce")

            if "season" not in df.columns:
                df["season"] = df["month"].apply(
                    lambda value: "Winter"
                    if value in [12, 1, 2]
                    else ("Spring" if value in [3, 4, 5] else ("Summer" if value in [6, 7, 8] else "Autumn"))
                )

            return df

    raise FileNotFoundError(
        "Could not find whale_data_cleaned.csv in the project root or jupyter_notebooks/ directory."
    )


def prepare_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, np.ndarray, np.ndarray]:
    """Create the SST, SSS, and combined dataframes used by the plots."""

    df_sst = df.dropna(subset=["sst"]).copy()
    df_sss = df.dropna(subset=["sss"]).copy()
    df_sst_sss = df.dropna(subset=["sst", "sss"]).copy()

    sst_array = df_sst["sst"].to_numpy()
    sss_array = df_sss["sss"].to_numpy()

    return df_sst, df_sss, df_sst_sss, sst_array, sss_array


def save_current_figure(filename: str) -> None:
    """Save the active figure to the figures directory and close it."""

    FIGURE_DIR.mkdir(exist_ok=True)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()


def create_visualisations() -> None:
    """Recreate the notebook charts and save them as PNG files."""

    sns.set_theme(style="whitegrid")

    df = load_cleaned_data()
    df_sst, df_sss, df_sst_sss, sst_array, sss_array = prepare_data(df)

    # SST 1: histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df_sst["sst"], bins=30, edgecolor="black")
    plt.title("Distribution of Sea-Surface Temperature")
    plt.xlabel("Sea-Surface Temperature (°C)")
    plt.ylabel("Number of Observations")
    save_current_figure("01_sst_histogram.png")

    # SST 2: box plot by season
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_sst, x="season", y="sst", order=SEASON_ORDER)
    plt.title("Sea-Surface Temperature by Season")
    plt.xlabel("Season")
    plt.ylabel("Sea-Surface Temperature (°C)")
    save_current_figure("02_sst_boxplot_by_season.png")

    # SST 3: observation count by season
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_sst, x="season", order=SEASON_ORDER)
    plt.title("Number of Whale Observations by Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Observations")
    save_current_figure("03_observations_by_season.png")

    # SST 4: mean and median by season
    season_sst_summary = (
        df_sst.groupby("season")["sst"].agg(["mean", "median"]).reindex(SEASON_ORDER).reset_index()
    )
    season_sst_chart = season_sst_summary.melt(
        id_vars="season",
        value_vars=["mean", "median"],
        var_name="statistic",
        value_name="sst",
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(data=season_sst_chart, x="season", y="sst", hue="statistic", order=SEASON_ORDER)
    plt.title("Mean and Median Sea-Surface Temperature by Season")
    plt.xlabel("Season")
    plt.ylabel("Sea-Surface Temperature (°C)")
    plt.legend(title="Statistic")
    save_current_figure("04_sst_mean_median_by_season.png")

    # SST 5: observations by SST range
    df_sst["sst_range"] = pd.cut(
        df_sst["sst"],
        bins=[-5, 0, 5, 10, 15, 20, 25, 30, 35, 40],
        labels=[
            "-5 to 0°C",
            "0 to 5°C",
            "5 to 10°C",
            "10 to 15°C",
            "15 to 20°C",
            "20 to 25°C",
            "25 to 30°C",
            "30 to 35°C",
            "35 to 40°C",
        ],
        include_lowest=True,
    )
    sst_range_counts = df_sst["sst_range"].value_counts().sort_index().reset_index()
    sst_range_counts.columns = ["sst_range", "observation_count"]
    plt.figure(figsize=(12, 6))
    sns.barplot(data=sst_range_counts, x="sst_range", y="observation_count")
    plt.title("Whale Observations by Sea-Surface Temperature Range")
    plt.xlabel("Sea-Surface Temperature Range")
    plt.ylabel("Number of Observations")
    plt.xticks(rotation=45)
    save_current_figure("05_observations_by_sst_range.png")

    # SST 6: mean SST by year
    yearly_mean_sst = df_sst.groupby("date_year")["sst"].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=yearly_mean_sst, x="date_year", y="sst", marker="o")
    plt.title("Mean Sea-Surface Temperature of Whale Observations by Year")
    plt.xlabel("Year")
    plt.ylabel("Mean Sea-Surface Temperature (°C)")
    plt.xticks(range(2010, 2026), rotation=45)
    save_current_figure("06_mean_sst_by_year.png")

    # SSS 1: histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df_sss["sss"], bins=30, edgecolor="black")
    plt.title("Distribution of Sea-Surface Salinity")
    plt.xlabel("Sea-Surface Salinity (PSU)")
    plt.ylabel("Number of Observations")
    save_current_figure("07_sss_histogram.png")

    # SSS 2: box plot by season
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_sss, x="season", y="sss", order=SEASON_ORDER)
    plt.title("Sea-Surface Salinity by Season")
    plt.xlabel("Season")
    plt.ylabel("Sea-Surface Salinity (PSU)")
    save_current_figure("08_sss_boxplot_by_season.png")

    # SSS 3: mean and median by season
    sss_season_summary = (
        df_sss.groupby("season")["sss"].agg(["mean", "median"]).reindex(SEASON_ORDER).reset_index()
    )
    sss_season_chart = sss_season_summary.melt(
        id_vars="season",
        value_vars=["mean", "median"],
        var_name="statistic",
        value_name="sss",
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(data=sss_season_chart, x="season", y="sss", hue="statistic", order=SEASON_ORDER)
    plt.title("Mean and Median Sea-Surface Salinity by Season")
    plt.xlabel("Season")
    plt.ylabel("Sea-Surface Salinity")
    plt.legend(title="Statistic")
    save_current_figure("09_sss_mean_median_by_season.png")

    # SST and SSS relationship
    sst_sss_correlation = np.corrcoef(df_sst_sss["sst"], df_sst_sss["sss"])[0, 1]
    print(f"Correlation between SST and SSS: {sst_sss_correlation:.3f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(df_sst_sss["sst"], df_sst_sss["sss"], alpha=0.5)
    plt.title("Correlation between SST and SSS")
    plt.xlabel("Sea Surface Temperature (°C)")
    plt.ylabel("Sea Surface Salinity (PSU)")
    save_current_figure("10_sst_sss_scatter.png")


if __name__ == "__main__":
    create_visualisations()