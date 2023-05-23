def remove_unwanted_subjects(list_subjects):
    remove_subjects = [".github", "Media", "Project", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "LICENSE", "README.md","mlc_config.json"]
    updated_list = [x for x in list_subjects if x not in remove_subjects]
    return updated_list