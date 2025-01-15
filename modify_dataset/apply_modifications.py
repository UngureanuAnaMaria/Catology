from modify_dataset.add_physical_traits.bengal import add_bengal_traits
from modify_dataset.add_physical_traits.birman import add_birman_traits
from modify_dataset.add_physical_traits.british_shorthair import add_british_shorthair_traits
from modify_dataset.add_physical_traits.chartreux import add_chartreux_traits
from modify_dataset.add_physical_traits.european_shorthair import add_european_shorthair_traits
from modify_dataset.add_physical_traits.maine_coon import add_maine_coon_traits
from modify_dataset.add_physical_traits.persian import add_persian_traits
from modify_dataset.add_physical_traits.ragdoll import add_ragdoll_traits
from modify_dataset.add_physical_traits.savannah import add_savannah_traits
from modify_dataset.add_physical_traits.siamese import add_siamese_traits
from modify_dataset.add_physical_traits.sphynx import add_sphynx_traits
from modify_dataset.add_physical_traits.turkish_angora import add_turkish_angora_traits
from modify_dataset.delete_columns import delete_columns
from modify_dataset.sort_dataset import sort_by_breed_sex_age
from modify_dataset.update_age_column import update_age_column
from modify_dataset.update_behavior_columns import rename_behavior_columns, update_behavior_columns
from modify_dataset.update_breed_column import update_breed_column, move_breed_column
from modify_dataset.update_sex_column import update_sex_column


def apply_modifications(file_path):

    print(f"Modifying dataset {file_path}")

    delete_columns(file_path)
    update_age_column(file_path)
    rename_behavior_columns(file_path)
    update_behavior_columns(file_path)
    update_breed_column(file_path)
    move_breed_column(file_path)
    update_sex_column(file_path)

    add_bengal_traits(file_path)
    add_birman_traits(file_path)
    add_british_shorthair_traits(file_path)
    add_chartreux_traits(file_path)
    add_european_shorthair_traits(file_path)
    add_maine_coon_traits(file_path)
    add_persian_traits(file_path)
    add_ragdoll_traits(file_path)
    add_savannah_traits(file_path)
    add_siamese_traits(file_path)
    add_sphynx_traits(file_path)
    add_turkish_angora_traits(file_path)

    sort_by_breed_sex_age(file_path)


apply_modifications(r"C:\Users\User\Desktop\Catology.xlsx")
