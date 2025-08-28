# reading from a file 
import os
input_file_path =  'week 4/input.txt'
output_file_path = 'week 4/output.txt' 
input_file_path = 'week 4/input.txt'
with open('week 4/input.txt') as file:
    content = file.read()
    print(content)

 # append the inpt text
    with open('week 4/input.txt', 'a') as file:
     file.write('welcome to the topic')

# print and read the updated file
     with open('week 4/input.txt') as file:
              print(file.read())

# modify the text by converting all the characters to uppercase
modified_content = content.upper()

# write the modified content to a new file
with open(output_file_path, 'a') as output_file:
            output_file.write(modified_content)

print(f"Success! the modified text has been saved to '{output_file_path}'.")

print(f"Error: The file '(input_file_path)' was not found.")
print("Please make sure the file exists in the specified directory.")

print(f"An unexpected error occurred: (e)")








