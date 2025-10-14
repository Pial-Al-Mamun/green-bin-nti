import kagglehub
from pathlib import Path
import shutil

# Folder where you want the dataset locally
dataset_dir = Path(__file__).parent / "dataset"
dataset_dir.mkdir(exist_ok=True)

is_dataset_downloaded = Path(__file__).parent / "dataset" / "8"

if is_dataset_downloaded.exists():
    print("The dataset is already downloaded")
    exit()

# Download dataset (will go into KaggleHub cache)
downloaded_path = kagglehub.dataset_download(
    "sumn2u/garbage-classification-v2",
)

# Move the cached dataset into your project folder
final_path = dataset_dir / Path(downloaded_path).name
if final_path.exists():
    shutil.rmtree(final_path)

shutil.move(str(downloaded_path), final_path)

print("Dataset is now in:", final_path)
