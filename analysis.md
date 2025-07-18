# 1. Distribution of Credit Scores
<img width="307" height="252" alt="image" src="https://github.com/user-attachments/assets/843d60d6-24c7-401f-8544-63cb6a3d3f29" />
<img width="1014" height="545" alt="image" src="https://github.com/user-attachments/assets/a76c8ca0-c0d8-4e18-8214-84db1aca7f2c" />

# 2. Wallets per Credit Score Range
<img width="313" height="250" alt="image" src="https://github.com/user-attachments/assets/ccf2151a-e62e-40f0-b35d-0c1f01085b50" />
<img width="1014" height="599" alt="image" src="https://github.com/user-attachments/assets/dd057275-f2cb-4bc8-9937-c7b481fb01ee" />

# 3. Average Deposit Value for Low Scoring Wallets
Average Deposit Value for Low Scoring Wallets: 4.2358162032222905e+22

# 4. Average Deposit Value for High Scoring Wallets
Average Deposit Value for High Scoring Wallets: 4.7750970585680114e+23

# 5. Average Number of Actions for Low Scoring Wallets
Average Number of Actions for Low Scoring Wallets: 9.883583130010457

# 6. Average Number of Actions for High Scoring Wallets
Average Number of Actions for High Scoring Wallets: 114.0828025477707

# 7. Summary of Low vs High Score Wallets
<img width="592" height="235" alt="image" src="https://github.com/user-attachments/assets/55c62c89-2055-42dd-a39c-61628131b9e9" />

# Observations

1. Most wallets have low credit scores (<300) indicating limited positive DeFi activity or riskier behaviors  
**Data Evidence:**  
Out of 3,497 wallets, 2,208 wallets (about 63%) have scores between 200 and 300.
Only 1 wallet has a score below 100, and 0 wallets between 100–200.  
**Visualization:**  
The histogram and bar chart of credit scores show a large spike in the lowest score bucket ([200, 300)), confirming most users have low scores.
2. High scoring wallets (>700) tend to have much larger deposit, repayment, and net flow values and significantly more actions and active days  
**Data Evidence:**  
There are 162 wallets with scores above 700.
On average, these wallets have:
Deposit Sum: ~9.2e+23 (vs. ~2.9e+22 for low scorers)
Repay Sum: ~3.6e+23 (vs. ~4.9e+21 for low scorers)
Num Actions: ~228 (vs. ~4.5 for low scorers)
Active Days: ~116 (vs. ~2.4 for low scorers)  
**Visualization:**  
The summary table comparing low and high score wallets shows these differences clearly.
3. Low scoring wallets typically show minimal deposit and repayment activity and often only a single transaction  
**Data Evidence:**  
Low score wallets (<300) have:
Deposit Sum: ~2.9e+22
Repay Sum: ~4.9e+21
Num Actions: ~4.5
Active Days: ~2.4 Many have only 1 action and 1 active day.
4. Liquidation rates are generally low across all score buckets suggesting most users avoid risky positions  
**Data Evidence:**  
The average liquidation_rate is 0.0 for both low and high score wallets. The liquidationcall_count is very low (0.015 for low, 0.2 for high scores).
5. High scoring wallets are more engaged with higher counts of deposits, repayments, and protocol interactions  
**Data Evidence:**  
High score wallets have:
Deposit Count: ~62
Repay Count: ~21
Num Actions: ~228
Active Days: ~116 Compared to low score wallets with much lower counts.
6. The credit score distribution is heavily skewed with only a small fraction of wallets achieving top scores  
**Data Evidence:**  
Only 6 wallets have scores above 900. The majority are clustered in the lowest bucket ([200, 300)), as shown in the bar chart.
7. Behavioral ratios (repay to borrow, redeem to deposit) are close to zero for most wallets indicating either no borrowing or repaying or redeeming or depositing activity  
**Data Evidence:**  
Both repay_to_borrow_ratio and redeem_to_deposit_ratio are 0.0 for most wallets, as shown in the summary statistics.
8. Net flow is zero for the majority but high scoring wallets show larger positive or negative net flows reflecting more complex financial behavior  
**Data Evidence:**  
The average net_flow is 0.0 for both low and high score wallets, but high scoring wallets have much larger transaction sums, indicating more complex activity.
9. There is a clear trend: more active, engaged, and responsible users (higher deposits, repayments, actions, and days) receive higher scores  
**Data Evidence:**  
The summary table shows that all engagement metrics (deposits, repayments, actions, days) are much higher for high score wallets.
10. The scoring system effectively distinguishes between passive one-off users and active responsible participants in the protocol
**Data Evidence:**  
The distribution of scores, counts of actions, and engagement metrics all show that passive users get low scores, while active, responsible users get high scores.
