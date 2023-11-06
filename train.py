import joblib
import xgboost as xgb
from sklearn.metrics import recall_score
from ucimlrepo import fetch_ucirepo

RANDOM_STATE = 42

best_params = {
    "max_depth": 15,
    "min_child_weight": 1,
    "subsample": 0.6991661528829747,
    "colsample_bytree": 0.7118881591953465,
    "gamma": 0.4038353275689222,
    "learning_rate": 0.9532067269474095,
    "n_estimators": 121,
}


def get_dataset():
    """Fetch the dataset from the UCI repo"""
    # fetch dataset
    cdc_diabetes_health_indicators = fetch_ucirepo(id=891)

    # data (as pandas dataframes)
    df = cdc_diabetes_health_indicators.data.features
    target = cdc_diabetes_health_indicators.data.targets.Diabetes_binary
    return df, target


def save_model(model):
    """Pickle the model to model.bin file"""
    with open("model.bin", "wb") as f_out:
        joblib.dump((model), f_out)


def train_best_model():
    """Train model with the best found hyperparameters on all the available data"""
    df, target = get_dataset()
    xgb_clf = xgb.XGBClassifier(
        **best_params,
        random_state=RANDOM_STATE,
        n_jobs=-1,
        eval_metric=recall_score,
    )
    xgb_clf.fit(df, target)
    save_model(xgb_clf)


if __name__ == "__main__":
    train_best_model()
