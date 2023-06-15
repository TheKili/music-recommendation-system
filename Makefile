## API actions
api:
	uvicorn recommender.API.fast:app --reload --port $$PORT

get_env:
	python -c 'from recommender.utils_api import get_env; get_env()'

get_welcome:
	python -c 'from recommender.utils_api import get_welcome; get_welcome()'

get_spotify_data:
	python -c 'from recommender.utils_api import get_spotify_data; get_spotify_data()'

get_recommendations:
	python -c 'from recommender.utils_api import get_recommendations; get_recommendations()'


get_env_gcp:
	python -c 'from recommender.utils_api import get_env_gcp; get_env_gcp()'

get_welcome_gcp:
	python -c 'from recommender.utils_api import get_welcome_gcp; get_welcome_gcp()'

get_spotify_data_gcp:
	python -c 'from recommender.utils_api import get_spotify_data_gcp; get_spotify_data_gcp()'

get_recommendations_gcp:
	python -c 'from recommender.utils_api import get_recommendations_gcp; get_recommendations_gcp()'


get_recommendations_test:
	python -c 'from recommender.utils_api import get_recommendations_test; get_recommendations_test()'



## create_data_matrix

## install_dependencies

## data_reduction_xyz
