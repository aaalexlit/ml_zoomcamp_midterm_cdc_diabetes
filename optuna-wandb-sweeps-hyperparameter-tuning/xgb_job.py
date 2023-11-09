from typing import Optional

import xgboost as xgb
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
from wandb.xgboost import WandbCallback

import wandb

RANDOM_STATE = 42

PROJECT = "diabetes-prediction"


def get_dataset():
    """Fetch the dataset from the UCI repo"""
    # fetch dataset
    cdc_diabetes_health_indicators = fetch_ucirepo(id=891)

    # data (as pandas dataframes)
    df = cdc_diabetes_health_indicators.data.features
    target = cdc_diabetes_health_indicators.data.targets.Diabetes_binary

    X_train, X_val, y_train, y_val = train_test_split(
        df,
        target,
        test_size=0.2,
        random_state=RANDOM_STATE,
    )
    return X_train, X_val, y_train, y_val


def custom_recall_score(y_true, y_pred):
    return recall_score(y_true, (y_pred >= 0.5).astype(float))


def train(project: Optional[str]):
    """Train model with the best found hyperparameters on all the available data"""
    run = wandb.init(project=project)

    # get config, could be set from sweep scheduler
    train_config = run.config

    # get training parameters from config
    max_depth = train_config.get("max_depth", 15)
    learning_rate = train_config.get("learning_rate", 0.9)
    n_estimators = train_config.get("n_estimators", 120)
    min_child_weight = train_config.get("min_child_weight", 1)

    X_train, X_val, y_train, y_val = get_dataset()

    xgb_clf = xgb.XGBClassifier(
        max_depth=max_depth,
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        min_child_weight=min_child_weight,
        random_state=RANDOM_STATE,
        n_jobs=-1,
        eval_metric=custom_recall_score,
        callbacks=[WandbCallback()],
    )
    
    xgb_clf.fit(
        X_train,
        y_train,
        eval_set=[(X_val, y_val), (X_train, y_train)],
    )


if __name__ == "__main__":
    train(project=PROJECT)
