import os

def print_subdirs(root, folders, depth=1):
    print(root)
    for folder in sorted(folders):
        folder_path = os.path.join(root, folder)
        if not os.path.isdir(folder_path):
            continue
        print(f"├── {folder}")
        subdirs = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
        for i, subdir in enumerate(sorted(subdirs)):
            if subdir in ['node_modules', '__pycache__']:  # Skip unwanted folders
                continue
            prefix = "└── " if i == len(subdirs) - 1 else "├── "
            print(f"│   {prefix}{subdir}")

# Run for backend and frontend
print(os.path.basename(os.getcwd()))
print_subdirs(os.getcwd(), ['backend', 'frontend'])