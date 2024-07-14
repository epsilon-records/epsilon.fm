import os
import pathspec

def load_gitignore(directory):
    gitignore_path = os.path.join(directory, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            gitignore_content = f.read()
        return pathspec.PathSpec.from_lines('gitwildmatch', gitignore_content.splitlines())
    return None

def should_ignore(path, spec):
    return spec.match_file(path) if spec else False

def combine_files_by_extension(directory, extensions, ignored_dirs):
    gitignore_spec = load_gitignore(directory)
    
    for ext in extensions:
        output_file = f"combined_{ext.lstrip('.')}.txt"
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for root, dirs, files in os.walk(directory):
                # Skip base directory files and ignored directories
                if root == directory or any(ignored_dir in root for ignored_dir in ignored_dirs):
                    continue
                
                # Remove ignored directories from dirs to skip them during traversal
                for ignored_dir in ignored_dirs:
                    if ignored_dir in dirs:
                        dirs.remove(ignored_dir)

                for file in files:
                    file_path = os.path.join(root, file)
                    # Check if file matches the current extension and is not ignored
                    if file.endswith(ext) and not should_ignore(file_path, gitignore_spec):
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(f"\n// File: {file_path}\n")
                            outfile.write(infile.read())
                            outfile.write("\n")
        print(f"Files with extension {ext} combined into {output_file}")

if __name__ == "__main__":
    # Specify the directory to walk through
    directory = "/opt/src/epsilon.fm"

    # Specify the file extensions to include
    extensions = ['.ts', '.js', '.jsx', '.tsx', '.svelte', '.html', '.css']

    # Specify the directories to ignore
    ignored_dirs = ['node_modules', 'src-tauri', '.git']

    combine_files_by_extension(directory, extensions, ignored_dirs)

