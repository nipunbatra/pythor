class PYLM(object):
    from rpy2.robjects import pandas2ri
    pandas2ri.activate()
    from rpy2.robjects.packages import importr
    stats = importr('stats')
    def convert_fit_to_python(self, fit):
        coeffs_r = fit.rx2('coefficients')
        coeffs= pandas2ri.ri2py(coeffs_r)
        coeff_names =  pandas2ri.ri2py(coeffs_r.names).tolist()
        coeff_series = pd.Series({k:v for k,v in zip(coeff_names, coeffs)})
        fitted_values = pandas2ri.ri2py(fit.rx2('fitted.values'))
        return coeff_series
        
    def fit(self, relationship, df):
        """
        relationship: string of the form: a~b+c
        df: Pandas Dataframe
        """
        # Get R dataframe
        r_df = pandas2ri.py2ri(df)
        # Create linear fit
        fit = stats.lm(relationship, data=df)
        self.fit = fit
        python_fit = self.convert_fit_to_python(fit)
        return python_fit
    
    def predict(self, df):
        pred_r = stats.predict(self.fit, newdata=df)
        pred_python = pandas2ri.ri2py(pred_r)
        return pred_python
