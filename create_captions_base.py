import os 
import json 

# Initializing and Setting folder names
# input = "/Mary_Public/perception_data/2025/Jacob_USC_Lake_Murray_LDM/compiled"
# output = "/Mary_Public/perception_data/2025/Jacob_USC_Lake_Murray_LDM/output_json"
# jsonl_f = "metadata.jsonl"

input = "/Mary_Public/Ryan_Team/Experiments/LDM/LDM_results/Cropped_RHIBs/min_json_size_5000" 
output = "/Mary_Public/Ryan_Team/Experiments/LDM/LDM_results/Cropped_RHIBs/min_json_size_5000_labels" 
jsonl_f = "metadata.jsonl"

prompt = "JPEM-style RHIB"

# create the output_dir if that wasn't created yet 
os.makedirs(output, exist_ok=True)
jsonl_path = os.path.join(input, jsonl_f) # create the jsonl file INSIDE of the output folder 

# First open the JSONL file in write mode
with open(jsonl_path, "w") as jsonl_file: 
    # Then iterate through the files in the input dir 
    counter = 0
    for f in os.listdir(input): # f is for filename
        counter += 1
        if f.endswith("g"): # here we generate the JSON filename
            json_f = os.path.splitext(f)[0] + ".json" 
            print(counter)

            json_path = os.path.join(output, json_f) 
            with open(json_path, "w") as json_file: 
                json.dump({"text": prompt}, json_file) 
                jsonl_entries = { "file_name": f, "text": prompt} 
            jsonl_file.write(json.dumps(jsonl_entries) + "\n")
            print("success: JSON and JSONL files have been created.")

