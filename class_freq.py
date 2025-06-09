import os
import json
from collections import Counter

def class_frequency(input_dir):
    """
    Count occurrences of labels in JSON files within a directory.
    """
    class_counts = Counter()
    
    json_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]
    total_files = len(json_files)
    
    print(f"Found {total_files} JSON files to process")
    
    for i, filename in enumerate(json_files, 1):
        file_path = os.path.join(input_dir, filename)
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            # shapes and count labels
            if 'shapes' in data and isinstance(data['shapes'], list):
                for shape in data['shapes']:
                    if isinstance(shape, dict) and 'label' in shape:
                        class_counts[shape['label']] += 1
            
            # progress update
            print(f"Processed {i}/{total_files} files", end='\r')
            
        except json.JSONDecodeError:
            print(f"\nError: Could not parse JSON in {filename}")
        except Exception as e:
            print(f"\nError processing {filename}: {str(e)}")
    
    # Print results
    print("\n\nClass counts:")
    print("===================")
    for class_name, count in sorted(class_counts.items()):
        print(f"{class_name}: {count}")
    print("===================")
    print(f"Total unique class types: {len(class_counts)}")
    print(f"Total class instances: {sum(class_counts.values())}")

if __name__ == "__main__":
    # input_directory = "/Mary_Public/Ryan_Team/backup/SP2025/JPEM_3" 
    input_directory = "/Mary_Public/Ryan_Team/backup/April_2_2025/JPEM_2"  
    
    try:
        class_frequency(input_directory)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

