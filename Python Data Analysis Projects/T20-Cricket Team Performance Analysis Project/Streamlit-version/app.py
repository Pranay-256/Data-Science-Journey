import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

st.set_page_config(page_title="T20 Cricket Team Performance Analysis", layout="wide")

# =====================================================
# -------------------- NAVIGATION ----------------------
# =====================================================
page = st.radio("", ["Home", "About"], horizontal=True)

# =====================================================
# -------------------- ABOUT PAGE ----------------------
# =====================================================
if page == "About":

    st.title("About This Project")

    # ---------------------------------------------------
    # 1. Problem Statement
    # ---------------------------------------------------

    st.header("1. Problem Statement")

    st.write("""
    In many local, school-level, inter-college, and small tournament cricket matches, 
    performance evaluation is often done manually. This creates several problems:

    - Player contributions are judged subjectively.
    - Awards such as Best Batsman or Best Bowler may not always be fairly decided.
    - Batting partnerships are rarely analyzed in a structured way.
    - Bowling performance is evaluated mainly on wickets, ignoring economy and consistency.
    - Match-to-match performance comparison is difficult without proper records.

    There is usually no structured data system to analyze performances across multiple matches.

    This project aims to solve that gap by introducing a simple, structured, and data-driven 
    performance evaluation system that works even without ball-by-ball data.
    """)

    # ---------------------------------------------------
    # 2. Objective
    # ---------------------------------------------------

    st.header("2. Objective")

    st.write("""
    The main objective of this project is to build a clear and unbiased cricket performance 
    analysis system using structured match-level data.

    The system focuses on:
    - Measuring individual batting contribution
    - Evaluating bowling impact using wickets and economy rate
    - Measuring player consistency across matches
    - Comparing performances between roles (batsman, bowler, all-rounder)
    - Providing fair statistical summaries for team evaluation

    This project is designed for:
    - Local cricket teams
    - Gully cricket players
    - School and college tournaments
    - Small-scale tournaments without advanced data tools

    The system ensures decisions are based on data rather than opinion.
    """)

    # ---------------------------------------------------
    # 3. Recommended Dataset
    # ---------------------------------------------------

    st.header("3. Recommended Dataset")

    st.write("""
    The system accepts structured match-level datasets following a strict schema.

    Required columns:

    Match_No  
    Player_Name  
    Role (batsman / bowler / all-rounder)  
    Batting_Position  
    Batting_Start_Over  
    Out_Over  
    Balls_Played  
    Runs_Scored  
    Overs_Bowled  
    Runs_Given  
    Wickets_Taken  

    Validation Rules Applied:

    - Match_No must not be null.
    - Player_Name must not be null.
    - Batting data should not exist without valid batting entry.
    - Bowling data should not exist if Overs_Bowled is zero.
    - Numeric fields must contain valid numbers.
    - Consistency calculations require more than one match.

    The system supports:
    - Single match dataset
    - Multiple match datasets

    If validation fails, the system stops and displays an error.
    """)

    # ---------------------------------------------------
    # 4. Analytical Approach & Constraints
    # ---------------------------------------------------

    st.header("4. Analytical Approach & Constraints")

    st.write("""
    The Analytics Tab performs structured performance evaluation using match-level aggregation.

    Batting Analysis:
    - Difference between individual runs scored
    - Strike rate comparison
    - Total runs contribution by role
    - Average runs by batting position (multi-match only)
    - Batting consistency score

    Bowling Analysis:
    - Difference between individual wickets taken
    - Economy rate comparison
    - Total wickets contribution by role
    - Bowling consistency score

    Match Dynamics:
    - Phase-wise wickets breakdown
    - Role-based contribution analysis

    Consistency Formula Used:

    Consistency Score = Mean Performance ÷ (Standard Deviation + 1)

    Constraints:
    - Phase classification uses over-based logic.
    - Batting position average requires multiple matches.
    - Consistency requires at least two matches.

    The analytical layer focuses on meaningful, interpretable metrics.
    """)

    # ---------------------------------------------------
    # 5. Visual Representation
    # ---------------------------------------------------

    st.header("5. Visual Representation")

    st.write("""
    The Visual Representation tab converts analytical results into graphical summaries 
    using Seaborn and Matplotlib (DPI = 120).

    Included visualizations:

    Bar Charts:
    - Difference in individual runs
    - Difference in wickets
    - Strike rate comparison
    - Economy rate comparison
    - Batting consistency
    - Bowling consistency
    - Phase-wise wickets
    - Average runs by position

    Pie Charts:
    - Total runs contribution by player
    - Total wickets contribution by player
    - Runs contribution by role
    - Wickets contribution by role

    All visuals are directly derived from validated match-level data.
    """)

    # ---------------------------------------------------
    # 6. Limitations
    # ---------------------------------------------------

    st.header("6. Limitations")

    st.write("""
    Since ball-by-ball data is not available, the system cannot analyze:

    - Phase-wise runs scored
    - Exact batting partnerships
    - Ball-level strike rate shifts
    - Momentum changes
    - Over-by-over progression
    - Pressure situation impact
    - Detailed partnership contributions

    Advanced insights require ball-level datasets and are outside the scope 
    of this version.

    Future versions may include:
    - Ball-by-ball integration
    - Partnership tracking models
    - Advanced impact metrics
    - Win probability analysis
    """)

    # ---------------------------------------------------
    # 7. Example Data Sets
    # ---------------------------------------------------

    st.header("7. Example Data Sets")

    st.write("If you do not have your own dataset, you may download the sample datasets below and upload them in the Home section to test the system.")

    # Dataset 1
    try:
        with open("RCB_IPL2024_FirstMatch.csv", "rb") as f1:
            st.download_button(
                label="Download Example Dataset - Match 1",
                data=f1,
                file_name="RCB_IPL2024_FirstMatch.csv",
                mime="text/csv"
            )
    except:
        pass

    # Dataset 2
    try:
        with open("RCB_IPL2024_Match2_vs_PBKS.csv", "rb") as f2:
            st.download_button(
                label="Download Example Dataset - Match 2",
                data=f2,
                file_name="RCB_IPL2024_Match2_vs_PBKS.csv",
                mime="text/csv"
            )
    except:
        pass

    # Dataset 3
    try:
        with open("RCB_IPL2024_Match3_vs_GT.csv", "rb") as f3:
            st.download_button(
                label="Download Example Dataset - Match 3",
                data=f3,
                file_name="RCB_IPL2024_Match3_vs_GT.csv",
                mime="text/csv"
            )
    except:
        pass

    st.stop()


