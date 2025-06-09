
import os
import shutil
from tqdm import tqdm


''' here I make a progress bar based implementation of a backup maker'''
def copy_json_png_pairs(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    total_num_files = 0
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.endswith('.json'):
                # the total number of files is the num of jsons not img
                total_num_files += 1
    
    # progress bar instantizing 
    progress = tqdm(total=total_num_files, desc="Copying files~", unit="file")
    
    # Walk directory
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.endswith('.json'):
                base_name = os.path.splitext(f)[0]
                json_path = os.path.join(root, f)
                png_path = os.path.join(root, f"{base_name}.png")
                shutil.copy2(json_path, output_dir)
                
                if os.path.exists(png_path):
                    shutil.copy2(png_path, output_dir)
                progress.update(1) # updating the progress
    
    progress.close()
    print(f"\nFinished! Copied files to: {output_dir}")

if __name__ == "__main__":
    input_directory = "/Mary_Public/perception_data/2024/20240520_jpem2/processed"  
    output_directory = "/Mary_Public/Ryan_Team/backup/April_25_2025/JPEM_2"  
    
    # input_directory = "/Mary_Public/perception_data/2024/20241104_jpem_3"  
    # output_directory = "/Mary_Public/Ryan_Team/backup/SP2025/JPEM_3"  

    try:
        copy_json_png_pairs(input_directory, output_directory)
    except Exception as e:
        print(f"An error occurred: {str(e)}")