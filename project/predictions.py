import warnings
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def find_best_arima_with_models(y, max_p=3, max_d=2, max_q=3):
    results = []

    for p in range(max_p + 1):
        for d in range(max_d + 1):
            for q in range(max_q + 1):

                try:
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")

                        model = ARIMA(y, order=(p, d, q))
                        fitted_model = model.fit()

                    results.append({
                        "order": (p, d, q),
                        "p": p,
                        "d": d,
                        "q": q,
                        "aic": fitted_model.aic,
                        "bic": fitted_model.bic,
                        "model": fitted_model
                    })

                except Exception:
                    continue

    results = pd.DataFrame(results)

    if results.empty:
        raise ValueError("No ARIMA model could be estimated.")

    best_aic_row = results.loc[results["aic"].idxmin()]
    best_bic_row = results.loc[results["bic"].idxmin()]

    best_aic_model = best_aic_row["model"]
    best_bic_model = best_bic_row["model"]

    return results, best_aic_row, best_bic_row, best_aic_model, best_bic_model


def create_prediction_table(country, fuel_type, y, max_p=3, max_d=2, max_q=3):
    y = pd.Series(y).dropna()

    if len(y) < 15:
        return pd.DataFrame({
    "Last observed price": [None],
    "Best model order by AIC": ["Not enough data"],
    "AIC prediction": [None],
    "AIC % change over last observation": [None],
    "Best model order by BIC": ["Not enough data"],
    "BIC prediction": [None],
    "BIC % change over last observation": [None]
})

    results, best_aic_row, best_bic_row, best_aic_model, best_bic_model = (
        find_best_arima_with_models(
            y,
            max_p=max_p,
            max_d=max_d,
            max_q=max_q
        )
    )

    last_observation = y.iloc[-1]

    aic_prediction = best_aic_model.forecast(steps=1).iloc[0]
    bic_prediction = best_bic_model.forecast(steps=1).iloc[0]

    aic_pct_change = ((aic_prediction / last_observation) - 1) * 100
    bic_pct_change = ((bic_prediction / last_observation) - 1) * 100

    return pd.DataFrame({
    "Last observed price": [round(last_observation, 2)],
    "Best model order by AIC": [best_aic_row["order"]],
    "AIC prediction": [round(aic_prediction, 2)],
    "AIC change in %": [round(aic_pct_change, 2)],
    "Best model order by BIC": [best_bic_row["order"]],
    "BIC prediction": [round(bic_prediction, 2)],
    "BIC change in %": [round(bic_pct_change, 2)]
})