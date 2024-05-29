# MODEL AGNOSTIC SAFE AI

This package is based on [safeaipackage](https://pypi.org/project/safeaipackage/). The main difference between these two packages is the input required by the functions. In safeaipackage there are different function which ask for train\test data and a machine learning model. Then, all the process of the training and evaluation is done inside the function. However, in modelagnosticsafeaipackage, it is only needed to provide the actual values (y) and the predicted values by any model you are interested in. Hence, while safeaipackage only works with scikit-learn models, here you can use any kind of model to find the estimated values and then use this package to evaluate risks of your model.


# Install

Simply use:

pip install modelagnosticsafeaipackage


# Citations

The proposed measures in this package came primarily out of research by 
[Paolo Giudici](https://www.linkedin.com/in/paolo-giudici-60028a/), [Emanuela Raffinetti](https://www.linkedin.com/in/emanuela-raffinetti-a3980215/), 
and [Golnoosh Babaei](https://www.linkedin.com/in/golnoosh-babaei-990077187/) in the [Statistical laboratory](https://sites.google.com/unipv.it/statslab-pavia/home?authuser=0) 
at the University of Pavia. 
This package is based on the following papers. If you use safeaipackage in your research we would appreciate a citation to our papers:
* [Giudici, P., & Raffinetti, E. (2024). RGA: a unified measure of predictive accuracy. Advances in Data Analysis and Classification, 1-27.](https://link.springer.com/article/10.1007/s11634-023-00574-2)
* [Raffinetti, E. (2023). A rank graduation accuracy measure to mitigate artificial intelligence risks. Quality & Quantity, 57(Suppl 2), 131-150.](https://link.springer.com/article/10.1007/s11135-023-01613-y)
