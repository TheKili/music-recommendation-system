## API actions
api:
	uvicorn recommender.API.fast:app --reload --port 8000

get_welcome:
	python -c 'from recommender.utils_api import get_welcome; get_welcome()'

get_recommendations:
	python -c 'from recommender.utils_api import get_recommendations; get_recommendations()'

get_spotify_data:
	python -c 'from recommender.utils_api import get_spotify_data; get_spotify_data()'

## create_data_matrix

## install_dependencies


## data_reduction_xyz
