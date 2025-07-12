# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

TODO
This allows boats to have an even distribution of data allowing for maximum storage. A downside would be that we need to query all boats to find all instances of observations at a certain time.

## Partitioning by Hour

TODO
This means that some boats might have to store more observations than others meaning less efficient storage space. This also means that when querying for an observation at a certain time you only have to look through certain boats as you know what timeframes they cover.

## Partitioning by Hash Value

TODO
This method allows for even distribution of data so maximum storage. But since the hash values are assigned arbitrarily you would have to query all boats to find observations within a certain timeframe. Since hash values are deterministic you only have to query one boat to find an observation with a certain timestamp.
