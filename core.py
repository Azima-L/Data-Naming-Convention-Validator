def is_valid_asset_name(file_name, prefixes, extensions, min_length=9):
    if not prefixes or not extensions:
        return False
    if not file_name.startswith(prefixes):
        return False
    if not file_name.endswith(extensions):
        return False
    if len(file_name) < min_length:
        return False
    return True

if __name__ == "__main__":
    print(is_valid_asset_name("SM_Rock.fbx", ("SM_", "SK_"), (".fbx", ".png")))
    print(is_valid_asset_name("rock.fbx", ("SM_", "SK_"), (".fbx", ".png")))
    print(is_valid_asset_name("T_.png", ("T_",), (".png",)))