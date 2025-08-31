from huggingface_hub.utils import RepositoryNotFoundError, HfHubHTTPError
from huggingface_hub import HfApi, create_repo
import os


repo_id = "harikbab02/Bank-Customer-Churn-2"
repo_type = "dataset"

# Initialize API client
api = HfApi(token=os.getenv("HF_TOKEN"))

# Step 1: Check if the space exists
try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Space '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Space '{repo_id}' not found. Creating new space...")
    create_repo(repo_id=repo_id, repo_type=repo_type, private=False)
    print(f"Space '{repo_id}' created.")

# Step 2: Check if the 'data' directory exists
data_dir = "data"
if not os.path.isdir(data_dir):
    print(f"Error: The directory '{data_dir}' does not exist. Please create it and add your data files before running this script.")
    exit(1)

# Step 3: Upload the folder
api.upload_folder(
    folder_path=data_dir,
    repo_id=repo_id,
    repo_type=repo_type,
)
