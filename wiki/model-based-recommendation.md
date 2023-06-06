Collaborative Dimension:
<<<<<<< HEAD

Possibilities
1. Sklearn
2. Surprise Library (Python)

3. Surprise Library:
- Singular Value Decomposition using SVD or SVDpp (latter separately keeps track of whether the user rated the item or not)
=======
Using User-Item (Song) Matrix of Occurence
-> Decompose into underlying Latent Factors Matrix by reducing dimensionality into more useful lower space
-> minimizing the loss between the reconstructed matrix and the original matrix
-> then can use inner product of **user and item latent factor matrix** for inferencing an **unobserved rating** (Matrix Factorization, Model based Prediction)

Possibilities (https://towardsdatascience.com/a-complete-guide-to-recommender-system-tutorial-with-sklearn-surprise-keras-recommender-5e52e8ceace1)
1. Truncated Singular Value Decomposition with Sklearn
2. Funk Matrix Factorization with Surprise 
3. Generalized Matrix Factorization with Keras

1. TruncatedSVD, Sklearn:
- TruncatedSVD is a variant of the Singular Value Decomposition that calculates only the K largest singular value (n_components)
- applies the **_linear dimensionality reduction_** and works well with sparse matrix
![[Screenshot 2023-06-06 at 09.40.53.png]]
- value of each cell will be the estimated value that satisfies the optimization constraint
- **Frage**: Was wäre user-item matrix in unserem Fall genau? Und warum bildet man sowohl eine User Latent Factor Matrix und Item Latent Factor Matrix
Hyperparameters:
- Epsilon
- n_components
- ...
Performance:
- recommendation would be based on some latent factors that we cannot explain directly compared to the explicit or implicit rating from the memory-based approach
- 
1. Funk MF with Surprise Library:
- Similar to Singular Value Decomposition using SVD or SVDpp (latter separately keeps track of whether the user rated the item or not)
>>>>>>> 6706132f34b92d1a15a957d1e6807b051b0d8bb9
![[Screenshot 2023-06-05 at 16.26.26.png]]
- _pᵤ_ and _qᵢ_ are vectors, and their length is a hyperparameter of the model, _n_. They are the actual [matrix-factorisation](https://en.wikipedia.org/wiki/Matrix_factorization_(recommender_systems)) part of the model
- Next, we need the preprocessed dataset to train our model, preproc is similar, however slight difference since here Surprise is used 
- Then we can fit, test and predict
Performance:
- Using the `pu`, `qi`, `bu` and `bi` methods of an `SVD` object, you can get the corresponding values from the math formula
- By calling methods we get 2D Array where each row represents an item with `n_factor` number of factors, these are the so-called latent factors that the model found, and they represent the item in the rating calculations
- A way to take this analysis one step further would be to use these latent factors as a basis for a cluster analysis
Hyperparameters:
- n_factors -> size of p and q vectors -> how many latent factors the model will try to find
- n_epochs -> how many times the gradient descent calculations are repeated
- lr_all -> learning rate for all params -> step sizes the model will use to minimise the cost function
- reg_all -> regularization for all params -> Surprise uses an L2 regularisation
- Can GridSearch for best Parameters
Conclusion:
- Straightforward approach to do model based approach for collaborative dimension
- Drawback: uses another Library (not Scikit)
- Problem: unsure about the output of model and if that is sufficient for our goal

<<<<<<< HEAD
To dig in deeper:
Which one to pick?
- user-item similarity
- item-user similarity
- item-item similarity (content?)
=======
>>>>>>> 6706132f34b92d1a15a957d1e6807b051b0d8bb9
