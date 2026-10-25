def encode_features(df):
    """Encodes categorical features for modeling."""
    df = df.copy()

    # Encode Churn
    churn_encoder = preprocessing.LabelEncoder()
    df['Churn'] = churn_encoder.fit_transform(df['Churn'])

    # Encode binary columns
    binary_columns = [
        'Partner', 'Dependents', 'PaperlessBilling', 'SeniorCitizen'
    ]
    binary_encoder = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']] * len(binary_columns)
    )
    df[binary_columns] = binary_encoder.fit_transform(
        df[binary_columns]
        ).astype(int)

    # One-hot encode Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=['Contract', 'PaymentMethod'],
        drop_first=True,
        dtype=int
    )

    # Encode TenureGroup in alphabetical order
    tenure_encoder = preprocessing.OrdinalEncoder()
    df[['TenureGroup']] = tenure_encoder.fit_transform(
        df[['TenureGroup']]
        ).astype(int)

    return df, churn_encoder, binary_encoder, tenure_encoder
