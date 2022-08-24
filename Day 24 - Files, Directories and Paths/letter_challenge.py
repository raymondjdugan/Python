PLACEHOLDER = "[name]"


with open("./input/names/invited_names.txt") as name_data:
    names = name_data.readlines()

with open("./input/letters/starting_letter.txt") as letter_data:
    letter_contents = letter_data.read()
    for name in names:
        striped_name = name.strip()
        new_starting_letter = letter_contents.replace(PLACEHOLDER, striped_name)
        with open(f"./output/ready_letters/letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_starting_letter)