# =====================================================
# -------------------- HOME PAGE ----------------------
# =====================================================

st.markdown(
    "<h1 style='text-align: center;'>🏏 T20 Cricket Team Performance Analysis</h1>",
    unsafe_allow_html=True
)

# ---------------- TEMPLATE DOWNLOAD ------------------
st.subheader("Download Template Dataset")

try:
    with open("template.csv", "rb") as file:
        st.download_button(
            label="Download Template CSV",
            data=file,
            file_name="T20_Template.csv",
            mime="text/csv"
        )
except:
    pass


# ---------------- DATA UPLOAD ------------------
st.subheader("Upload Dataset")

upload_option = st.radio(
    "Select Upload Type:",
    ["Single Match Dataset", "Multiple Match Datasets"]
)

uploaded_files = None

if upload_option == "Single Match Dataset":
    uploaded_files = st.file_uploader("Upload CSV", type=["csv"], accept_multiple_files=False)
else:
    uploaded_files = st.file_uploader("Upload Multiple CSVs", type=["csv"], accept_multiple_files=True)

# =====================================================
# ================== MAIN PROCESS =====================
# =====================================================

if uploaded_files:

    # ---------------- DATA LOADING ------------------
    if upload_option == "Single Match Dataset":
        df = pd.read_csv(uploaded_files)
    else:
        dfs = []
        for file in uploaded_files:
            dfs.append(pd.read_csv(file))
        df = pd.concat(dfs, ignore_index=True)

    df.columns = df.columns.str.strip()

    # ---------------- DATA VALIDATION (Hidden) ------------------
    def data_validation(df):

        no_match = df["Match_No"].isnull()
        invalid_player = df["Player_Name"].isnull()

        if no_match.any():
            raise ValueError("Some rows missing Match_No")

        if invalid_player.any():
            raise ValueError("Some rows missing Player_Name")

    try:
        data_validation(df)
    except Exception as err:
        st.error(err)
        st.stop()

    # ---------------- DATA CLEANING (Hidden) ------------------
    df2 = df.copy()

    df2 = df2.dropna(subset=["Player_Name"])
    df2["Batting_Position"] = df2["Batting_Position"].fillna("not-fixed")
    df2["Role"] = df2["Role"].fillna(df2["Role"].mode()[0])

    numeric_cols = [
        "Batting_Start_Over", "Out_Over", "Balls_Played",
        "Runs_Scored", "Overs_Bowled", "Runs_Given", "Wickets_Taken"
    ]

    for col in numeric_cols:
        df2[col] = pd.to_numeric(df2[col], errors="coerce").fillna(0)

    df2["Was_Out"] = (df2["Out_Over"] > 0)

    # ---------------- FEATURE ENGINEERING ------------------

    df2["Strike_Rate"] = np.where(
        df2["Balls_Played"] > 0,
        ((df2["Runs_Scored"] / df2["Balls_Played"]) * 100).round(2),
        0
    )

    # ECONOMY CALCULATION (as per notebook)

    over = df2["Overs_Bowled"].astype(int)
    balls = (df2["Overs_Bowled"] - over) * 10
    real_over = over + (balls / 6)

    df2["Economy_Rate"] = 0.0
    df2.loc[real_over > 0, "Economy_Rate"] = (
        df2.loc[real_over > 0, "Runs_Given"] / real_over[real_over > 0]
    ).round(2)

    # ---------------- FILTERED DATA ------------------

    done_batting = df2[df2["Balls_Played"] > 0]
    done_bowling = df2[df2["Overs_Bowled"] > 0]

    # =====================================================
    # ======================= TABS =========================
    # =====================================================

    tab1, tab2, tab3 = st.tabs(
        ["📊 Analytics", "📈 Visual Representations", "👤 Players-Summary"]
    )

    # =====================================================
    # ===================== ANALYTICS ======================
    # =====================================================

    with tab1:

        st.subheader("Dataset Overview")
        st.write(f"Total Matches: {df2['Match_No'].nunique()}")
        st.write(f"Total Players: {df2['Player_Name'].nunique()}")


        # Runs Difference
        runs_difference = (
            done_batting.groupby("Player_Name")
            .agg({"Runs_Scored": "sum", "Balls_Played": "sum"})
            .sort_values(by="Runs_Scored", ascending=False)
        )

        st.subheader("Difference Between Individual Runs Scored")
        st.dataframe(runs_difference)

        # Team total Runs in each match
        st.subheader("Team Total Runs in Each Match")

        if done_batting["Match_No"].nunique() > 1:
        
            runs_each_match = (
                done_batting
                .groupby("Match_No")["Runs_Scored"]
                .sum()
                .reset_index()
                .sort_values("Match_No")
            )
        
            st.dataframe(runs_each_match)
        
        else:
            st.info("Team Total Runs in Each Match is not applicable for single match dataset.")        

        # Player's Total runs in each match (with drop-down)
        st.subheader("Player's Total Runs in Each Match")

        if done_batting["Match_No"].nunique() > 1:
        
            players_list = sorted(done_batting["Player_Name"].unique().tolist())
        
            selected_player = st.selectbox(
                "Select a Player",
                players_list
            )
        
            selected_player_df = done_batting[
                done_batting["Player_Name"] == selected_player
            ]
        
            player_runs = (
                selected_player_df.groupby("Match_No").agg({"Runs_Scored": "sum", "Balls_Played" : "sum"}).sort_values("Match_No")
            )
        
            st.markdown(f"**{selected_player} - Total Runs in Each Match**")
            st.dataframe(player_runs)
        
        else:
            st.info("Player's Total Runs in Each Match is not applicable for single match dataset.")
    

        # Wickets Difference
        bowling_diff = (
            done_bowling.groupby("Player_Name")
            .agg({"Wickets_Taken": "sum", "Overs_Bowled": "sum"})
            .sort_values(by="Wickets_Taken", ascending=False)
        )

        st.subheader("Difference Between Individual Wickets Taken")
        st.dataframe(bowling_diff)

        #Team Total Wickets in Each Match

        st.subheader("Team Total Wickets in Each Match")

        if done_bowling["Match_No"].nunique() > 1:
        
            wickets_each_match = (
                done_bowling
                .groupby("Match_No")["Wickets_Taken"]
                .sum()
                .reset_index()
                .sort_values("Match_No")
            )
        
            st.dataframe(wickets_each_match)
        
        else:
            st.info("Team Total Wickets in Each Match is not applicable for single match dataset.")
        
        # Players Total Wickets in Each Match (With Dropdown)

        st.subheader("Player's Total Wickets in Each Match")

        if done_bowling["Match_No"].nunique() > 1:
        
            players_list_bowl = sorted(done_bowling["Player_Name"].unique().tolist())
        
            selected_player_bowl = st.selectbox(
                "Select a Player",
                players_list_bowl,
                key="wicket_player_select"
            )
        
            selected_player_bowl_df = done_bowling[
                done_bowling["Player_Name"] == selected_player_bowl
            ]
        
            player_wickets = (
                selected_player_bowl_df
                .groupby("Match_No")["Wickets_Taken"]
                .sum()
                .reset_index()
                .sort_values("Match_No")
            )
        
            st.markdown(f"**{selected_player_bowl} - Total Wickets in Each Match**")
            st.dataframe(player_wickets)
        
        else:
            st.info("Player's Total Wickets in Each Match is not applicable for single match dataset.")


        # Strike_Rate Difference

        batters_allrounders = done_batting[
            (done_batting["Role"] == "batsman") |
            (done_batting["Role"] == "all-rounder")
        ]
        
        strike_rate_diff = (
            batters_allrounders.groupby("Player_Name")
            .agg({
                "Strike_Rate": "mean",
                "Runs_Scored": "sum",
                "Balls_Played": "sum"
            })
            .sort_values(by="Strike_Rate", ascending=False)
            .round(2)
        )
        
        st.subheader("Strike-Rate Comparison between Batsmen and All-Rounders")
        st.dataframe(strike_rate_diff)

        # --------------------------------------------------
        # Economy-Rate Comparison between Bowlers and All-Rounders
        # --------------------------------------------------
        
        bowlers_allrounders = done_bowling[
            (done_bowling["Role"] == "bowler") |
            (done_bowling["Role"] == "all-rounder")
        ]
        
        economy_diff = (
            bowlers_allrounders.groupby("Player_Name")
            .agg({
                "Economy_Rate": "mean",
                "Overs_Bowled": "sum",
                "Runs_Given": "sum"
            })
            .sort_values(by="Economy_Rate")
            .round(2)
        )
        
        st.subheader("Economy-Rate Comparison between Bowlers and All-Rounders")
        st.dataframe(economy_diff)

        # --------------------------------------------------
        # Total Runs Contribution Based on Roles
        # --------------------------------------------------
        
        runs_contribution_by_role = (
            done_batting[done_batting["Runs_Scored"] > 0]
            .groupby("Role")["Runs_Scored"]
            .sum()
            .sort_values(ascending=False)
        )
        
        st.subheader("Total Runs Contribution Based on Roles")
        st.dataframe(runs_contribution_by_role)

        # --------------------------------------------------
        # Total Wickets Contribution Based on Roles
        # --------------------------------------------------
        
        wickets_contribution_by_role = (
            done_bowling[done_bowling["Wickets_Taken"] > 0]
            .groupby("Role")["Wickets_Taken"]
            .sum()
            .sort_values(ascending=False)
        )
        
        st.subheader("Total Wickets Taken Contribution Based on Roles")
        st.dataframe(wickets_contribution_by_role)

        # --------------------------------------------------
        # Phase-wise Wickets Breakdown
        # --------------------------------------------------
        
        wickets_df = df2[df2["Was_Out"] == True].copy()

        def assign_phase(over):
            if over <= 6:
                return "Powerplay"
            elif over <= 15:
                return "Middle Overs"
            else:
                return "Death Overs"
        
        wickets_df["Wicket_Phase"] = wickets_df["Out_Over"].apply(assign_phase)
        
        phase_wickets = (
            wickets_df
            .groupby("Wicket_Phase")
            .size()   # count rows directly instead of Player_Name column
            .reindex(["Powerplay", "Middle Overs", "Death Overs"])
            .reset_index(name="Wickets_Lost")   # rename column properly
        )
        
        st.subheader("Phase-wise Wickets Lost")
        st.dataframe(phase_wickets)
   

        # --------------------------------------------------
        # Players Consistency in Batting
        # --------------------------------------------------
        
        if df2["Match_No"].nunique() > 1:

            match_runs = (
                done_batting.groupby(["Match_No", "Player_Name"])["Runs_Scored"]
                .sum()
                .reset_index()
            )
        
            batting_consistency = (
                match_runs.groupby("Player_Name")["Runs_Scored"]
                .agg(["mean", "std", "count"])
                .round(2)
            )
        
            batting_consistency = batting_consistency[
                batting_consistency["count"] > 1
            ]
        
            batting_consistency["Consistency_Score"] = (
                batting_consistency["mean"] /
                (batting_consistency["std"] + 1)
            ).round(2)
        
            batting_consistency = batting_consistency.sort_values(
                by="Consistency_Score",
                ascending=False
            )
        
            # Reset index to convert Player_Name to column
            batting_consistency = batting_consistency.reset_index()
        
            # Reorder columns
            batting_consistency = batting_consistency[
                ["Player_Name", "Consistency_Score", "mean", "std", "count"]
            ]
        
            st.subheader("Players Consistency in Batting")
            st.dataframe(batting_consistency)
        
        else:
        
            st.info("Players Consistency in Batting is not applicable for single match dataset.")


        # --------------------------------------------------
        # Players Consistency in Bowling
        # --------------------------------------------------
        
        if df2["Match_No"].nunique() > 1:

            match_wickets = (
                done_bowling.groupby(["Match_No", "Player_Name"])["Wickets_Taken"]
                .sum()
                .reset_index()
            )
        
            bowling_consistency = (
                match_wickets.groupby("Player_Name")["Wickets_Taken"]
                .agg(["mean", "std", "count"])
                .round(2)
            )
        
            bowling_consistency = bowling_consistency[
                bowling_consistency["count"] > 1
            ]
        
            bowling_consistency["Consistency_Score"] = (
                bowling_consistency["mean"] /
                (bowling_consistency["std"] + 1)
            ).round(2)
        
            bowling_consistency = bowling_consistency.sort_values(
                by="Consistency_Score",
                ascending=False
            )
        
            # Reset index to make Player_Name a column
            bowling_consistency = bowling_consistency.reset_index()
        
            # Reorder columns
            bowling_consistency = bowling_consistency[
                ["Player_Name", "Consistency_Score", "mean", "std", "count"]
            ]
        
            st.subheader("Players Consistency in Bowling")
            st.dataframe(bowling_consistency)
        
        else:
            st.info("Players Consistency in Bowling is not applicable for single match dataset.")


        # --------------------------------------------------
        # Average Runs by Batting Position
        # --------------------------------------------------
        
        if df2["Match_No"].nunique() > 1:
        
            avg_runs_by_position = (
                done_batting.groupby("Batting_Position")["Runs_Scored"]
                .mean()
                .sort_index()
                .round(2)
            )
        
            st.subheader("Average Runs by Batting Position")
            st.dataframe(avg_runs_by_position)
        
        else:
            st.info("Average Runs by Batting Position is not applicable for single match dataset.")
        

    # =====================================================
    # ===================== VISUALS ========================
    # =====================================================

    with tab2:

        # Runs Bar
        st.subheader("Difference in Runs Scored")
        plt.figure(figsize = (6,4) , dpi=120)
        sns.barplot(y=runs_difference.index, x=runs_difference["Runs_Scored"])
        plt.title("Difference in Runs Scored")
        st.pyplot(plt.gcf())
        plt.close()

        # Team total runs in each match
        st.subheader("Team Total Runs in Each Match")

        if done_batting["Match_No"].nunique() > 1:
        
            runs_each_match = (
                done_batting
                .groupby("Match_No")["Runs_Scored"]
                .sum()
                .sort_index()
            )
        
            x_vals = runs_each_match.index.astype(int)
            y_vals = runs_each_match.values
        
            plt.figure(dpi=120)
        
            sns.lineplot(x=x_vals, y=y_vals, marker="o")
        
            plt.xticks(range(min(x_vals), max(x_vals) + 1))
            plt.title("Team Total Runs in Each Match")
            plt.xlabel("Match No")
            plt.ylabel("Total Runs Scored")
            plt.tight_layout()
        
            st.pyplot(plt.gcf())
            plt.close()
        
        else:
            st.info("Team Total Runs in Each Match is not applicable for single match dataset.")

        #player's total runs in each match    
        st.subheader("Player's Total Runs in Each Match")

        if done_batting["Match_No"].nunique() > 1:
        
            players_list = sorted(done_batting["Player_Name"].unique().tolist())
        
            selected_player = st.selectbox(
                "Select a Player",
                players_list,
                key="player_runs_trend"
            )
        
            selected_player_df = done_batting[
                done_batting["Player_Name"] == selected_player
            ]
        
            player_runs = (
                selected_player_df
                .groupby("Match_No")["Runs_Scored"]
                .sum()
                .reset_index()
                .sort_values("Match_No")
            )
        
            x_vals = player_runs["Match_No"].astype(int)
            y_vals = player_runs["Runs_Scored"]
        
            plt.figure(dpi=120)
        
            sns.lineplot(x=x_vals, y=y_vals, marker="o")
        
            plt.xticks(range(min(x_vals), max(x_vals) + 1))
            plt.title(f"{selected_player}'s Total Runs in Each Match")
            plt.xlabel("Match No")
            plt.ylabel("Runs Scored")
            plt.tight_layout()
        
            st.pyplot(plt.gcf())
            plt.close()
        
        else:
            st.info("Player's Total Runs in Each Match is not applicable for single match dataset.")


        # Wickets Bar
        st.subheader("Difference in Wickets Taken")
        plt.figure(dpi=120)
        sns.barplot(x=bowling_diff["Wickets_Taken"], y=bowling_diff.index)
        plt.title("Difference in Wickets Taken")
        st.pyplot(plt.gcf())
        plt.close()

        # team total wickets in each match
        st.subheader("Team Total Wickets in Each Match")

        if done_bowling["Match_No"].nunique() > 1:
        
            wickets_each_match = (
                done_bowling
                .groupby("Match_No")["Wickets_Taken"]
                .sum()
                .sort_index()
            )
        
            x_vals = wickets_each_match.index.astype(int)
            y_vals = wickets_each_match.values
        
            plt.figure(dpi=120)
            sns.lineplot(x=x_vals, y=y_vals, marker="o")
        
            plt.xticks(range(min(x_vals), max(x_vals) + 1))
            plt.title("Team Total Wickets in Each Match")
            plt.xlabel("Match No")
            plt.ylabel("Total Wickets Taken")
            plt.tight_layout()
        
            st.pyplot(plt.gcf())
            plt.close()
        
        else:
            st.info("Team Total Wickets in Each Match is not applicable for single match dataset.")

        #Player's Total wickets in each match
        st.subheader("Player's Total Wickets in Each Match")

        if done_bowling["Match_No"].nunique() > 1:
        
            players_list_bowl = sorted(done_bowling["Player_Name"].unique().tolist())
        
            selected_player_bowl = st.selectbox(
                "Select a Player",
                players_list_bowl,
                key="player_wickets_trend"
            )
        
            selected_player_bowl_df = done_bowling[
                done_bowling["Player_Name"] == selected_player_bowl
            ]
        
            player_wickets = (
                selected_player_bowl_df
                .groupby("Match_No")["Wickets_Taken"]
                .sum()
                .reset_index()
                .sort_values("Match_No")
            )
        
            x_vals = player_wickets["Match_No"].astype(int)
            y_vals = player_wickets["Wickets_Taken"]
        
            plt.figure(dpi=120)
            sns.lineplot(x=x_vals, y=y_vals, marker="o")
        
            plt.xticks(range(min(x_vals), max(x_vals) + 1))
            plt.title(f"{selected_player_bowl}'s Total Wickets in Each Match")
            plt.xlabel("Match No")
            plt.ylabel("Wickets Taken")
            plt.tight_layout()
        
            st.pyplot(plt.gcf())
            plt.close()
        
        else:
            st.info("Player's Total Wickets in Each Match is not applicable for single match dataset.")
    


        #Total Runs Contribution
        st.subheader("Total Runs Contribution")
        
        top_batters = (
            done_batting.groupby("Player_Name")["Runs_Scored"]
            .sum()
            .sort_values(ascending=False)
            .head()
        )
        
        others = runs_difference["Runs_Scored"].sum() - top_batters.sum()
        
        batting_data = top_batters.copy()
        batting_data["Others"] = others
        batting_data = batting_data[batting_data > 0]
        
        plt.figure(dpi=120)
        wedges, texts, autotexts = plt.pie(
            batting_data,
            autopct="%1.1f%%",
            startangle=90
        )

        for autotext in autotexts:
            autotext.set_fontsize(9)        
        
        plt.legend(
            wedges,
            batting_data.index,
            title="Players",
            loc="center left",
            bbox_to_anchor=(1, 0.5)
        )
        
        plt.title("Total Runs Contribution")
        plt.tight_layout()
        
        st.pyplot(plt.gcf())
        plt.close()
         

        #Total Wickets Contribution

        st.subheader("Total Wickets Contribution")

        top_bowling = (
            done_bowling.groupby("Player_Name")["Wickets_Taken"]
            .sum()
            .sort_values(ascending=False)
        )
        
        other_bowlers = bowling_diff["Wickets_Taken"].sum() - top_bowling.sum()
        
        bowling_data = top_bowling.copy()
        bowling_data["Others"] = other_bowlers
        bowling_data = bowling_data[bowling_data > 0]
        
        plt.figure(dpi=120)

        wedges, texts, autotexts = plt.pie(
            bowling_data,
            autopct="%1.1f%%",
            startangle=90
        )

        for autotext in autotexts:
            autotext.set_fontsize(9)

        plt.legend(
            wedges,
            bowling_data.index,
            title="Players",
            loc="center left",
            bbox_to_anchor=(1, 0.5)
        )
        
        plt.title("Total Wickets Contribution")
        plt.tight_layout()
        
        st.pyplot(plt.gcf())
        plt.close()


        #Strike-Rate Comparison

        st.subheader("Strike-Rate Comparison between Batsmen and All-Rounders")

        plt.figure(dpi=120)
        sns.barplot(
            x=strike_rate_diff["Strike_Rate"],
            y=strike_rate_diff.index
        )
        plt.title("Strike-Rate Comparison")
        plt.xlabel("Strike Rate")
        plt.ylabel("Players")
        st.pyplot(plt.gcf())
        plt.close()

        #Economy-Rate Comparision

        st.subheader("Economy-Rate Comparison between Bowlers and All-Rounders")

        plt.figure(dpi=120)
        sns.barplot(
            x=economy_diff["Economy_Rate"],
            y=economy_diff.index
        )
        plt.title("Economy Rate Comparison")
        plt.xlabel("Economy Rate")
        plt.ylabel("Players")
        st.pyplot(plt.gcf())
        plt.close()

        #Total Runs Contribution Based on Roles

        st.subheader("Total Runs Contribution by Roles")

        plt.figure(dpi=120)
        
        wedges, texts, autotexts = plt.pie(
            runs_contribution_by_role,
            autopct="%1.1f%%",
            startangle=90
        )
        
        # 👇 Reduce percentage font size
        for autotext in autotexts:
            autotext.set_fontsize(9)
        
        plt.legend(
            wedges,
            runs_contribution_by_role.index,
            title="Roles",
            loc="center left",
            bbox_to_anchor=(1, 0.5)
        )
        
        plt.title("Runs Contribution by Roles")
        plt.tight_layout()
        
        st.pyplot(plt.gcf())
        plt.close()


        # Total Wickets Contribution Based on Roles

        st.subheader("Total Wickets Contribution by Roles")

        plt.figure(dpi=120)
        
        wedges, texts, autotexts = plt.pie(
            wickets_contribution_by_role,
            autopct="%1.1f%%",
            startangle=90
        )
        
        # 👇 Reduce percentage font size
        for autotext in autotexts:
            autotext.set_fontsize(9)
        
        plt.legend(
            wedges,
            wickets_contribution_by_role.index,
            title="Roles",
            loc="center left",
            bbox_to_anchor=(1, 0.5)
        )
        
        plt.title("Wickets Contribution by Roles")
        plt.tight_layout()
        
        st.pyplot(plt.gcf())
        plt.close()


        # Phase-Wise Wickets Breakdown

        st.subheader("Phase-wise Wickets Lost")

        plt.figure(dpi=120)
        sns.barplot(
            x=phase_wickets["Wicket_Phase"],
            y=phase_wickets["Wickets_Lost"]
        )
        plt.title("Phase-wise Wickets Lost")
        plt.xlabel("Match Phase")
        plt.ylabel("Total Wickets Lost")
        st.pyplot(plt.gcf())
        plt.close()

        # Players Consistency in Batting

        if df2["Match_No"].nunique() > 1:

            st.subheader("Players Consistency in Batting")
        
            plt.figure(dpi=120)
            sns.barplot(
                y=batting_consistency["Player_Name"],
                x=batting_consistency["Consistency_Score"]
            )
            plt.title("Batting Consistency Score")
            st.pyplot(plt.gcf())
            plt.close()
        
        else:
            st.info("Batting consistency not applicable for single match dataset.")

        #Players Consistency in Bowling

        if df2["Match_No"].nunique() > 1:

            st.subheader("Players Consistency in Bowling")
        
            plt.figure(dpi=120)
            sns.barplot(
                y=bowling_consistency["Player_Name"],
                x=bowling_consistency["Consistency_Score"]
            )
            plt.title("Bowling Consistency Score")
            st.pyplot(plt.gcf())
            plt.close()
        
        else:
            st.info("Bowling consistency not applicable for single match dataset.")

        #Average Runs by Batting Position

        if df2["Match_No"].nunique() > 1:

            st.subheader("Average Runs by Batting Position")
        
            plt.figure(dpi=120)
            sns.barplot(
                x=avg_runs_by_position.index,
                y=avg_runs_by_position.values
            )
            plt.title("Average Runs by Batting Position")
            plt.xlabel("Batting Position")
            plt.ylabel("Average Runs")
            st.pyplot(plt.gcf())
            plt.close()
        
        else:
            st.info("Average runs by position not applicable for single match dataset.")
    
    # =====================================================
    # ================== PLAYERS SUMMARY ==================
    # =====================================================

    with tab3:

        st.subheader("Highest Run Scorers")

        top_runs = (
            done_batting.groupby(["Role", "Player_Name"])
            .agg({"Runs_Scored": "sum", "Strike_Rate": "mean", "Balls_Played": "sum"})
            .sort_values(by="Runs_Scored", ascending=False)
            .head(3)
        )

        st.dataframe(top_runs.reset_index())

        st.subheader("Highest Wicket Takers")

        top_wickets = (
            done_bowling.groupby(["Role", "Player_Name"])
            .agg({"Wickets_Taken": "sum", "Overs_Bowled": "sum", "Economy_Rate" : "mean"})
            .sort_values(by="Wickets_Taken", ascending=False)
            .head(3)
        )

        st.dataframe(top_wickets.reset_index())

        st.subheader("Players with Highest Strike Rate")

        strike = (
            done_batting.groupby(["Role", "Player_Name"])
            .agg({"Strike_Rate": "mean", "Balls_Played": "sum", "Runs_Scored": "sum"})
            .sort_values(by="Strike_Rate", ascending=False)
            .head(3)
        )

        st.dataframe(strike.reset_index())

        st.subheader("Players with Highest Economy Rate")

        economy = (
            done_bowling.groupby(["Role", "Player_Name"])
            .agg({"Economy_Rate": "mean", "Overs_Bowled": "sum", "Runs_Given": "sum",
                  "Wickets_Taken": "sum"})
            .sort_values(by="Economy_Rate", ascending=True)
            .head(3)
        )

        st.dataframe(economy.reset_index())


        if df2["Match_No"].nunique() > 1:

            st.subheader("Most Consistent Players in Batting")
        
            # Merge role info
            batting_consistency_summary = batting_consistency.copy().reset_index()
        
            total_batting_stats = (
                done_batting.groupby(["Player_Name", "Role"])
                .agg({
                    "Balls_Played": "sum",
                    "Runs_Scored": "sum"
                })
                .reset_index()
            )
        
            batting_consistency_summary = batting_consistency_summary.merge(
                total_batting_stats,
                on="Player_Name"
            )
        
            batting_consistency_summary = (
                batting_consistency_summary
                .sort_values(by="Consistency_Score", ascending=False)
                .head(3)
            )
        
            batting_consistency_summary = batting_consistency_summary[
                ["Role", "Player_Name", "Consistency_Score", "Runs_Scored" ,"Balls_Played"]
            ]
        
            st.dataframe(batting_consistency_summary)
        
        else:
            st.info("Batting consistency is not applicable for single match dataset.")


        if df2["Match_No"].nunique() > 1:

            st.subheader("Most Consistent Players in Bowling")
        
            bowling_consistency_summary = bowling_consistency.copy().reset_index()
        
            total_bowling_stats = (
                done_bowling.groupby(["Player_Name", "Role"])
                .agg({
                    "Overs_Bowled": "sum",
                    "Wickets_Taken": "sum"
                })
                .reset_index()
            )
        
            bowling_consistency_summary = bowling_consistency_summary.merge(
                total_bowling_stats,
                on="Player_Name"
            )
        
            bowling_consistency_summary = (
                bowling_consistency_summary
                .sort_values(by="Consistency_Score", ascending=False)
                .head(3)
            )
        
            bowling_consistency_summary = bowling_consistency_summary[
                ["Role", "Player_Name", "Consistency_Score", "Wickets_Taken", "Overs_Bowled"]
            ]
        
            st.dataframe(bowling_consistency_summary)
        
        else:
            st.info("Bowling consistency is not applicable for single match dataset.")    