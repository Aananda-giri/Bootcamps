# Time series

## Deep learning ober traditional machine learning

- Identifying complex patterns, trends, and seasons
- Forcasting for long terms
- Handling missing values

## Algorighms for time series analysis

- RNN
- LSTM
- GatedRecurrent units
- Encoder decoder model

## Structure

1. Load and apply feature engineering on the ddataset
2. build the model
3. train model
4. perform time seriees forcaastingq

## Traffic volume forcasting using LSTM

predict traffic and time required to reach destination

### Dataset Analysis

- metro interstate traffic volume dataset
- hourly recoding of traffic
- coluumns: holydays, temp, rain, snow, clouds, weather, weather descriptioin, date_time, traffic_volume

- Loading the dataset
  - download dataset
  - Extract compressed file

```
df = pd.read_csv('.csv', parse_dates=['date_time'], index_col="date_time")

# check duplicate timestamps
df_traffic = df_traffic[~df_traffic.index.duplicated(keep='last')]
```

### Splitting dataset

```
df_traffic['temp'].describe()

* replace 0 kelvin temp with mean or median value
* convert catergorical variables into dummy/indicator variables.

* drop weather description dolumn
* split data (train, test, val) split based on time peroid
* training dataset: 2 continuous years

* validation dataset: next 6 months of dataset
`df_traffic.loc[datetime.datetime(year=2018, month=1, day=1, hour=0):datetime.datetime(year=2018, month=6, day=300, hour=23)]`

*test dataset: remaining time peroid
`df_traffic.loc[datetime.datetime(year=2018, month=7, day=1, hour=0):]`
```

### Feature engineering

- normalizing interval variables
- we'll use min-max scalar technique for normalization

1. Create scalars: min-max scalers
2. Creating transformers using scalars defined perviously
3. apply scaling

### Creating custom dataset

- Extract features and targets from dataset
- convert dataset into windows with default size of 480 (20 days wowth of data)

### Creating window/sequencing

-fixed window is gives model the span to work with rolling target.

## LSTM with pytorch

### 1. Define the model

- initialize LSTM model
- cereate linear layer with torch.nn

- initialize loss function: MSE

```
class TrafficVolumePrediction

     - input_size: no. of features in input
     - hidden_dim: no. of hidden LSTM

     - n_layer: no. of lstm layer stacked on top of each otoher
     - output_size: no. of outputs sexpected from model (1 for our reqgression model)
     - window_size: size of window data is to be divided into (480 -> 480/24 = 20 days of data)
```

#### Defining hidden layers

things we do in forward method:
_ extract batch_size from x using size method
_ get hidden functinon to initialize hidden layer

- pass input and get output
- flatten output to single dimension

`torch.utils.data.DataLoader`

3. Set up th eoptimizer
4. set up data
5. Configure training loop

training_step(batch_index, train_batch <data batch from dataloader>)

6. configure validation loop
