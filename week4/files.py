# filename = "some_folder/demofile.txt"
#
# with open(filename) as the_file:
#     contents = the_file.read()
#     print(contents)

# filename = "programming.txt"
# with open(filename, "w") as the_file:
#     the_file.write("programming is fun\n")
#     the_file.write("hello python")


def count_words(filename):
    with open(filename) as the_file:
        contents = the_file.read()
        words = contents.split()
        num_words = len(words)
        # print("The file " + filename + " has about " + str(num_words) + " words")
        print("The file {} has about {} words".format(filename, num_words))

filename = "some_folder/demofile.txt"
count_words(filename)
