import git
import os

def iterate_over_child_directories(parent_dir):
    i = 0
    with os.scandir(parent_dir) as it:
        for entry in it:
            if entry.is_dir():
                yield entry.path

def check_if_git_project(dir_to_check):
    try:
        repo = git.Repo(dir_to_check)
    except (git.InvalidGitRepositoryError, git.NoSuchPathError):
        return False
    
    return True

def make_lists(parent_dir):
    git_dirs, non_git_dirs = [], []

    for child_dir in iterate_over_child_directories(parent_dir):
        target = git_dirs if check_if_git_project(parent_dir) else non_git_dirs
        target.append(child_dir)

    return git_dirs, non_git_dirs

def version_control_verification(parent_dir):
    git_dirs, non_git_dirs = make_lists(parent_dir)
    print("Git Directories: \n{}\n", git_dirs)
    print("\nNon-Git Directories: \n{}\n", non_git_dirs)

def input_parent_path_util():
    dir_path = input("Enter directory_path: ")

    if os.path.isdir(dir_path):
        version_control_verification(dir_path)
    
def main():
    input_parent_path_util()

if __name__ == "__main__":
    main()