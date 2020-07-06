from skmultiflow.data import AGRAWALGenerator
import pandas as pd
import numpy as np

# 1. Instantiate the stream generator
generator = AGRAWALGenerator()
generator.prepare_for_use()

# 2. Get data from the stream
X, y = generator.next_sample()
print(X.shape, y.shape)


X, y = generator.next_sample(1000)
print(X.shape, y.shape)


# 3. Check if the stream has more data
generator.has_more_samples()


# 4. Restart the stream
generator.restart()

# 5. Save data into a csv file [Optional]
df = pd.DataFrame(np.hstack((X,np.array([y]).T)))
print("df ",df)