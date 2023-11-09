def objective(trial):
    # Define search spaces for hyperparameters
    n_estimators = trial.suggest_int('n_estimators', 10, 300)
    max_depth = trial.suggest_int('max_depth', 1, 20)
    min_child_weight = trial.suggest_float('min_child_weight', 0, 1)
    learning_rate = trial.suggest_float('learning_rate', 1e-5, 1, log=True)

    print(f"{n_estimators=} {max_depth=} {min_child_weight=} {learning_rate=}")

    # !! don't actually train, return -1
    return -1    
