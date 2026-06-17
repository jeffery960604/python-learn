import os
import shutil

# Paths
base_dir = "/Users/xiang/Documents/python learning/aerospace_practice"

# Structure mapping
mapping = {
    "pr.py": "01_基礎運算/pr.py",
    "list/list_ex.py": "02_資料結構/列表與元組/list_ex.py",
    "list/list_pr.py": "02_資料結構/列表與元組/list_pr.py",
    "list/tuple_ex.py": "02_資料結構/列表與元組/tuple_ex.py",
    "tuple and list .py": "02_資料結構/列表與元組/tuple_and_list.py",
    "dict/dict_ex.py": "02_資料結構/字典/dict_ex.py",
    "dict/dict_ex2.py": "02_資料結構/字典/dict_ex2.py",
    "dict/dict_pr.py": "02_資料結構/字典/dict_pr.py",
    "for_pr/for_ex.py": "03_控制流程/for_ex.py",
    "for_pr/for＿pr.py": "03_控制流程/for_pr.py",
    "自訂模組/__pycache__/main.py": "04_模組化/main.py",
    "自訂模組/__pycache__/constants.py": "04_模組化/constants.py",
    "自訂模組/__pycache__/physics_engine.py": "04_模組化/physics_engine.py",
}

def organize():
    for src, dst in mapping.items():
        src_path = os.path.join(base_dir, src)
        dst_path = os.path.join(base_dir, dst)
        
        # Create dst dir if not exists (should already exist from my mkdir)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        
        if os.path.exists(src_path):
            print(f"Moving {src} to {dst}")
            _ = shutil.move(src_path, dst_path)
        else:
            print(f"Source not found: {src_path}")

if __name__ == "__main__":
    organize()
    

