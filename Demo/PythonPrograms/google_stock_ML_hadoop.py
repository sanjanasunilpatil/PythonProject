#!/usr/bin/python3
from pyspark import SparkContext
from pyspark.sql import SQLContext
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


class Regression:

    def driver_class(self, train_file_path, test_file_path):
        train_data = self.read_data(train_file_path)
        split_train_data = self.split_data(train_data)
        processed_train_data = self.data_preprocessing(split_train_data[0], split_train_data[1])
        self.store_processed_data(processed_train_data[0], processed_train_data[1])
        test_data = self.read_data(test_file_path)
        split_test_data = self.split_data(test_data)
        y_pred = self.ML_model(processed_train_data[0], processed_train_data[1], split_test_data[0])
        self.accuracy(split_test_data[1], y_pred)

    def read_data(self, file_path):
        sc = SparkContext("local", "ML")
        sql_context = SQLContext(sc)
        data = sql_context.read.load(file_path, format='com.databricks.spark.csv', header='true', inferSchema='true').toPandas()
        sc.stop()
        return data

    def split_data(self, data):
        x = data.iloc[:, 2:3]
        y = data.iloc[:, 1:2]

        return x, y

    def data_preprocessing(self, x, y):
        if y['Open'].isnull().sum() > 0:
            print("Taking care of null values of cnt column")
            y = y.fillna(y.mean())

        if x['High'].isnull().sum() > 0:
            x = x.fillna(x.mean())

        return x, y

    def ML_model(self, x, y, x_test):
        regression = LinearRegression()
        regression.fit(x, y)
        y_pred = regression.predict(x_test)

        return y_pred

    def accuracy(self, y_test, y_pred):
        accuracy = r2_score(y_test, y_pred)
        print("Accuracy of model ", accuracy)

    def store_processed_data(self, x_train, y_train):
        pd_df = pd.concat([x_train, y_train], axis=1)
        sc = SparkContext("local", "ML")
        sql_context = SQLContext(sc)
        spark_df = sql_context.createDataFrame(pd_df)
        spark_df.write.csv('hdfs://localhost:9000/googleStockPrediction/processed_data')
        sc.stop()


r = Regression()
r.driver_class("hdfs://localhost:9000/googleStockPrediction/google_stock_train_data.csv", "hdfs://localhost:9000/googleStockPrediction/google_stock_test_data.csv")