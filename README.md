# blockchain_wallet_credit_scoring_system

A rule-based credit scoring system for blockchain wallets, using historical transaction behavior on DeFi protocols.
By analyzing wallet actions like deposits, borrowings, repayments, and liquidations, it assigns a credit score (0–1000) to each wallet.

## 📂 Project Structure

├── user-wallet-transactions.json    # Input: Raw transaction data  
├── wallet_scores.json               # Output: Scored wallets  
├── score_wallets.py                 # Main scoring script  
└── README.md                        # This file  

---

## ⚙️ How It Works

# 1. **Data Ingestion**
    Loads wallet transaction history from a JSON file.

# 2. **Preprocessing**
    - Cleans and parses fields (amounts, timestamps, asset prices).
    - Filters for key actions: `deposit`, `borrow`, `repay`, `redeemunderlying`, `liquidationcall`.

# 3. **Feature Engineering**
    For each wallet:
    - Total & average USD values by action
    - Active days, number of actions
    - Derived behavioral ratios (e.g. repay/borrow ratio, liquidation rate)

# 4. **Credit Scoring**
    - Normalizes features using `MinMaxScaler`
    - Applies heuristic weights to reward good behavior and penalize risk
    - Outputs a credit score between 0 and 1000

---

## 🧪 Example Output

 ```json
 [
   {
     "userWallet": "0xabc123...",
     "credit_score": 785
   },
   ...
 ]
 ```

---

## 🚀 Run the Project

# 1. Install dependencies:
 pip install pandas numpy scikit-learn

# 2. Run the script:
 python score_wallets.py

# Ensure your user-wallet-transactions.json is in the project folder.
