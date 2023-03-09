# Bare soil analysis

Analysis of bare soil in fields across England.

## Inputs

Makes use of the following public data sources:

- Satellite reflectance data at 10m² resolution from ESA [Sentinel 2A](https://scihub.copernicus.eu).
- Land cover data at 10m² resolution from [UK CEH](https://catalogue.ceh.ac.uk/documents/017313c6-954b-4343-8784-3d61aa6e44da).
- Rainfall at 1km² resolution from Met Office [HadUK-Grid](https://catalogue.ceda.ac.uk/uuid/4dc8450d889a491ebb20e724debe2dfb).
- LIDAR at 1m² from the Environment Agency's [National LIDAR Programme](https://www.data.gov.uk/dataset/f0db0249-f17b-4036-9e65-309148c97ce4/national-lidar-programme).


## Objective

The objective of this analysis is to build a model to detemine the best predictors of bare soil by building an explanatory model in python.
For the purposes of this study bare soil will be defined as where the Normalised Difference Vegetation Index (NDVI) is below 0.2, as calculated from Sentinel 2A red (B04) and near infared (B08) bands.

## Approach

The dependent variable will be NDVI, or where NDVI < 0.2.

The independant variables will include features engineered from the following aspects:

- Time, e.g. year, day of year
- Land use
- Topography, e.g. slope, altitude, adjacent slopes
- Adjacent vegetation
- Proximity to water courses
- Rainfall

A raster dataset will be created for a location in England and layers will be derived from the above datasets.
A best model will be selected through feature engineering and model selection.
Results will be discussed.