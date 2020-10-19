# AI Crop Recommedation System (Beta)

Inputs Paramenters for the Model(s) (listed in the order of priority from highest to lowest):

1. season (for which season, farmer is looking to sow ex: whole-year, kharif, rabi)
2. soil type (fertility of soil) (may be be augmented from area/district)
2. soil pH (in WCS, may be be augmented from area/district)
3. temperature ranges (in WCS, can be augmented from area/district)
4. humidity ranges (in WCS, can be augmented from area/district)
5. natural water availability (in WCS, can be augmented from area/district)
6. farmland terrian/topography (in WCS, can be augmented from area/district)
7. last crop cultivated (*hard to get)
8. farmland area (in acres)
9. current crop (*optional)
10. current revenue (*optional)

```* WCS = Worst Case Scenario```


### Additional Comments

* A merely Acceptable Dataset found [here](https://data.gov.in/catalog/district-wise-season-wise-crop-production-statistics?filters%5Bfield_catalog_reference%5D=87631&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc)
    * Drawbacks
        * Very limited number of dimentions(features)
        * Amiguity arises as Dataset's info says data is from 1997 but dataset iteslf has records from 2000-2014. ***Assuming** that the decision to start collecting was conceptualized in 1997.*

