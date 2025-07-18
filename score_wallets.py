import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from datetime import datetime


def preprocess_transactions(df):
    df['actionData.amount'] = pd.to_numeric(df['actionData.amount'], errors='coerce')
    df['actionData.assetPriceUSD'] = pd.to_numeric(df['actionData.assetPriceUSD'], errors='coerce')
    df['usd_value'] = df['actionData.amount'] * df['actionData.assetPriceUSD']

    actions = ['deposit', 'borrow', 'repay', 'redeemunderlying', 'liquidationcall']
    df = df[df['action'].isin(actions)].copy()

    # Group actions
    grouped = df.groupby(['userWallet', 'action'])['usd_value'].agg(['sum', 'count']).unstack(fill_value=0)
    grouped.columns = [f"{col[1]}_{col[0]}" for col in grouped.columns]

    time_stats = df.groupby('userWallet').agg(
        first_seen=('timestamp', 'min'),
        last_seen=('timestamp', 'max'),
        num_actions=('timestamp', 'count')
    )
    # Ensure first_seen and last_seen are datetime
    time_stats['first_seen'] = pd.to_datetime(time_stats['first_seen'])
    time_stats['last_seen'] = pd.to_datetime(time_stats['last_seen'])
    time_stats['active_days'] = (time_stats['last_seen'] - time_stats['first_seen']).dt.days + 1

    features = grouped.merge(time_stats, left_index=True, right_index=True)

    # Derived features
    features['repay_to_borrow_ratio'] = features.get('sum_repay', 0) / (features.get('sum_borrow', 1))
    features['redeem_to_deposit_ratio'] = features.get('sum_redeemunderlying', 0) / (features.get('sum_deposit', 1))
    features['liquidation_rate'] = features.get('count_liquidationcall', 0) / features['num_actions']
    features['net_flow'] = (
        features.get('sum_deposit', 0)
        + features.get('sum_repay', 0)
        - features.get('sum_borrow', 0)
        - features.get('sum_redeemunderlying', 0)
    )

    features.reset_index(inplace=True)
    return features


def score_wallets(features_df):
    selected = [
    'deposit_sum', 'borrow_sum', 'repay_sum', 'redeemunderlying_sum',
    'repay_to_borrow_ratio', 'redeem_to_deposit_ratio',
    'liquidation_rate', 'net_flow', 'num_actions', 'active_days'
    ]


    # Fix missing
    X = features_df[selected].replace([np.inf, -np.inf], np.nan)
    imputer = SimpleImputer(strategy='constant', fill_value=0)
    X_imputed = imputer.fit_transform(X)
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    weights = np.array([0.2, -0.3, 0.4, -0.2, 0.5, 0.3, -0.5, 0.4, 0.1, 0.2])
    raw_scores = X_scaled.dot(weights)
    scaled_scores = 1000 * (raw_scores - raw_scores.min()) / (raw_scores.max() - raw_scores.min())
    features_df['credit_score'] = scaled_scores.astype(int)
    return features_df[['userWallet', 'credit_score']]


def main():
    input_file = 'user-wallet-transactions.json'
    output_file = 'wallet_scores.json'

    with open(input_file, 'r') as f:
        tx_data = json.load(f)
    df = pd.json_normalize(tx_data)
    features = preprocess_transactions(df)
    scores = score_wallets(features)
    scores.to_json(output_file, orient='records', indent=2)
    print(f"Scores written to {output_file}")


if __name__ == '__main__':
    main()
