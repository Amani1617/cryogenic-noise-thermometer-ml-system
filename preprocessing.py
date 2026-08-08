class Preprocessor:
    def clean_data(self, df):
        # Remove duplicates
        df = df.drop_duplicates()

        # Fill missing values (forward fill)
        df = df.ffill()

        return df

    def create_features(self, df):
        # Temperature variation
        df["temperature_change"] = df["temperature_k"].diff()

        # Pressure variation
        df["pressure_change"] = df["still_pressure"].diff()

        # Cooling efficiency
        df["cooling_difference"] = (
            df["water_cooling_outlet"] - df["water_cooling_inlet"]
        )

        return df

    def normalize(self, df):
        numeric_columns = df.select_dtypes(include="number").columns
        for column in numeric_columns:
            minimum = df[column].min()
            maximum = df[column].max()
            if maximum != minimum:
                df[column] = (df[column] - minimum) / (maximum - minimum)
        return df
